#!/usr/bin/env bash
set -euo pipefail

: "${OPENAI_API_KEY:?Please export OPENAI_API_KEY first}"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 'PROMPT' https://.../ref1.png [https://.../ref2.png ...]"
  exit 1
fi

PROMPT="$1"; shift
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
FILES=()
i=0
for url in "$@"; do
  i=$((i+1))
  f="$TMP/ref_$i"
  curl -LfsS "$url" -o "$f"
  FILES+=("$f")
done

ARGS=()
for f in "${FILES[@]}"; do
  ARGS+=( -F "image[]=@$f" )
done

curl -sS -X POST "https://api.openai.com/v1/images/edits" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "model=gpt-image-2" \
  "${ARGS[@]}" \
  -F "prompt=$PROMPT" \
  | jq -r '.data[0].b64_json' | base64 --decode > output.png

echo "Saved output.png"
