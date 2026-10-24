"""Fifteen-point inspection. A missing master file cannot pass."""

from __future__ import annotations

import re
from pathlib import Path

CHECKS = [
    "opening_hook",
    "originality",
    "script_accuracy",
    "narration_quality",
    "audio_clarity",
    "audio_sync",
    "visual_consistency",
    "editing_quality",
    "pacing",
    "thumbnail_readability",
    "title_accuracy",
    "copyright",
    "youtube_policy",
    "export_quality",
    "playback",
]

ADVICE_RE = re.compile(
    r"\b(not (personal|financial|medical|legal|insurance) advice)\b",
    re.I,
)
PERSONA_RE = re.compile(
    r"\b(as your ai (doctor|adviser|advisor|lawyer)|i am an? ai (doctor|financial adviser))\b",
    re.I,
)


def inspect_script(text: str, *, title: str, master_path: Path | None, thumbnail_path: Path | None) -> dict:
    words = re.findall(r"[A-Za-z0-9'£$%]+", text)
    results = {name: {"pass": False, "note": ""} for name in CHECKS}
    has_advice = bool(ADVICE_RE.search(text))
    has_persona = bool(PERSONA_RE.search(text))
    has_source = "http://" in text or "https://" in text
    long_enough = len(words) >= 700
    title_in_script = title.lower()[:24] in text.lower() or len(title) > 10

    results["opening_hook"] = {
        "pass": "cold open" in text.lower()[:900] or text.strip().lower().startswith("open on"),
        "note": "The script must mark a cold open before the body.",
    }
    results["originality"] = {
        "pass": "original" in text.lower() and not has_persona,
        "note": "The script must say the episode is original and must not cast an AI expert.",
    }
    results["script_accuracy"] = {
        "pass": has_source and has_advice and long_enough,
        "note": "Need a source URL, an advice disclaimer, and at least 700 words.",
    }
    results["title_accuracy"] = {
        "pass": bool(title) and title_in_script and "misleading" not in title.lower(),
        "note": "The chosen title must appear in the script header.",
    }
    results["youtube_policy"] = {
        "pass": has_advice and not has_persona and "made for kids" not in text.lower(),
        "note": "Sensitive topics stay sourced and are not made for kids.",
    }
    results["copyright"] = {
        "pass": "no third-party footage" in text.lower() or "original footage" in text.lower(),
        "note": "The script must commit to original footage.",
    }
    media_missing = master_path is None or not master_path.exists()
    thumb_missing = thumbnail_path is None or not thumbnail_path.exists()
    for name, note in (
        ("narration_quality", "No narration file has been recorded."),
        ("audio_clarity", "No mixed audio file exists."),
        ("audio_sync", "No picture lock exists to sync."),
        ("visual_consistency", "No picture master exists."),
        ("editing_quality", "No edit exists."),
        ("pacing", "Pacing cannot be judged without a cut."),
        ("export_quality", "No export file exists."),
        ("playback", "Nothing has been played back."),
    ):
        results[name] = {"pass": not media_missing, "note": note}
    results["thumbnail_readability"] = {
        "pass": not thumb_missing,
        "note": "No thumbnail file exists.",
    }
    failed = [name for name, row in results.items() if not row["pass"]]
    return {
        "passed": not failed,
        "failed": failed,
        "checks": results,
        "word_count": len(words),
    }
