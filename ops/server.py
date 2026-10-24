"""Local control desk. It records status. It does not create YouTube channels."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from ops.catalog import CHANNELS, COMPETITORS, DNA, EVIDENCE, EXCLUDED, channel_by_id, summary
from ops.qc import inspect_script
from ops.videos import VIDEOS, videos_for

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8080


def _package(channel: dict) -> dict:
    videos = []
    for video in videos_for(channel["id"]):
        script_path = ROOT / video["script"]
        report = None
        if script_path.exists():
            report = inspect_script(
                script_path.read_text(encoding="utf-8"),
                title=video["title"],
                master_path=None,
                thumbnail_path=None,
            )
        videos.append({**video, "qc": report})
    return {
        **channel,
        "evidence": [EVIDENCE[key] for key in channel["evidence_ids"]],
        "competitors": [COMPETITORS[key] for key in channel["competitor_ids"]],
        "dna": DNA[channel["dna_key"]],
        "videos": videos,
        "pipeline": _pipeline(videos),
        "next_action": _next_action(channel, videos),
    }


def _pipeline(videos: list[dict]) -> dict:
    return {
        "research": 0 if videos else 1,
        "script_ready": sum(1 for video in videos if video["state"] == "script_ready"),
        "production": 0,
        "completed": 0,
        "scheduled": 0,
        "published": 0,
        "qc_failures": sum(1 for video in videos if video.get("qc") and not video["qc"]["passed"]),
    }


def _next_action(channel: dict, videos: list[dict]) -> str:
    if not channel["launch"]:
        return "Stay in research. Bulk channel creation needs the owner's authorization and a connected YouTube account."
    if not videos:
        return "Write the first original script."
    if videos[0].get("qc") and not videos[0]["qc"]["passed"]:
        return "Quality control is open. Record original narration and picture before any upload."
    return "Connect the owner's YouTube channel, then schedule."


def desk_snapshot() -> dict:
    rows = [_package(channel) for channel in CHANNELS]
    pipe = {
        "research": sum(row["pipeline"]["research"] for row in rows),
        "script_ready": sum(row["pipeline"]["script_ready"] for row in rows),
        "production": 0,
        "completed": 0,
        "scheduled": 0,
        "published": 0,
        "qc_failures": sum(row["pipeline"]["qc_failures"] for row in rows),
    }
    return {
        "summary": {**summary(), "pipeline": pipe},
        "channels": rows,
        "excluded": EXCLUDED,
    }


def schedule_blockers(channel_id: str) -> list[str]:
    channel = channel_by_id(channel_id)
    blockers = []
    if channel is None:
        return ["Unknown channel."]
    if not channel["youtube_created"]:
        blockers.append("No YouTube channel exists for this brand. Creation needs the owner's Google account.")
    blockers.append("Owner authorization for bulk creation has not been recorded.")
    videos = videos_for(channel_id)
    if not videos:
        blockers.append("There is no script package to schedule.")
        return blockers
    script_path = ROOT / videos[0]["script"]
    report = inspect_script(
        script_path.read_text(encoding="utf-8"),
        title=videos[0]["title"],
        master_path=None,
        thumbnail_path=None,
    )
    if not report["passed"]:
        blockers.append("Quality control failed: " + ", ".join(report["failed"]) + ".")
    return blockers


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Channel Desk</title>
<style>
  :root { color-scheme: light; --ink:#1c1915; --muted:#5c564c; --line:#e4ddd2; --paper:#f7f4ee; --card:#fff; --accent:#8a3d12; }
  * { box-sizing: border-box; }
  body { margin:0; font:16px/1.45 Georgia, "Iowan Old Style", serif; color:var(--ink); background:var(--paper); }
  header { padding:28px 32px 12px; max-width:1180px; margin:0 auto; }
  h1 { font-size:28px; font-weight:600; margin:0 0 6px; }
  h2 { font-size:20px; margin:0 0 8px; }
  p, li { color:var(--ink); }
  .muted { color:var(--muted); }
  main { max-width:1180px; margin:0 auto; padding:0 32px 48px; display:grid; grid-template-columns: 1.1fr 0.9fr; gap:24px; }
  .stats { display:flex; gap:18px; flex-wrap:wrap; margin:16px 0; }
  .stat b { display:block; font-size:22px; font-variant-numeric:tabular-nums; }
  .stat span { color:var(--muted); font-size:13px; }
  button, select { font:14px/1.2 inherit; background:var(--card); border:1px solid var(--line); padding:6px 10px; }
  button { cursor:pointer; }
  button.active { border-color:var(--accent); color:var(--accent); }
  table { width:100%; border-collapse:collapse; background:var(--card); }
  th, td { text-align:left; padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top; font-size:14px; }
  th { font-weight:600; }
  tr { cursor:pointer; }
  tr.selected { background:#f3ebe3; }
  #detail { background:var(--card); border:1px solid var(--line); padding:16px 18px; position:sticky; top:12px; max-height:calc(100vh - 24px); overflow:auto; }
  .fail { color:#8a1f12; }
  .ok { color:#1d5c32; }
  pre { white-space:pre-wrap; font:13px/1.4 ui-monospace, monospace; background:#f3efe8; padding:10px; }
  @media (max-width:900px) { main { grid-template-columns:1fr; } #detail { position:static; max-height:none; } }
</style>
</head>
<body>
<header>
  <h1>Channel Desk</h1>
  <p class="muted" id="lead">Loading the 24 October 2026 research snapshot.</p>
  <div class="stats" id="stats"></div>
  <p>
    <button type="button" data-market="all" class="active">All markets</button>
    <button type="button" data-market="UK">UK</button>
    <button type="button" data-market="US">US</button>
    <button type="button" data-launch="1">Launch batch</button>
    <label class="muted"> Sort is fixed: desk score, then name.</label>
  </p>
</header>
<main>
  <section>
    <table>
      <thead><tr><th>Rank</th><th>Channel</th><th>Market</th><th>Score</th><th>Niche</th><th>YouTube</th></tr></thead>
      <tbody id="rows"></tbody>
    </table>
  </section>
  <aside id="detail"><p class="muted">Select a channel.</p></aside>
</main>
<script>
const state = { market: "all", launch: false, selected: null, data: null };
async function load() {
  const response = await fetch("/api/snapshot");
  state.data = await response.json();
  const s = state.data.summary;
  document.getElementById("lead").textContent =
    "Public research retrieved " + s.retrieved + ". Scores are a weighted desk reading of that evidence, not YouTube Analytics.";
  document.getElementById("stats").innerHTML = [
    [s.channel_count, "Opportunities ranked"],
    [s.youtube_channels_created, "YouTube channels created"],
    [s.pipeline.published, "Videos published"],
    [s.pipeline.script_ready, "Scripts ready"],
    [s.pipeline.qc_failures, "QC failures"],
    [s.launch_count, "Launch batch"]
  ].map(([v, l]) => `<div class="stat"><b>${v}</b><span>${l}</span></div>`).join("");
  draw();
}
function draw() {
  const body = document.getElementById("rows");
  const channels = state.data.channels.filter(ch => {
    if (state.market !== "all" && ch.market !== state.market) return false;
    if (state.launch && !ch.launch) return false;
    return true;
  });
  body.innerHTML = channels.map(ch => `<tr data-id="${ch.id}" class="${state.selected===ch.id?"selected":""}">
    <td>${ch.rank}</td><td>${ch.name}<br><span class="muted">@${ch.handle}</span></td>
    <td>${ch.market}</td><td>${ch.score}</td><td>${ch.niche}</td>
    <td>${ch.youtube_created ? "Created" : "Not created"}</td></tr>`).join("");
  body.querySelectorAll("tr").forEach(row => row.addEventListener("click", () => openChannel(row.dataset.id)));
}
async function openChannel(id) {
  state.selected = id;
  draw();
  const response = await fetch("/api/channels/" + id);
  const ch = await response.json();
  const video = ch.videos[0];
  const qc = video && video.qc;
  const failed = qc ? qc.failed.map(name => `<li class="fail">${name}: ${qc.checks[name].note}</li>`).join("") : "";
  const comps = ch.competitors.map(c => `<li>${c.name} (${c.subs_label} public subscriber label) — ${c.handle}</li>`).join("") || "<li>No named competitor was captured for this sub-niche.</li>";
  document.getElementById("detail").innerHTML = `
    <h2>${ch.name}</h2>
    <p class="muted">@${ch.handle} · ${ch.market} · score ${ch.score} · rank ${ch.rank}</p>
    <p>${ch.positioning}</p>
    <p><strong>Schedule assumption.</strong> ${ch.publish_days} at ${ch.publish_hour_local} ${ch.timezone}. ${ch.schedule_basis}</p>
    <p><strong>Voice.</strong> ${ch.voice}</p>
    <p><strong>Picture.</strong> ${ch.visual}</p>
    <p><strong>Money note.</strong> ${ch.monetization_note}</p>
    <h2>Competitor DNA</h2>
    <ul>${comps}</ul>
    <p>${ch.dna.observed}</p>
    <p>${ch.dna.principle}</p>
    <p class="muted">${ch.dna.not_observed}</p>
    <h2>Package</h2>
    ${video ? `<p><strong>${video.title}</strong> · ${video.state}</p>
      <p>${video.description.split("\\n")[0]}</p>
      <ul>${failed}</ul>
      <p>Word count ${qc.word_count}. QC ${qc.passed ? "passed" : "has open items"}.</p>
      <button id="schedule" type="button">Attempt to schedule</button>
      <pre id="schedule-result"></pre>` : `<p>No script yet. ${ch.next_action}</p>`}
    <p><strong>Next.</strong> ${ch.next_action}</p>`;
  const button = document.getElementById("schedule");
  if (button) button.addEventListener("click", async () => {
    const result = await fetch("/api/channels/" + id + "/schedule", { method: "POST" });
    const body = await result.json();
    document.getElementById("schedule-result").textContent = JSON.stringify(body, null, 2);
  });
}
document.querySelectorAll("button[data-market]").forEach(button => button.addEventListener("click", () => {
  state.market = button.dataset.market;
  state.launch = false;
  document.querySelectorAll("header button").forEach(item => item.classList.remove("active"));
  button.classList.add("active");
  draw();
}));
document.querySelector("button[data-launch]").addEventListener("click", (event) => {
  state.launch = true;
  state.market = "all";
  document.querySelectorAll("header button").forEach(item => item.classList.remove("active"));
  event.currentTarget.classList.add("active");
  draw();
});
load();
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def _send(self, code: int, payload, content_type: str) -> None:
        body = payload if isinstance(payload, bytes) else json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path == "/":
            self._send(200, PAGE.encode("utf-8"), "text/html; charset=utf-8")
            return
        if path == "/api/health":
            self._send(200, {"ok": True, "service": "channel-desk"}, "application/json")
            return
        if path == "/api/snapshot":
            self._send(200, desk_snapshot(), "application/json")
            return
        if path == "/api/summary":
            snap = desk_snapshot()
            self._send(200, snap["summary"], "application/json")
            return
        if path.startswith("/api/channels/"):
            channel_id = path.removeprefix("/api/channels/")
            channel = channel_by_id(channel_id)
            if channel is None:
                self._send(404, {"error": "not found"}, "application/json")
                return
            self._send(200, _package(channel), "application/json")
            return
        self._send(404, {"error": "not found"}, "application/json")

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path.startswith("/api/channels/") and path.endswith("/schedule"):
            channel_id = path.removeprefix("/api/channels/").removesuffix("/schedule").strip("/")
            blockers = schedule_blockers(channel_id)
            self._send(
                409,
                {"scheduled": False, "youtube_confirmed": False, "blockers": blockers},
                "application/json",
            )
            return
        self._send(404, {"error": "not found"}, "application/json")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=PORT)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Channel Desk listening on http://{args.host}:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
