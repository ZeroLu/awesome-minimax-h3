# 外网热传！AI 视频提示词库 Awesome MiniMax H3 来袭，手把手拆解 H3 生成案例！（附 GIF 与中文对照）

![Awesome MiniMax H3](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260813/awesome-minimax-h3-cover.png)

## 【内容摘要】

这篇文章整理了一个开源提示词仓库 **Awesome MiniMax H3**，专门收集 MiniMax H3 / Hailuo AI 在 X 上流传的高质量视频案例，并把视频、原始提示词、中文对照与可复用写法整理在一起。

如果你也遇到过这种情况：别人随手一条提示词就能生成电影感镜头、真实街拍、情景喜剧和节拍卡点短片，而你生成出来总是动作断、镜头乱、角色漂，那么问题很可能不只是模型，而是提示词没有把“时间、镜头、动作、物理关系和声音节奏”写清楚。

我把这些案例做成了仓库：

👉 **GitHub：** https://github.com/ZeroLu/awesome-minimax-h3?utm_source=awesome_minimax_h3_issue&utm_medium=github_issue

下面直接拆案例。

---

## 一、Sitcom / 情景喜剧：把对白、停顿和表情写进提示词

![AI Cannot Replace Joey](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-08.gif)

**完整中文提示词：**

```text
Joey 和 Chandler 并排坐在沙发上，手里拿着咖啡杯。Joey 转向 Chandler，脸上带着完全真诚、十分担忧的表情。

对白：

JOEY：“人工智能会取代我们吗？”

Chandler 慢慢从咖啡杯上抬起头。停顿。直视 Joey。

CHANDLER：“Joey，人工智能取代不了你。没有任何东西能取代你。”

Joey 缓慢地点头，明显松了一口气，开始消化这句话。

JOEY：“因为我太厉害了？”

Chandler 盯着他。长时间停顿。他低头看了一眼咖啡，然后再次抬头。

CHANDLER：“……当然。我们就这么说吧。”

风格：温暖的 90 年代情景喜剧美学，稳定的手持镜头感，自然的表演，角色穿着休闲服装。Joey 必须完全认真地说出每一句话，不带任何讽刺意味。Chandler 用疲惫、冷淡的死板讽刺语气完成所有台词。最后一句说完后，在 Chandler 的脸上保持完整一拍，再切镜头。
```

这个案例是经典情景喜剧式对白，也是 Sitcom 类提示词最值得放在第一位的例子。很多人做 AI 对话视频只写台词，忽略了喜剧真正依赖的 **停顿、视线、反应和最后一拍**。

---

## 二、Comic / 喜剧花絮：用“假花絮”制造喜剧节奏

![The Office Kim Jong Un Blooper](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-05.gif)

**完整中文提示词：**

```text
（花絮镜头）：《办公室》与金正恩。场景：入口处。

0:00–0:04 —— Dunder Mifflin 入口处的中景。Michael Scott 带着巨大的兴奋笑容打开门，金正恩走进来。Michael 立刻用顽皮、幼稚的童谣式声音唱歌，同时指着他：“金正恩，金正恩……太阳底下最酷的人！”他的双手配合节奏做出小幅舞蹈动作。

0:04–0:07 —— Michael 继续唱歌，并按照节奏对金正恩的腹部做轻柔、友好的拳击动作：“金正恩，金正恩……别难过，开心玩一玩！”

0:07–0:10 —— 金正恩努力保持严肃，嘴唇紧紧抿住，但肩膀开始颤抖。他终于忍不住，突然大笑起来。

0:10–0:13 —— Michael 停在出拳到一半的动作上，看着正在大笑的金正恩，自己也立刻笑场。

0:13–0:15 —— 两个人都笑得很厉害。Michael 一边举着拳头，一边几乎站不稳。视频结束在两人彻底破坏角色、放声大笑的瞬间。
```

这个案例的关键词是 `Blooper take`，也就是“花絮片段”。提示词把 15 秒拆成“先表演、再憋笑、最后连续笑场”的喜剧链路。不要只写“搞笑”，要写出 **谁先绷不住、谁接着破功、镜头停在哪个表情上**。

---

## 三、儿童教育：把“字母教学”写成完整时间轴

![ABC Learning Explainer](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-01.gif)

**完整中文提示词：**

