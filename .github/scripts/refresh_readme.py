#!/usr/bin/env python3
"""Refresh the <!-- REPOS:START --> … <!-- REPOS:END --> block in README.md.

Fetches public, non-fork repos for the account via the GitHub REST API and
rewrites the marked section.  Exits 0 in all cases; the caller (GitHub
Actions workflow) inspects `git diff` to decide whether to commit.
"""

import json
import os
import re
import sys
import urllib.request

ACCOUNT = "BWBlueVector"  # GitHub account whose repos we list
README_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
START_MARKER = "<!-- REPOS:START -->"
END_MARKER = "<!-- REPOS:END -->"


def fetch_repos(token: str) -> list[dict]:
    """Return public, non-fork repos for ACCOUNT sorted alphabetically by name."""
    url = (
        f"https://api.github.com/users/{ACCOUNT}/repos"
        "?type=public&sort=full_name&per_page=100"
    )
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "refresh-readme-script",
    }
    if token:
        headers["Authorization"] = "Bearer " + token

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        repos = json.load(resp)

    return [
        r
        for r in repos
        # Skip forks and the special profile-README repo (name == account name)
        if not r["fork"] and r["name"] != ACCOUNT
    ]


def build_section(repos: list[dict]) -> str:
    """Render the full marked block (markers included).

    Uses a simple bullet-list format because the GitHub API only provides a
    short description string — not the hand-crafted emojis and paragraphs
    that may have existed before the first automated run.  The markers
    delimit exactly what the script owns; everything outside them is untouched.
    """
    lines = [START_MARKER]
    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        desc = (repo.get("description") or "").strip()
        entry = f"- **[{name}]({url})**"
        if desc:
            entry += f" — {desc}"
        lines.append(entry)
    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme(new_section: str) -> bool:
    """Replace the marked block in README.md.  Returns True if file changed."""
    readme = os.path.realpath(README_PATH)
    with open(readme, encoding="utf-8") as fh:
        original = fh.read()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(original):
        print("ERROR: markers not found in README.md", file=sys.stderr)
        sys.exit(1)

    updated = pattern.sub(new_section, original)
    if updated == original:
        return False

    with open(readme, "w", encoding="utf-8") as fh:
        fh.write(updated)
    return True


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN", "")
    repos = fetch_repos(token)
    new_section = build_section(repos)
    changed = update_readme(new_section)
    if changed:
        print("README.md updated with latest repo list.")
    else:
        print("README.md is already up to date — nothing to commit.")


if __name__ == "__main__":
    main()
