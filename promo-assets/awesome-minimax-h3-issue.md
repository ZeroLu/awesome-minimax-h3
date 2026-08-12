# 外网热传！AI 视频提示词库 Awesome MiniMax H3 来袭，手把手拆解 H3 生成案例！（附 GIF 与中文对照）

![Awesome MiniMax H3](https://raw.githubusercontent.com/ZeroLu/awesome-minimax-h3/main/assets/awesome-minimax-h3-cover.png)

## 【内容摘要】

这篇文章整理了一个开源提示词仓库 **Awesome MiniMax H3**，专门收集 MiniMax H3 / Hailuo AI 在 X 上流传的高质量视频案例，并把视频、原始提示词、中文对照与可复用写法整理在一起。

如果你也遇到过这种情况：别人随手一条提示词就能生成电影感镜头、真实街拍、情景喜剧和节拍卡点短片，而你生成出来总是动作断、镜头乱、角色漂，那么问题很可能不只是模型，而是提示词没有把“时间、镜头、动作、物理关系和声音节奏”写清楚。

我把这些案例做成了仓库：

👉 **GitHub：** https://github.com/ZeroLu/awesome-minimax-h3?utm_source=awesome_minimax_h3_issue&utm_medium=github_issue

下面直接拆案例。

---

## 一、儿童教育：把“字母教学”写成完整时间轴

![ABC Learning Explainer](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-01.gif)

这个案例不是简单写“做一个 ABC 教学动画”，而是把学习流程拆成固定模板：

> LETTER → SOUND → OBJECT → PLAYFUL ACTION → OBJECT NAME

中文理解就是：

> 字母 → 发音 → 对应物体 → 有趣动作 → 物体名称

提示词还继续规定了受众、视觉风格、背景、每一秒发生什么，以及旁白怎么说。例如 A 的部分要求大写 A 和小写 a 出现，然后 A 变成红苹果，苹果有表情并轻轻弹跳，最后显示 `APPLE`，并高亮首字母 A。

这个案例最值得学的是：**教育类视频不要只写主题，要写学习路径**。模型知道每一步的目标后，画面会更稳定，也更像真正给孩子看的内容。

---

## 二、街头纪实：让模型处理“相机互动”和真实小动作

![Street Photographer Candid Moment](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-02.gif)

这个提示词的核心是一个很具体的街拍动作：

> 一位年轻的西方女性街头摄影师走过热闹市中心，注意到咖啡馆外一位老人和他的小狗。她通过相机构图，拍下这一瞬间，然后把相机转向观众，骄傲地展示刚拍到的照片。

后面继续追加约束：

> 超写实画面、自然手持纪录片运动、真实相机互动、自然表情、准确手部动作、真实狗狗行为、自然日光、电影景深、角色一致性、沉浸式城市环境声。

这个案例说明 MiniMax H3 类模型很吃“可表演动作”。你要把人物先看见什么、怎么拿相机、怎么展示结果、说什么话写出来，而不是只写“街头摄影师拍照”。

---

## 三、电影动作：用“一镜到底”控制高速追逐

![Speeder Chase Across a Cliff City](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-03.gif)

这个案例是悬崖城市飞车追逐，提示词开头就定了关键规则：

> Speeder chase across a cliff city (single continuous shot)

中文意思是：

> 悬崖城市中的飞车追逐，单个连续镜头。

然后它不是泛泛描述“飞车很快”，而是把镜头路径写得非常具体：

> 摄影机从巨大的石雕悬崖城市俯冲而下，锁定一束沿窄路疾驰的光。镜头先冲到前方，再甩回后方，贴近推进器；热浪、碎石、警示灯、坍塌阳台、拱门、晾衣绳、窗户连续出现，最后冲出城市，看到瀑布山谷和彩虹水雾。

动作片提示词的关键不是形容词堆叠，而是 **空间路径**。把镜头怎么追、怎么穿、怎么转、最后怎么揭示大场景写清楚，模型才更容易生成“电影镜头”。

---

## 四、社媒整活：用“假花絮”制造喜剧节奏

![The Office Kim Jong Un Blooper](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-05.gif)

这个案例的关键词是：

> Blooper take

也就是“花絮片段”。提示词把 15 秒拆成多个段落：

> 0:00-0:04，中景，Michael Scott 在 Dunder Mifflin 门口开门，兴奋迎接来宾。  
> 0:04-0:07，他继续唱着童谣式节奏，并配合节拍做夸张动作。  
> 0:07-0:10，对方努力憋笑，肩膀开始抖。  
> 0:10-0:13，Michael 也笑场。  
> 0:13-0:15，两个人彻底破功，视频结束在笑场瞬间。

这种写法适合做短视频梗图、伪纪录片、办公室喜剧和名场面二创。重点是：不要只写“搞笑”，要写出 **谁先绷不住、谁接着破功、镜头停在哪个表情上**。

---

## 五、音乐卡点：用结构化约束做 30 个镜头

![Beat-Synced Character Showcase](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-07.gif)

这个提示词很适合做角色展示、游戏角色宣传片、IP 短视频。它要求：

> 使用角色参考作为严格角色参考，使用音频参考作为节奏和剪辑参考。保持角色身份、比例、发型、服装、颜色和整体风格一致。

结构写得非常硬：

> 5 个环境  
> 每个环境 3 秒  
> 每个环境 6 个 burst-cut 镜头  
> 总计 30 个镜头

还要求每次切换都落在强拍、半拍或音乐重音上，并且每个环境要在氛围、光线、尺度和视觉语言上明显不同。

这个案例最适合总结成一句话：**卡点视频不要只写“跟着音乐剪”，要写镜头数量、环境数量、每段时长和切点规则。**

---

## 六、情景喜剧：把对白、停顿和表情写进提示词

![AI Cannot Replace Joey](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-08.gif)

这个案例是经典情景喜剧式对白：

> Joey 和 Chandler 坐在沙发上，拿着咖啡杯。Joey 真诚又担心地问：“AI 会取代我们吗？”

然后提示词继续写 Chandler 的表演：

> Chandler 慢慢从咖啡杯上抬头，停顿，直视 Joey。  
> Chandler 用疲惫的冷幽默语气回答。  
> 最后一行说完后，镜头在 Chandler 的脸上多停一拍再切。

很多人做 AI 对话视频只写台词，忽略了喜剧真正依赖的是 **停顿、视线、反应和最后一拍**。这个案例把这些都写进去了，所以画面会更像 sitcom，而不是两个角色机械念台词。

---

## 独家福利一：MiniMax H3 视频提示词怎么写？

我建议把 MiniMax H3 提示词拆成 7 层：

1. **视频类型**：电影动作、街头纪实、产品广告、情景喜剧、儿童教育、音乐卡点。
2. **主体与目标**：谁在画面里，他要完成什么动作。
3. **时间轴**：0-3 秒、3-7 秒、7-12 秒分别发生什么。
4. **镜头语言**：手持、推近、环绕、低角度、航拍、一镜到底、特写。
5. **物理互动**：手怎么拿物体、角色怎么转身、狗怎么动、碎石怎么飞。
6. **声音与对白**：旁白、台词、语气、停顿、音乐强拍。
7. **硬约束**：角色不变、服装不变、不重复构图、不加 UI、不模糊、不变形。

一个可复用模板：

```text
Create a [duration]-second [video type] video.

Subject:
[main character / object / creature], with consistent identity, outfit, proportions and style.

Scene:
[location, time of day, lighting, atmosphere].

Timeline:
0:00-0:03 - [action + camera movement]
0:03-0:07 - [action + interaction + camera movement]
0:07-0:12 - [turning point / reveal / expression]
0:12-0:15 - [ending beat / final frame]

Camera:
[handheld / cinematic dolly / tracking / orbit / close-up / wide reveal].

Audio:
[dialogue / narration / music rhythm / sound effects].

Style:
[photorealistic / 90s sitcom / premium 3D animation / cinematic sci-fi].

Hard constraints:
Maintain character consistency. No morphing. No extra text or UI unless specified. No repeated framing. Natural motion and realistic interactions.
```

---

## 独家福利二：MiniMax H3 提示词生成器（Meta-Prompt）

如果你不想每次从零写，可以直接把下面这段交给 AI，让它帮你生成英文视频提示词：

```text
You are a professional AI video prompt writer for MiniMax H3 / Hailuo AI.

I will give you a rough video idea. Turn it into a complete English video prompt.

Requirements:
- Write for a 15-second AI video unless I specify another duration.
- Include subject, scene, visual style, camera movement, action timeline, sound/dialogue if needed, and hard constraints.
- Use precise physical actions instead of vague adjectives.
- Break the video into timestamped beats.
- Describe how the camera moves through space.
- Add consistency constraints for characters, outfit, identity, hands, objects and environment.
- If the idea is funny, write the comedic timing: pause, reaction, expression, final beat.
- If the idea is cinematic, write the spatial path, reveal, lighting and motion accents.
- If the idea is synced to music, define the number of cuts, sections, beat accents and transition timing.

My rough idea:
[在这里输入你的视频想法]
```

---

## FAQ

### Q1：Awesome MiniMax H3 是什么？

一个开源 MiniMax H3 视频提示词仓库，整理公开社区案例、视频效果、原始提示词、中文对照和可复用写法。

👉 https://github.com/ZeroLu/awesome-minimax-h3?utm_source=awesome_minimax_h3_issue&utm_medium=github_issue

### Q2：为什么同样是 MiniMax H3，别人生成效果更好？

通常差别在提示词结构。高质量案例会写清楚角色、镜头、时间轴、动作、对白、物理关系和约束，而不是只写一句主题。

### Q3：MiniMax H3 更适合做什么？

从目前这些社区案例看，它很适合电影动作、街头纪实、情景喜剧、儿童教育、音乐卡点角色展示和社媒短视频梗图。

### Q4：仓库里所有视频都有提示词吗？

大部分都有。个别 X 链接没有公开完整提示词，仓库里会标注状态；没有提示词的案例不强行补。

---

## 总结

AI 视频正在从“写一句话碰碰运气”进入“像导演一样写提示词”的阶段。

MiniMax H3 的关键不是多堆形容词，而是把 **时间、空间、动作、镜头、声音和约束** 写出来。你写得越像分镜，模型越容易给你稳定、连贯、有节奏的视频。

我已经把这些案例整理成了开源仓库，后续会继续补充更多提示词：

👉 **Awesome MiniMax H3：** https://github.com/ZeroLu/awesome-minimax-h3?utm_source=awesome_minimax_h3_issue&utm_medium=github_issue

欢迎 Star、收藏，也欢迎提交你看到的高质量 MiniMax H3 案例。
