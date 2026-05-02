# Pricing & quotas

| Plan | Price | API calls / month | Concurrency | Watermark | Notes |
|---|---|---|---|---|---|
| Free trial | $0 | 3 / day per IP | 1 | yes | No signup needed |
| Starter | $19 | 50 | 2 | no | Auto Short + YT Studio |
| Creator | $49 | 200 | 4 | no | + Clip Generator + AI Shorts + Voice Clone |
| Pro | $99 | 600 | 8 | no | + Auto-publish + API tokens (3) |
| Empire | $249 | 2000 | 20 | no | + Unlimited tokens, batch, priority |

Buy at: <https://cart.melyx.id/pay/idea2viral-starter> (or `-creator`, `-pro`, `-empire`).

Cancel anytime — tier reverts to Free at next renewal date.

## Credit-based vs call-based

Currently the API counts each successful call as 1 unit against your monthly quota. Render-heavy endpoints (`/auto-short`, `/clip-generator/render`, `/ai-short`) may also consume credits from your dashboard balance — see your `/dashboard` for live balance.

## SLAs

- 99.5% uptime monthly
- p95 latency <200ms for non-rendering endpoints
- Render jobs (auto-short / clip-render / ai-short) target <90s but can take up to 5min for long videos

For Empire tier, contact `support@idea2viral.com` for custom SLA + dedicated rate limits.
