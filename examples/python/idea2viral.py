"""
Idea2Viral Python SDK — minimal client for the public + authenticated REST API.

Free tier: no API key needed. 3 calls/day per IP, watermarked / truncated.
Paid tier: pass `api_key=` (Pro+ only — generate at cp.idea2viral.com/api-keys).

Usage:
    from idea2viral import Idea2Viral

    iv = Idea2Viral()
    print(iv.title_suggest("5 feng shui mistakes that drain your wealth"))

    paid = Idea2Viral(api_key="iv_live_...")
    job = paid.auto_short(topic="...", language="en", duration_sec=30)
"""
from __future__ import annotations
import json
import urllib.request
import urllib.error
from typing import Optional, Any

BASE_URL = "https://cp.idea2viral.com/api/v1"


class Idea2ViralError(Exception):
    pass


class Idea2Viral:
    def __init__(self, api_key: Optional[str] = None, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    # ─── Free demo endpoints ───────────────────────────────────
    def title_suggest(self, topic: str) -> dict:
        return self._post("/public/title-suggest", {"topic": topic}, auth=False)

    def script_preview(self, topic: str, language: str = "en", tone: str = "viral") -> dict:
        return self._post("/public/script-preview",
                          {"topic": topic, "language": language, "tone": tone},
                          auth=False)

    def clip_suggest(self, youtube_url: str) -> dict:
        return self._post("/public/clip-suggest", {"youtube_url": youtube_url}, auth=False)

    # ─── Paid endpoints (require api_key) ─────────────────────
    def auto_short(self, topic: str, language: str = "en", tone: str = "viral",
                   duration_sec: int = 30, voice_profile_id: Optional[int] = None) -> dict:
        return self._post("/auto-short", {
            "topic": topic, "language": language, "tone": tone,
            "duration_sec": duration_sec, "voice_profile_id": voice_profile_id,
        })

    def yt_titles(self, topic: str, context: str = "", refine: str = "") -> dict:
        return self._post("/youtube-studio/titles", {
            "topic": topic, "context": context, "refine": refine,
        })

    def yt_description(self, topic: str, picked_title: str = "") -> dict:
        return self._post("/youtube-studio/description", {
            "topic": topic, "picked_title": picked_title,
        })

    def yt_thumbnail(self, prompt: str) -> dict:
        return self._post("/youtube-studio/thumbnail", {"prompt": prompt})

    def clip_analyze(self, input_url: str, max_clips: int = 8) -> dict:
        return self._post("/clip-generator/analyze",
                          {"input_url": input_url, "max_clips": max_clips})

    def clip_render(self, video_path: str, start: float, end: float,
                    hook: str = "", mode: str = "blur_bg") -> dict:
        return self._post("/clip-generator/render", {
            "video_path": video_path, "start": start, "end": end,
            "hook": hook, "mode": mode,
        })

    def ai_short(self, source_url: str = "", source_text: str = "",
                 avatar_id: int = 0, voice: str = "", language: str = "en",
                 tone: str = "viral") -> dict:
        return self._post("/ai-short", {
            "source_url": source_url, "source_text": source_text,
            "avatar_id": avatar_id, "voice": voice,
            "language": language, "tone": tone,
        })

    def publish_youtube(self, project_id: int, kind: str = "short",
                        privacy: str = "unlisted", override_title: str = "",
                        override_description: str = "") -> dict:
        return self._post("/publish/youtube", {
            "project_id": project_id, "kind": kind, "privacy": privacy,
            "override_title": override_title, "override_description": override_description,
        })

    def get_job(self, job_id: int) -> dict:
        return self._get(f"/jobs/{job_id}")

    # ─── HTTP helpers ─────────────────────────────────────────
    def _headers(self, auth: bool) -> dict:
        h = {"Content-Type": "application/json", "Accept": "application/json",
             "User-Agent": "idea2viral-python/0.1"}
        if auth:
            if not self.api_key:
                raise Idea2ViralError("api_key required for this endpoint — get one at cp.idea2viral.com/api-keys")
            h["Authorization"] = f"Bearer {self.api_key}"
        return h

    def _post(self, path: str, body: Any, auth: bool = True) -> dict:
        req = urllib.request.Request(self.base_url + path,
                                     data=json.dumps(body).encode("utf-8"),
                                     headers=self._headers(auth),
                                     method="POST")
        return self._send(req)

    def _get(self, path: str) -> dict:
        req = urllib.request.Request(self.base_url + path,
                                     headers=self._headers(auth=True),
                                     method="GET")
        return self._send(req)

    @staticmethod
    def _send(req) -> dict:
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                detail = json.loads(e.read().decode("utf-8"))
            except Exception:
                detail = {"error": str(e)}
            raise Idea2ViralError(f"HTTP {e.code}: {detail}") from e


if __name__ == "__main__":
    iv = Idea2Viral()
    res = iv.title_suggest("5 feng shui mistakes that drain your wealth")
    print(json.dumps(res, indent=2, ensure_ascii=False))
