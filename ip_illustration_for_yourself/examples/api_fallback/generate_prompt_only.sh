#!/usr/bin/env bash
set -euo pipefail

: "${OPENAI_API_KEY:?Please export OPENAI_API_KEY first}"

PROMPT=${1:-'EXTREMELY cute mini pen-doodle illustration, tiny chibi subject on a large pure-white page, naive dot-eye face, rough black ink contour with visible natural wobble, uneven stroke character, micro-hesitations, short broken contour segments and tiny gaps, simple clean flat color fills, sparse article-relevant micro-scene. No text.'}

curl -sS -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg p "$PROMPT" '{model:"gpt-image-2",prompt:$p,size:"1024x1024",background:"opaque"}')" \
  | jq -r '.data[0].b64_json' | base64 --decode > output.png

echo "Saved output.png"