```text
制作一个 15 秒的动画教育视频，教幼儿认识字母 A、B、C、D。

每个字母都必须遵循以下学习流程：

字母 → 发音 → 物体 → 有趣动作 → 物体名称

目标受众：3 至 6 岁儿童。

视觉风格：
使用可爱的圆润 3D 角色、柔和的粉彩色、温和的面部表情和简单易识别的物体。结合高级极简科技美学：干净的留白、优雅的构图、柔和的摄影棚灯光、细微反射、平滑渐变、圆润几何形状、清晰字体和极其精致的转场。

动画应该充满趣味、适合儿童，同时保持平静、整洁且设计感十足。

使用干净的米白色背景，每个字母后方使用不同的柔和色彩光晕。

0:00–0:01｜开场
一个微笑的小星星吉祥物弹跳到画面中央。

彩色字母短暂地漂浮在它周围。

显示文字：“Let’s learn!”

吉祥物点击屏幕，产生柔和的涟漪，并揭示第一个字母。

0:01–0:04｜A is for Apple
显示一个大写“A”和旁边较小的小写“a”。使用粗、圆润且高度易读的字体。

旁白说：“A。A 发 ah 的音。A is for Apple。”

大写 A 轻轻膨胀并变成一个闪亮的红苹果。A 的顶端变成苹果梗，一片小绿叶从侧面展开。苹果长出可爱的笑脸，并轻柔地弹跳一次。

显示单词：“APPLE”

将首字母 A 高亮为红色。加入柔和的弹出音效和细小的嘎吱声。

0:04–0:07｜B is for Ball
苹果滚过屏幕，身后留下一条弯曲的红色轨迹。

轨迹绕两圈，形成一个大写“B”，旁边出现小写“b”。

旁白说：“B。B 发 buh 的音。B is for Ball。”

B 的两个圆弧膨胀并合并成一个彩色条纹球。球以有趣的挤压与拉伸动画弹跳两次。

显示单词：“BALL”

将首字母 B 高亮为蓝色。每次弹跳都与柔和的音乐音符同步。

0:07–0:10｜C is for Cat
球在最后一次弹跳时拉伸成弯曲形状，变成一个大写“C”。

小写“c”轻轻滑到旁边。

旁白说：“C。C 发 kuh 的音。C is for Cat。”

C 旋转并变成一只可爱橙色猫咪卷曲的尾巴。猫咪的身体由柔和的圆润形状组成。

猫咪伸展身体、眨眼，并用爪子轻轻挥手一次。

显示单词：“CAT”

将首字母 C 高亮为橙色。加入安静、友好的“喵”声。

0:10–0:13｜D is for Duck
猫咪的尾巴展开并变成大写“D”弯曲的一侧。小写“d”弹到旁边。

旁白说：“D。D 发 duh 的音。D is for Duck。”

D 的直线变成鸭子的脖子，弯曲部分变成圆润的黄色身体。一个小橙色鸭嘴和两只小翅膀弹出。

鸭子向前摇摆、拍动翅膀，并发出欢快的嘎嘎声。

显示单词：“DUCK”

将首字母 D 高亮为黄色。在鸭子的脚下加入细小的水面涟漪。

0:13–0:15｜复习
苹果、球、猫和鸭子滑入四个整洁的圆角卡片。

在它们上方放置字母：“A  B  C  D”

吉祥物回来，依次指向每个物体，让它们按顺序弹跳一次。

旁白说：“A、B、C、D。做得好！”

最后显示文字：“Great job!”

加入小型闪光动画和温暖的音乐铃声。

动画要求：
让每个字母在变形前完整、清晰地出现一小段时间。清楚展示大写和小写版本。确保每个物体都能立即被识别。使用平滑的形状变形，让孩子能直观看懂字母如何变成物体。

保持拼写稳定、字形干净、物体形状准确和角色设计一致。使用柔和的挤压与拉伸、轻微运动模糊、细微阴影、精致灯光以及与音效精准同步的动作。

避免快速摄影机运动、杂乱背景、刺眼颜色、过小文字、变形字母、随机符号、重复物体、恐怖表情或过于复杂的变形。

最终视频应该可爱、有教育意义、令人记忆深刻、平静，并且具有极高的完成度。
```

这个案例不是简单写“做一个 ABC 教学动画”，而是把每个字母的学习路径、旁白、变形动作、音效和复习环节全部写成时间轴。教育类视频不要只写主题，要写清楚学习路径。

---

## 四、街头纪实：让模型处理“相机互动”和真实小动作

![Street Photographer Candid Moment](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-02.gif)

