#!/usr/bin/env python3

import json
import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TMP_DIR = Path("/tmp/minimax_h3_x_threads")
DATA_FILE = REPO_ROOT / "data" / "community-x-minimax-h3-cases.json"
VIDEO_DIR = REPO_ROOT / "videos" / "generated"

ITEMS = [
    {
        "id": "x-mm-h3-01",
        "tweet_id": "2084227244533411987",
        "title_en": "ABC Learning Explainer",
        "title_zh": "ABC 儿童学习动画",
        "prompt_mode": "thread_tail",
        "readme_video_url": "https://github.com/user-attachments/assets/fecbdb24-fafc-4c1f-8d8f-af8edb184366",
    },
    {
        "id": "x-mm-h3-02",
        "tweet_id": "2087102541146522089",
        "title_en": "Street Photographer Candid Moment",
        "title_zh": "街头摄影师抓拍瞬间",
        "prompt_mode": "root_prompt",
        "readme_video_url": "https://github.com/user-attachments/assets/73580897-499e-4d7b-b33f-f813d7e24304",
    },
    {
        "id": "x-mm-h3-03",
        "tweet_id": "2082499539735588916",
        "title_en": "Speeder Chase Across a Cliff City",
        "title_zh": "悬崖城市飞车追逐",
        "prompt_mode": "root_prompt",
        "readme_video_url": "https://github.com/user-attachments/assets/f181a998-ac6a-4402-b47b-c51fc4da833c",
    },
    {
        "id": "x-mm-h3-04",
        "tweet_id": "2084298391107055692",
        "title_en": "Local Generation Showcase",
        "title_zh": "本地生成展示",
        "prompt_mode": "missing",
        "readme_video_url": "https://github.com/user-attachments/assets/813dd424-5028-40f5-8575-282fd2096c79",
    },
    {
        "id": "x-mm-h3-05",
        "tweet_id": "2084838553943449908",
        "title_en": "The Office Kim Jong Un Blooper",
        "title_zh": "办公室金正恩笑场片段",
        "prompt_mode": "root_prompt",
        "readme_video_url": "https://github.com/user-attachments/assets/1866164a-7dab-4e17-9586-77a98c7675a1",
    },
    {
        "id": "x-mm-h3-06",
        "tweet_id": "2084353489061499021",
        "title_en": "Jim and Dwight Discuss Coding Agents",
        "title_zh": "Jim 与 Dwight 讨论编码智能体",
        "prompt_mode": "quoted_prompt",
        "readme_video_url": "https://github.com/user-attachments/assets/a274ccc4-e425-4166-9d06-003b051a4fa5",
    },
    {
        "id": "x-mm-h3-07",
        "tweet_id": "2086553240448241802",
        "title_en": "Beat-Synced Character Showcase",
        "title_zh": "节拍同步角色环境展示",
        "prompt_mode": "root_prompt",
        "readme_video_url": "https://github.com/user-attachments/assets/4ed145a5-407d-492b-8a23-0412bf94b489",
    },
    {
        "id": "x-mm-h3-08",
        "tweet_id": "2084600512180113820",
        "title_en": "AI Cannot Replace Joey",
        "title_zh": "AI 替代不了 Joey",
        "prompt_mode": "thread_tail",
        "readme_video_url": "https://github.com/user-attachments/assets/a43c1430-7973-4786-973e-e413070ab832",
    },
]


def fetch_thread_json(tweet_id: str) -> dict:
    cache_file = TMP_DIR / f"{tweet_id}.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text())

    result = subprocess.run(
        [
            "curl",
            "-L",
            "--max-time",
            "90",
            "-A",
            "Mozilla/5.0",
            f"https://twitter-thread.com/api/unroll-thread?id={tweet_id}",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(result.stdout)
    return json.loads(result.stdout)


def extract_best_video_url(tweet: dict) -> str | None:
    video = tweet.get("video")
    if not video:
        return None
    mp4_sources = [
        source
        for source in (video.get("sources") or [])
        if source.get("contentType") == "video/mp4"
    ]
    if not mp4_sources:
        return None
    return max(mp4_sources, key=lambda item: item.get("bitrate", 0))["url"]


def strip_prompt_prefix(text: str) -> str:
    text = re.sub(r"https://t\.co/\S+", "", text).strip()
    patterns = [
        r"^.*?MiniMax H3 Prompt:\s*",
        r"^.*?Minimax H3 Prompt:\s*",
        r"^.*?H3 bloppers prompt is below\s*👇\s*",
        r"^.*?Prompt\s*:\s*",
        r"^.*?Prompt:\s*",
        r"^.*?prompt:\s*",
    ]
    for pattern in patterns:
        stripped = re.sub(pattern, "", text, flags=re.IGNORECASE | re.DOTALL)
        if stripped != text:
            return stripped.strip()
    return text


def extract_prompt(thread: dict, prompt_mode: str) -> tuple[str, str]:
    tweets = thread["tweets"]
    if prompt_mode == "missing":
        return (
            "[Prompt not available in the original tweet or archived thread as of 2026-08-12.]",
            "missing",
        )
    if prompt_mode == "thread_tail":
        prompt = "\n\n".join((tweet.get("text") or "").strip() for tweet in tweets[1:]).strip()
        return strip_prompt_prefix(prompt), "complete"
    root_text = (tweets[0].get("text") or "").strip()
    if prompt_mode == "quoted_prompt":
        match = re.search(r'Prompt was\s+"([^"]+)"', root_text, re.IGNORECASE)
        if match:
            return match.group(1).strip(), "complete"
    return strip_prompt_prefix(root_text), "complete"


def main() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    cases = []

    for item in ITEMS:
        payload = fetch_thread_json(item["tweet_id"])
        if not payload.get("ok"):
            raise RuntimeError(f"Thread fetch failed for {item['tweet_id']}: {payload}")
        thread = payload["thread"]
        root_tweet = thread["tweets"][0]
        prompt, prompt_status = extract_prompt(thread, item["prompt_mode"])
        video_url = extract_best_video_url(root_tweet)
        if not video_url:
            raise RuntimeError(f"No downloadable video found for {item['tweet_id']}")

        local_name = f"{item['id']}.mp4"
        local_path = VIDEO_DIR / local_name
        if not local_path.exists():
            subprocess.run(["wget", "-q", "-O", str(local_path), video_url], check=True)

        cases.append(
            {
                "id": item["id"],
                "category": "community",
                "title": {
                    "fallback": {
                        "zh": item["title_zh"],
                        "en": item["title_en"],
                    }
                },
                "prompt": {
                    "originalLanguage": "en",
                    "fallback": {
                        "zh": prompt,
                        "en": prompt,
                    },
                },
                "src": local_name,
                "media": {"images": [], "videos": []},
                "source": {
                    "platform": "x",
                    "tweetUrl": thread["url"],
                    "threadUrl": thread["threadUrl"],
                    "author": {
                        "name": thread["author"]["name"],
                        "username": thread["author"]["username"],
                    },
                    "archivedAt": "2026-08-12",
                    "promptStatus": prompt_status,
                },
                "readmeVideoUrl": item["readme_video_url"],
            }
        )

    DATA_FILE.write_text(json.dumps(cases, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
