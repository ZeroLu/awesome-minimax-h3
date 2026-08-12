#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
community_cases="$repo_root/data/community-x-minimax-h3-cases.json"

render_cases() {
  local language="$1"
  local prompt_field="$2"

  jq -r --arg language "$language" --arg prompt_field "$prompt_field" '
    def file: split("/") | last;
    def category:
      if .id | IN("x-mm-h3-01") then "education-explainers"
      elif .id | IN("x-mm-h3-02") then "documentary-vlog-realism"
      elif .id | IN("x-mm-h3-03") then "cinematic-action"
      elif .id | IN("x-mm-h3-05", "x-mm-h3-06", "x-mm-h3-08") then "sitcom-character-dialogue"
      elif .id | IN("x-mm-h3-07") then "music-synced-showcases"
      else "community-showcases"
      end;
    def category_title:
      if . == "education-explainers" then "1. Education & Explainers"
      elif . == "documentary-vlog-realism" then "2. Documentary & Vlog Realism"
      elif . == "cinematic-action" then "3. Cinematic Action"
      elif . == "sitcom-character-dialogue" then "4. Sitcom & Character Dialogue"
      elif . == "music-synced-showcases" then "5. Music-Synced Showcases"
      else "6. Community Showcases"
      end;
    def title: (.title.fallback[$language] // .title.fallback.en);
    def prompt_header:
      if $language == "zh" then
        if (.prompt.originalLanguage // "en") == "zh" then "提示词（中文）" else "提示词（原文）" end
      else
        if (.prompt.originalLanguage // "en") == "zh" then "Prompt (English)" else "Prompt (Original English)" end
      end;
    def source_block:
      "#### " + (if $language == "zh" then "来源" else "Source" end) + "\n\n" +
      "[@"
      + .source.author.username
      + "](https://x.com/"
      + .source.author.username
      + ")"
      + " · [X Post]("
      + .source.tweetUrl
      + ")"
      + (if .source.promptStatus == "missing"
          then "\n\n> " + (if $language == "zh" then "截至 2026-08-12，公开抓取结果中未找到完整 prompt。" else "Complete prompt was not found in public captures as of August 12, 2026." end)
          else ""
        end)
      + "\n\n";
    map(select((.source.promptStatus // "complete") == "complete")) as $items |
    ["education-explainers", "documentary-vlog-realism", "cinematic-action", "sitcom-character-dialogue", "music-synced-showcases", "community-showcases"]
    | map(
        . as $cat |
        ($items | map(select(category == $cat)) | sort_by(.id)) as $group |
        if ($group | length) == 0 then ""
        else
          "## " + ($cat | category_title) + "\n" +
          ($group | map(
            "### \(title)\n\n" +
            "#### " + (if $language == "zh" then "结果视频" else "Result Video" end) + "\n\n" +
            (if .readmeVideoUrl then .readmeVideoUrl else "[" + (.src | file) + "](./videos/generated/" + (.src | file) + ")" end) + "\n\n" +
            source_block +
            "#### " + prompt_header + "\n\n```text\n\(.prompt.fallback[$prompt_field])\n```\n"
          ) | join("\n")) + "\n"
        end
      ) | join("")
  ' "$community_cases"
}

{
  cat <<'EOF'
# Awesome MiniMax H3

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/ZeroLu/awesome-minimax-h3?style=social)](https://github.com/ZeroLu/awesome-minimax-h3/stargazers)

| [English](./README.md) | [简体中文](./README-zh.md) |

> A curated library of community **MiniMax H3** prompts collected from standout X showcases.

Only community X examples with archived prompts are shown in the main README. Prompt wording remains as close as possible to the original posts.

## Table of Contents

1. [Education & Explainers](#1-education--explainers)
2. [Documentary & Vlog Realism](#2-documentary--vlog-realism)
3. [Cinematic Action](#3-cinematic-action)
4. [Sitcom & Character Dialogue](#4-sitcom--character-dialogue)
5. [Music-Synced Showcases](#5-music-synced-showcases)
6. [Community Showcases](#6-community-showcases)

---
EOF
  render_cases en en
  cat <<'EOF'
---

## Source & Notes

- Community X cases are archived from public X posts and public mirror captures on August 12, 2026.
- Items without a complete public prompt are kept in [`data/community-x-minimax-h3-cases.json`](./data/community-x-minimax-h3-cases.json), but are not rendered in the main prompt list.
- The machine-readable source record is available at [`data/community-x-minimax-h3-cases.json`](./data/community-x-minimax-h3-cases.json).
EOF
} > "$repo_root/README.md"

{
  cat <<'EOF'
# Awesome MiniMax H3

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/ZeroLu/awesome-minimax-h3?style=social)](https://github.com/ZeroLu/awesome-minimax-h3/stargazers)

| [English](./README.md) | [简体中文](./README-zh.md) |

> 收集整理自精选 X 帖子的 **MiniMax H3** 社区提示词库。

主 README 只展示已经公开归档完整 prompt 的社区 X 案例，并尽量保留原帖提示词原貌。

## 目录

1. [Education & Explainers](#1-education--explainers)
2. [Documentary & Vlog Realism](#2-documentary--vlog-realism)
3. [Cinematic Action](#3-cinematic-action)
4. [Sitcom & Character Dialogue](#4-sitcom--character-dialogue)
5. [Music-Synced Showcases](#5-music-synced-showcases)
6. [Community Showcases](#6-community-showcases)

---
EOF
  render_cases zh zh
  cat <<'EOF'
---

## 来源与说明

- 社区 X 案例归档自 2026 年 8 月 12 日公开可访问的 X 帖子与公开镜像抓取结果。
- 未找到完整公开 prompt 的条目保留在 [`data/community-x-minimax-h3-cases.json`](./data/community-x-minimax-h3-cases.json)，但不展示在主提示词列表中。
- 完整结构化案例数据位于 [`data/community-x-minimax-h3-cases.json`](./data/community-x-minimax-h3-cases.json)。
EOF
} > "$repo_root/README-zh.md"
