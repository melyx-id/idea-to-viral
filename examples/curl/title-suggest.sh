#!/bin/bash
# Free demo — no auth required, 3 calls/day per IP, returns 3 titles + watermark.
# Paid (Starter+) returns 10 titles with viral score + chat refinement.

curl -X POST https://cp.idea2viral.com/api/v1/public/title-suggest \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "5 feng shui mistakes that drain your wealth"
  }'
