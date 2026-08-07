# ip_illustration_for_yourself

一个同时适配 **Codex / 其他 Agent / 小红书 RedSkill / GPT Image 2 API fallback** 的 IP 小插画 Skill。

只有一个包：`ip_illustration_for_yourself.zip`。

包里同时包含：
- `SKILL.md`：主 Skill
- `references/`：已认可的本地参考图，供 Codex / 可读包内文件的 Agent 使用
- `REFERENCE_URLS.md`：RedSkill / 文本型 Agent 的远程参考 URL 映射
- `examples/api_fallback/`：没有直接生图能力时的 GPT Image 2 API 示例
- `tools/`：把公开 BASE URL 写入 Skill 的辅助脚本

## 目标画风

北极星：**稚拙、mini、留白多、豆豆眼可爱、粗糙钢笔外描边、轮廓略断续、色块干净、和文章强相关。**

尤其注意：**描边粗糙是硬性标准。**

如果生成结果的外轮廓：
- 太丝滑
- 太连续
- 太像矢量线
- 太专业、太干净

就应判定为 off-style 并重画。

正确的粗糙感应该来自：
- 轻微手抖
- 不均匀曲线
- micro-hesitations
- short broken segments
- tiny contour gaps
- imperfect joins

但色块要相对干净；不要靠蜡笔、油画棒、彩铅斑驳感制造“粗糙”。

## 运行模式

### A. Codex / Agent 能读包内图片 + 有 gpt-image-2
直接使用 `references/` 里的多张风格锁定图 + 用户上传的角色参考图生成。

### B. RedSkill / Agent 不能随 Skill 上传图片
使用 `REFERENCE_URLS.md` 里的公开图片链接。

RedSkill 本身不一定能读取 zip 内的图片，所以发布到 RedSkill 前，需要把 `references/` 放到 GitHub / CDN / OSS 等公开地址，然后把 `YOUR_PUBLIC_BASE_URL` 换成公开根地址。

包里的工具：

```bash
python tools/build_skill_with_urls.py --base-url "https://你的公开地址/ip_illustration_for_yourself"
```

会生成可发布的 URL 版本。

### C. Agent 没有 gpt-image-2 / 没有生图能力
不要假装出图。输出：
- 最终 prompt
- 推荐参考图 URL / 文件列表
- GPT Image 2 API 指引
- 可直接复制的 curl 示例

OpenAI 当前官方说明：
- Image generation guide: https://developers.openai.com/api/docs/guides/image-generation
- GPT Image 2 model: https://developers.openai.com/api/docs/models/gpt-image-2

官方文档确认 `gpt-image-2` 可用于 Image API 的 `/v1/images/generations` 和 `/v1/images/edits`；多张参考图可通过 edits 请求的多个 `image[]` 输入使用。

## 参考图策略

不要只靠一张图锁风格。

推荐每次至少：
- 2 张核心 style lock
- 1–3 张 catgirl 已认可风格参考
- 用户自己的角色参考
- 如文章涉及具体对象，可再加入 logo / 产品 / UI / 地点 / 包装 / 课程页等参考

用户可以在**第一次使用**或**任何后续提示**里继续补充新的参考图或公开图片链接。

## 文章配图

默认生成 5 张，除非用户指定数量。

图片必须对应文章里的真实信息、场景、比喻、结构或情绪变化，不要生成泛化的“可爱 AI 插图”。

默认不加文字，除非用户明确要求。

## 路径兼容

包内路径全部使用 `/`，不使用 Windows 的 `\\`。

这样可以避免 macOS / Linux 解压时漏文件或路径异常。

## RedSkill 的公开图片 URL

这个包已经把“本地参考资产”和“远程 URL 模式”合并在一起，但**公开 URL 本身必须由一个可公开访问的图床/GitHub/CDN 提供**。ChatGPT 沙盒文件地址不是公网地址，不能直接当 RedSkill 的参考图 URL。

如果有 GitHub / OSS / CDN，把整个 `references/` 目录原样上传即可，再用工具一次性替换 BASE URL。