**完整中文提示词：**

```text
一位年轻的西方女性街头摄影师走过热闹的市中心街道，注意到一位坐在咖啡馆外的老人和他的小狗。她通过相机认真构图，捕捉这个自然发生的瞬间，然后把相机转向观众，骄傲地展示她刚刚拍下的照片。她微笑着说：“Look at that。”随后继续在城市中行走。

画面要极度写实，采用自然的手持纪录片式运动、真实的相机互动、自然可信的面部表情、准确的手部动作、真实的狗狗行为、自然日光、电影级景深、持续一致的角色形象、沉浸式城市环境声，以及高级纪录片质感。
```

这个案例说明 MiniMax H3 很吃“可表演动作”。要把人物先看见什么、怎么拿相机、怎么展示结果、说什么话写出来，而不是只写“街头摄影师拍照”。

---

## 五、电影动作：用“一镜到底”控制高速追逐

![Speeder Chase Across a Cliff City](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-03.gif)

**完整中文提示词：**

```text
悬崖城市中的飞车追逐，单个连续镜头。

摄影机从一座由石头雕刻而成的宏伟悬崖城市俯冲而下，朝着一道沿狭窄悬崖道路疾驰的微小光线冲去。

锁定目标：一辆紧贴墙壁、以疯狂速度飞驰的飞行车。

摄影机像弹弓一样冲到飞行车前方，随后猛地甩回，再贴近后方推进器：画面中出现热浪、被甩起的砂砾和不断闪烁的警示灯。

一座正在坍塌的阳台洒下大量碎片；骑手在拱门坠落前一英寸的位置猛打方向，随后沿着一条流畅的运动线路穿过悬挂的晾衣绳和敞开的窗户。

摄影机穿过同样的开口，始终紧贴飞行车的运动轨迹。最后一个弯道之后，画面突然平静下来：摄影机向外冲出，揭示这座城市正打开一片由瀑布供水的无边山谷，水雾变成彩虹。

@Hailuo_AI  #MiniMaxH3
```

动作片提示词的关键不是形容词堆叠，而是 **空间路径**。把镜头怎么追、怎么穿、怎么转、最后怎么揭示大场景写清楚，模型才更容易生成连续的电影镜头。

---

## 六、音乐卡点：用结构化约束做 30 个镜头

![Beat-Synced Character Showcase](https://static.nanobananaproprompts.com/article_upload/awesome-minimax-h3_20260812/x-mm-h3-07.gif)

**完整中文提示词：**

```text
使用 @[char ref] 作为严格的角色参考，使用 @[audio ref] 作为节奏、律动和剪辑参考。

始终保持角色准确的身份、比例、发型、服装、颜色和整体风格一致。

制作一个 15 秒的电影感 burst-cut 快切视频，在 5 个自然适合该角色设计、气质和世界观的不同环境中展示这个角色。

AUDIO SYNC｜音频同步
让整个剪辑与 @[audio ref] 同步。剪切、摄影机动作强调、转场和环境切换必须精准落在强拍、半拍和音乐重音上。让 audio1 控制蒙太奇的节奏和强度。

STRUCTURE｜结构
- 总共 5 个环境
- 每个环境 3 秒
- 每个环境 6 个 burst-cut 快切镜头
- 总共 30 个镜头

每个环境在氛围、灯光、尺度和视觉语言上都必须明显不同。

通过快速的电影化角度展示每个环境：大远景建立镜头、航拍、低角度、侧面视角、跟拍、环境细节特写、中景和英雄镜头。

每次切镜都必须展示新的角度、距离、构图或空间关系。避免重复构图。混合使用静态镜头、推进、拉远、跟踪、环绕和类似升降机的运动。

让角色的动作保持细微且自然。重点放在环境变化、电影化构图以及与 audio1 的紧密同步上。

硬性约束：
- 必须正好有 5 个环境
- 每个环境必须正好有 6 个镜头
- 总共必须正好有 30 个镜头
- 环境变化必须遵循 audio1 的音乐乐句
- 剪切和运动强调必须与 audio1 同步
- 不得更换服装
- 不得出现角色复制
- 不得发生变形
- 不得出现文字或 UI
- 不得出现模糊、无法辨认的画面
- 必须保持严格的角色一致性
```

这个案例很适合做角色展示、游戏角色宣传片和 IP 短视频。卡点视频不要只写“跟着音乐剪”，要写清镜头数量、环境数量、每段时长和切点规则。

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
