// Idea2Viral Node.js SDK — minimal client (no deps; uses native fetch).
//
// Free tier: no API key needed. 3 calls/day per IP, watermarked / truncated.
// Paid tier: pass apiKey (Pro+ — generate at cp.idea2viral.com/api-keys).
//
// Usage:
//   import { Idea2Viral } from './idea2viral.js';
//   const iv = new Idea2Viral();
//   console.log(await iv.titleSuggest('topic'));

export class Idea2Viral {
  constructor({ apiKey = null, baseUrl = 'https://cp.idea2viral.com/api/v1' } = {}) {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, '');
  }

  // Free demo endpoints
  titleSuggest(topic) { return this._post('/public/title-suggest', { topic }, false); }
  scriptPreview(topic, language = 'en', tone = 'viral') {
    return this._post('/public/script-preview', { topic, language, tone }, false);
  }
  clipSuggest(youtubeUrl) {
    return this._post('/public/clip-suggest', { youtube_url: youtubeUrl }, false);
  }

  // Paid endpoints
  autoShort(opts) { return this._post('/auto-short', opts); }
  ytTitles(opts) { return this._post('/youtube-studio/titles', opts); }
  ytDescription(opts) { return this._post('/youtube-studio/description', opts); }
  ytThumbnail(opts) { return this._post('/youtube-studio/thumbnail', opts); }
  clipAnalyze(opts) { return this._post('/clip-generator/analyze', opts); }
  clipRender(opts) { return this._post('/clip-generator/render', opts); }
  aiShort(opts) { return this._post('/ai-short', opts); }
  publishYoutube(opts) { return this._post('/publish/youtube', opts); }
  getJob(jobId) { return this._get(`/jobs/${jobId}`); }

  // Low-level
  async _post(path, body, auth = true) {
    return this._send(path, { method: 'POST', body: JSON.stringify(body) }, auth);
  }
  async _get(path) { return this._send(path, { method: 'GET' }, true); }

  async _send(path, init, auth) {
    const headers = { 'Content-Type': 'application/json', 'User-Agent': 'idea2viral-node/0.1' };
    if (auth) {
      if (!this.apiKey) throw new Error('apiKey required — get one at cp.idea2viral.com/api-keys');
      headers.Authorization = `Bearer ${this.apiKey}`;
    }
    const r = await fetch(this.baseUrl + path, { ...init, headers });
    const txt = await r.text();
    let data;
    try { data = JSON.parse(txt); }
    catch { throw new Error(`Non-JSON response (${r.status}): ${txt.substring(0, 200)}`); }
    if (!r.ok || data.ok === false) {
      throw new Error(`HTTP ${r.status}: ${data.error || JSON.stringify(data)}`);
    }
    return data;
  }
}

// Demo run
if (import.meta.url === `file://${process.argv[1]}`) {
  const iv = new Idea2Viral();
  console.log(await iv.titleSuggest('5 feng shui mistakes that drain your wealth'));
}
