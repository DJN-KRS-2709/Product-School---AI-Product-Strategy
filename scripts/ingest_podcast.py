#!/usr/bin/env python3
"""
Ingest Product School's Product Podcast into local markdown files.

Primary source: BuzzSprout RSS feed (831 episodes, public transcripts with
speaker names, no API key needed).

Usage:
    python ingest_podcast.py                          # full run
    python ingest_podcast.py --limit 5                # test with 5 episodes
    python ingest_podcast.py --output-dir path/to/dir  # custom output
    python ingest_podcast.py --delay 1                 # seconds between fetches
"""

import argparse
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Set

try:
    import requests
except ImportError:
    print("Missing dependency: pip install requests")
    sys.exit(1)

RSS_URL = "https://feeds.buzzsprout.com/90361.rss"
BUZZSPROUT_PODCAST_ID = "90361"
DEFAULT_DELAY = 0.5
NS = {"podcast": "https://podcastindex.org/namespace/1.0"}


class TranscriptHTMLParser(HTMLParser):
    """Parse BuzzSprout transcript HTML into structured text with speaker labels."""

    def __init__(self):
        super().__init__()
        self.segments = []
        self._current_text = ""
        self._in_bold = False
        self._bold_text = ""

    def handle_starttag(self, tag, attrs):
        if tag == "b":
            self._in_bold = True
            self._bold_text = ""

    def handle_endtag(self, tag):
        if tag == "b":
            self._in_bold = False
            if self._bold_text.strip():
                if self._current_text.strip():
                    self.segments.append(self._current_text.strip())
                self._current_text = ""
                self.segments.append(f"\n### {self._bold_text.strip()}\n")
        elif tag == "p":
            if self._current_text.strip():
                self.segments.append(self._current_text.strip())
                self._current_text = ""

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return
        if self._in_bold:
            self._bold_text += text
        else:
            self._current_text += " " + text

    def get_text(self):
        if self._current_text.strip():
            self.segments.append(self._current_text.strip())
        return "\n\n".join(self.segments)


def fetch_rss_episodes(limit: Optional[int] = None) -> List[dict]:
    """Fetch and parse the BuzzSprout RSS feed."""
    print(f"Fetching RSS feed from: {RSS_URL}")
    resp = requests.get(RSS_URL, headers={"User-Agent": "ProductSchoolIngest/1.0"})
    resp.raise_for_status()

    root = ET.fromstring(resp.text)
    channel = root.find("channel")
    items = channel.findall("item")

    episodes = []
    for item in items:
        title = item.find("title")
        pub_date = item.find("pubDate")
        description = item.find("description")
        enclosure = item.find("enclosure")
        duration_el = item.find("{http://www.itunes.com/dtds/podcast-1.0.dtd}duration")
        transcript_el = item.find("podcast:transcript", NS)

        episode_id = ""
        transcript_url = ""
        if transcript_el is not None:
            transcript_url = transcript_el.get("url", "")
            id_match = re.search(r"/(\d+)/transcript", transcript_url)
            if id_match:
                episode_id = id_match.group(1)

        audio_url = enclosure.get("url", "") if enclosure is not None else ""
        if not episode_id and audio_url:
            id_match = re.search(r"/(\d+)-", audio_url)
            if id_match:
                episode_id = id_match.group(1)

        episodes.append({
            "title": title.text if title is not None else "Untitled",
            "pub_date": pub_date.text if pub_date is not None else "",
            "description": (description.text or "")[:500] if description is not None else "",
            "audio_url": audio_url,
            "duration": duration_el.text if duration_el is not None else "",
            "transcript_url": transcript_url,
            "episode_id": episode_id,
        })

    if limit:
        episodes = episodes[:limit]

    print(f"Found {len(episodes)} episodes in RSS feed")
    return episodes


def parse_pub_date(pub_date_str: str) -> str:
    """Parse RSS pubDate into YYYY-MM-DD."""
    try:
        dt = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")
        return dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return datetime.now().strftime("%Y-%m-%d")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def extract_guest_from_title(title: str) -> str:
    """Extract guest name from episode title.

    BuzzSprout titles follow patterns like:
      "Topic | Guest Name | E291"
      "Topic with Guest Name | E290"
    """
    pipe_match = re.match(r"^(.+?)\s*\|\s*(.+?)\s*\|\s*E\d+", title)
    if pipe_match:
        return pipe_match.group(2).strip()

    with_match = re.search(r"\bwith\s+(.+?)(?:\s*\||$)", title, re.IGNORECASE)
    if with_match:
        guest = with_match.group(1).strip()
        guest = re.split(r"\s*\|\s*", guest)[0]
        if len(guest.split()) <= 6:
            return guest

    parts = title.split("|")
    if len(parts) >= 2:
        candidate = parts[-2].strip() if re.match(r"E\d+", parts[-1].strip()) else parts[0].strip()
        if len(candidate.split()) <= 6:
            return candidate

    return ""


