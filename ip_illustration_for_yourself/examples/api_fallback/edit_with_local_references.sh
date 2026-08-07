#!/usr/bin/env bash
set -euo pipefail

: "${OPENAI_API_KEY:?Please export OPENAI_API_KEY first}"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 'PROMPT' ref1.png [ref2.png ...]"
  exit 1
fi

PROMPT="$1"; shift
ARGS=()
for f in "$@"; do
  ARGS+=( -F "image[]=@$f" )
done

curl -sS -X POST "https://api.openai.com/v1/images/edits" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "model=gpt-image-2" \
  "${ARGS[@]}" \
  -F "prompt=$PROMPT" \
  | jq -r '.data[0].b64_json' | base64 --decode > output.png

echo "Saved output.png"
