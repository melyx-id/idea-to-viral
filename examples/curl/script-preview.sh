#!/bin/bash
# Free demo — returns first 30% of an AI-generated short script.
# Paid (Starter+) returns full script + voice + 9:16 render.

curl -X POST https://cp.idea2viral.com/api/v1/public/script-preview \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "How to start a side hustle",
    "language": "en",
    "tone": "viral"
  }'