def fetch_transcript(transcript_url: str) -> Optional[str]:
    """Fetch and parse an HTML transcript from BuzzSprout."""
    if not transcript_url:
        return None

    try:
        resp = requests.get(transcript_url, headers={"User-Agent": "ProductSchoolIngest/1.0"}, timeout=30)
        if resp.status_code != 200:
            return None
    except requests.RequestException:
        return None

    parser = TranscriptHTMLParser()
    parser.feed(resp.text)
    text = parser.get_text()

    text = re.sub(r"<!--.*?-->", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text if text else None


def write_episode_markdown(output_dir: Path, episode: dict, transcript: str) -> Path:
    """Write a single episode markdown file."""
    title = episode["title"]
    date_str = parse_pub_date(episode["pub_date"])
    guest = extract_guest_from_title(title)
    duration = episode.get("duration", "")
    description = episode.get("description", "")
    episode_id = episode.get("episode_id", "")

    fname = f"{date_str}-{slugify(title)}.md"
    filepath = output_dir / fname

    frontmatter_lines = [
        "---",
        f'title: "{title}"',
    ]
    if guest:
        frontmatter_lines.append(f'guest: "{guest}"')
    frontmatter_lines.extend([
        f'date: "{date_str}"',
        f'source: "buzzsprout"',
        f'episode_id: "{episode_id}"',
    ])
    if duration:
        frontmatter_lines.append(f'duration: "{duration}"')
    if episode.get("audio_url"):
        frontmatter_lines.append(f'audio_url: "{episode["audio_url"]}"')
    frontmatter_lines.append("---")

    body = "\n".join(frontmatter_lines)
    body += f"\n\n# {title}\n\n"
    if description:
        clean_desc = re.sub(r"<[^>]+>", "", description).strip()
        if clean_desc:
            body += f"> {clean_desc[:500]}\n\n"
    body += "## Transcript\n\n"
    body += transcript
    body += "\n"

    filepath.write_text(body, encoding="utf-8")
    return filepath


def build_index(output_dir: Path):
    """Build _index.md from all episode markdown files."""
    episodes = []
    for f in sorted(output_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        content = f.read_text(encoding="utf-8")
        title = ""
        guest = ""
        date = ""
        for line in content.split("\n"):
            if line.startswith('title: "'):
                title = line.split('"')[1]
            elif line.startswith('guest: "'):
                guest = line.split('"')[1]
            elif line.startswith('date: "'):
                date = line.split('"')[1]
            elif line == "---" and title:
                break
        episodes.append({
            "file": f.name,
            "title": title,
            "guest": guest,
            "date": date,
        })

    episodes.sort(key=lambda e: e["date"], reverse=True)

    lines = [
        "# The Product Podcast - Episode Index",
        "",
        f"Total episodes: {len(episodes)}",
        f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| Date | Title | Guest |",
        "|------|-------|-------|",
    ]
    for ep in episodes:
        guest_col = ep["guest"] if ep["guest"] else ""
        title_link = f"[{ep['title']}]({ep['file']})"
        lines.append(f"| {ep['date']} | {title_link} | {guest_col} |")

    lines.append("")
    (output_dir / "_index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Index written with {len(episodes)} episodes")


def existing_episode_ids(output_dir: Path) -> Set[str]:
    """Scan existing markdown files to find already-ingested episode IDs."""
    ids = set()
    for f in output_dir.glob("*.md"):
        if f.name.startswith("_"):
            continue
        content = f.read_text(encoding="utf-8")
        match = re.search(r'episode_id:\s*"([^"]+)"', content)
        if match:
            ids.add(match.group(1))
    return ids


def main():
    parser = argparse.ArgumentParser(description="Ingest Product School podcast from BuzzSprout RSS")
    parser.add_argument(
        "--output-dir",
        default="insights/product-podcast",
        help="Output directory for markdown files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max episodes to process (for testing)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help=f"Seconds between transcript fetches (default: {DEFAULT_DELAY})",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    episodes = fetch_rss_episodes(args.limit)

    already_done = existing_episode_ids(output_dir)
    print(f"Already ingested: {len(already_done)} episodes")

    successes = 0
    failures = 0
    skipped = 0

    for i, episode in enumerate(episodes):
        eid = episode["episode_id"]
        title = episode["title"]

        if eid and eid in already_done:
            skipped += 1
            continue

        print(f"[{i+1}/{len(episodes)}] {title}")

        transcript = fetch_transcript(episode["transcript_url"])
        if transcript is None:
            print(f"  SKIP - no transcript available")
            failures += 1
            continue

        filepath = write_episode_markdown(output_dir, episode, transcript)
        print(f"  OK -> {filepath.name}")
        successes += 1
        time.sleep(args.delay)

    print(f"\nDone: {successes} new, {skipped} skipped, {failures} failed (no transcript)")
    build_index(output_dir)


if __name__ == "__main__":
    main()
