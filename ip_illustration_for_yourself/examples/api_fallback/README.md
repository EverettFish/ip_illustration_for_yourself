# GPT Image 2 API fallback

官方文档：
- https://developers.openai.com/api/docs/guides/image-generation
- https://developers.openai.com/api/docs/models/gpt-image-2

## 纯 prompt 生成
```bash
export OPENAI_API_KEY="..."
bash generate_prompt_only.sh "你的 prompt"
```

## 本地参考图
GPT Image 2 支持 Image API edits，多个参考图通过多个 `image[]` multipart 字段传入。

```bash
bash edit_with_local_references.sh "你的 prompt" \
  ../../references/style_lock/01_docs_reader_style.png \
  ../../references/style_lock/03_catgirl_anchor.png \
  /path/to/your_character.png
```

## RedSkill 公开 URL 参考图
脚本先下载公开 URL，再提交到 `/v1/images/edits`：

```bash
bash edit_with_public_urls.sh "你的 prompt" \
  "https://cdn.example.com/style1.png" \
  "https://cdn.example.com/style2.png" \
  "https://cdn.example.com/character.png"
```
