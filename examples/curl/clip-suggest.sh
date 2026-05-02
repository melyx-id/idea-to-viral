#!/bin/bash
# Free demo — returns 1 estimated viral moment for a YouTube URL.
# Paid (Creator+) downloads + transcribes the video and returns 3-15 real
# viral moments with auto-render to 9:16 + burned subtitles.

curl -X POST https://cp.idea2viral.com/api/v1/public/clip-suggest \
  -H "Content-Type: application/json" \
  -d '{
    "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  }'
