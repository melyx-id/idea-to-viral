# Idea2Viral API Reference

> Full reference at https://idea2viral.com/api (tier-gated). This Markdown is a quick overview.

**Base URL:** `https://cp.idea2viral.com/api/v1`

## Authentication

| Endpoint family | Auth |
|---|---|
| `/v1/public/*` | None — IP rate-limited 3/day |
| All others | `Authorization: Bearer iv_live_...` (Pro+ tier required) |

Generate tokens: <https://cp.idea2viral.com/api-keys>

---

## Free demo endpoints

### `POST /v1/public/title-suggest`

```json
// request
{ "topic": "5 feng shui mistakes that drain your wealth" }

// response
{
  "ok": true,
  "titles": [ "...", "...", "..." ],
  "watermark": "Powered by idea2viral.com — upgrade to Starter+ for 10 titles + scoring",
  "calls_remaining_today": 2,
  "upgrade_url": "https://idea2viral.com/api"
}
```

### `POST /v1/public/script-preview`

```json
// request
{ "topic": "How to start a side hustle", "language": "en", "tone": "viral" }

// response
{
  "ok": true,
  "script_preview": "🚀 Want to escape the 9-to-5... [truncated]",
  "preview_pct": 30,
  "watermark": "...",
  "calls_remaining_today": 2
}
```

### `POST /v1/public/clip-suggest`

```json
// request
{ "youtube_url": "https://www.youtube.com/watch?v=..." }

// response
{
  "ok": true,
  "note": "Estimated. Paid Creator+ downloads + transcribes for accurate detection.",
  "suggestion": { "start_sec": 120, "end_sec": 150, "hook": "...", "reason": "..." },
  "watermark": "...",
  "calls_remaining_today": 2
}
```

---

## Paid endpoints (Starter+ / Creator+ / Pro+)

| Endpoint | Tier | Purpose |
|---|---|---|
| `POST /v1/auto-short` | Starter+ | Topic → finished narrated 9:16 short |
| `POST /v1/youtube-studio/titles` | Starter+ | 10 viral titles + score + chat refine |
| `POST /v1/youtube-studio/description` | Starter+ | SEO description + chapter timestamps |
| `POST /v1/youtube-studio/thumbnail` | Starter+ | 16:9 thumbnail via Flux |
| `POST /v1/clip-generator/analyze` | Creator+ | Long video → 3-15 viral moment timestamps |
| `POST /v1/clip-generator/render` | Creator+ | Render specific moment as 9:16 + subs |
| `POST /v1/ai-short` | Creator+ | URL → UGC actor talking-head short |
| `POST /v1/voice-clone` | Creator+ | Clone voice from 30s sample |
| `POST /v1/publish/youtube` | Pro+ | Auto-upload to YouTube |
| `POST /v1/publish/tiktok` | Pro+ | Auto-publish to TikTok |
| `GET /v1/jobs/{id}` | Starter+ | Poll render job status |

Full request / response schemas are documented at <https://idea2viral.com/api> — login + paid tier required to view.

---

## Errors

```json
{
  "ok": false,
  "error": "rate_limit_exceeded",
  "kind": "rate_limit",
  "detail": "3 calls/day from this IP. Reset at 00:00 UTC.",
  "upgrade_url": "https://cart.melyx.id/pay/idea2viral-starter"
}
```

| `kind` | Meaning |
|---|---|
| `auth` | Missing or invalid bearer |
| `credits` | Insufficient credits |
| `rate_limit` | Hit daily/monthly cap |
| `tier_locked` | Plan does not include this endpoint |
| `bad_input` | Malformed request body |
| `llm_failed` | Upstream LLM error (retry safe) |
| `render_failed` | FFmpeg / fal.ai failure |
| `internal` | Unhandled exception (please open an issue) |

---

## Webhooks

Configure at `/webhooks` in the dashboard. Events:

- `project.completed` — render finished
- `publish.posted` — successfully published to platform
- `publish.failed` — publish attempt failed

Payload example:

```json
{
  "event": "project.completed",
  "project_id": 42,
  "video_url": "https://cp.idea2viral.com/storage/renders/...mp4",
  "duration_sec": 30,
  "ts": "2026-05-02T14:30:00Z"
}
```

Webhook signature: `X-Idea2Viral-Signature: <hmac-sha256 of body using webhook secret>`.
