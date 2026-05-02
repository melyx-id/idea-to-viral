# Idea-to-Viral

> Turn any idea into a viral short-form video — script, voice, visuals, captions, publish.

[![Built with Claude](https://img.shields.io/badge/Built%20with-Claude-7c3aed?logo=anthropic)](https://www.anthropic.com/claude)
[![API Status](https://img.shields.io/badge/API-live-success)](https://cp.idea2viral.com)
[![Free trial](https://img.shields.io/badge/Free%20trial-3%20calls%2Fday-22c55e)](https://cp.idea2viral.com/signup)

**Idea-to-Viral** is a hosted AI platform that automates the entire short-form video pipeline:
**topic → script → voice clone → visuals → captions → 9:16 render → multi-platform publish**.

This repo contains the **public API documentation, SDK examples, and demo notebooks**. The full SaaS engine (rendering, voice cloning, viral-moment detection, multi-tenant orchestration) is closed-source and runs at [cp.idea2viral.com](https://cp.idea2viral.com).

---

## ✨ What you can build with the API

| Use case | Endpoint family | Tier |
|---|---|---|
| Long YouTube → 3-15 viral 9:16 shorts | `/v1/clip-generator/*` | Creator+ |
| Topic → finished narrated short | `/v1/auto-short` | Starter+ |
| URL/landing page → UGC actor video | `/v1/ai-short` | Creator+ |
| 10 viral title variants + thumbnail | `/v1/youtube-studio/*` | Starter+ |
| Voice clone from 30s sample | `/v1/voice-clone` | Creator+ |
| Auto-publish to TikTok/YT/Reels | `/v1/publish/*` | Pro+ |

**Free tier** = 3 calls/day on demo endpoints (watermarked output). Paid plans unlock full quota + watermark removal.

---

## 🚀 Quick start

```bash
curl -X POST https://cp.idea2viral.com/api/v1/auto-short \
  -H "Authorization: Bearer iv_live_YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "5 feng shui mistakes that drain your wealth",
    "language": "en",
    "duration_sec": 30,
    "tone": "viral"
  }'
```

Response:

```json
{
  "ok": true,
  "project_id": 42,
  "video_url": "https://cp.idea2viral.com/storage/renders/...mp4",
  "duration_sec": 30,
  "credits_used": 8
}
```

Get your API token at [cp.idea2viral.com/api-keys](https://cp.idea2viral.com/api-keys) (Pro+ tier).

---

## 📦 SDKs

- **Python** — see [`examples/python/`](examples/python/)
- **Node.js** — see [`examples/node/`](examples/node/)
- **cURL** — see [`examples/curl/`](examples/curl/)
- **n8n workflow** — see [`examples/n8n-workflow.json`](examples/n8n-workflow.json)

---

## 🎬 Demo

Try it without signup at [Hugging Face Space →](https://huggingface.co/spaces/idea2viral/idea-to-viral) (rate-limited, watermarked).

![demo](assets/demo.gif)

---

## 📚 Docs

- [API Reference](docs/api.md)
- [Pricing & quotas](docs/pricing.md)
- [Authentication](docs/auth.md)
- [Webhook events](docs/webhooks.md)

---

## 💼 Pricing

| Plan | Monthly | API calls | Voice clones | Watermark |
|---|---|---|---|---|
| Free trial | $0 | 3/day | — | yes |
| Starter | $19 | 50/mo | 1 | none |
| Creator | $49 | 200/mo | 5 | none |
| Pro | $99 | 600/mo | unlimited | none |
| Empire | $249 | 2000/mo | unlimited | none |

[Upgrade →](https://cart.melyx.id/pay/idea2viral-creator)

---

## 🔐 License

This repository (docs, examples, SDK stubs) is licensed under [MIT](LICENSE).
The hosted API service is proprietary; usage is subject to [Terms of Service](https://cp.idea2viral.com/terms).

---

## 🛠 Built with

- **Backend**: PHP 8.4 + MySQL (workspace-isolated multi-tenant)
- **AI orchestration**: OpenAI GPT-4o, Google Gemini Flash, fal.ai (Flux/Kling/Hailuo/SadTalker), ElevenLabs, faster-whisper
- **Video pipeline**: FFmpeg, PySceneDetect, yt-dlp
- **Developed with**: [Anthropic Claude](https://www.anthropic.com/claude) AI assistance throughout

---

## 📬 Support

- Issues / questions: [open an issue](https://github.com/idea2viral/idea-to-viral/issues)
- Email: support@idea2viral.com
- Discord: [join](https://discord.gg/idea2viral)
