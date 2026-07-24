<!--
This file is meant for a special GitHub "profile README" repo — a repo named
EXACTLY the same as your GitHub username (e.g. if your username is braxwilliams,
create a repo called "braxwilliams"). GitHub automatically shows that repo's
README.md at the top of your profile page. Copy this file's contents into that
repo as README.md.
-->

### Hi, I'm Braxton — I design and ship real, working AI agent systems.

12+ years as a U.S. Air Force public affairs officer, now pivoting that same discipline — clear communication, process rigor, real accountability — into building and implementing AI systems for real work, not demos.

**What I actually build:** persistent AI assistants with real memory, real verification discipline, and real production incidents I've debugged and fixed. The repos below aren't tutorials I copied — they're the exact tooling from a working system I run daily, cleaned up and generalized so you can use it too.

---

#### 🧠 [scout-blueprint](../scout-blueprint) — build your own persistent AI assistant
A complete, copy-paste spec for a voice-enabled AI assistant with real memory, a local dashboard, and $0/month cost beyond your existing Claude subscription. Documents the real failure modes (stale dashboards, broken links, permission sprawl) that only show up once you actually run something like this for a while.

#### 📓 [obsidian-vault-conventions](../obsidian-vault-conventions) — reliable AI-agent memory
A Claude Code skill that keeps an AI's persistent memory correctly readable by both the AI and a human browsing it in Obsidian — built after two real bugs (broken wikilinks, vanishing tags) taught me the hard way that these two "readers" don't agree on what a valid file looks like.

#### ✅ [post-change-verification](../post-change-verification) — don't trust, verify
The single most useful discipline I've built into my own agent workflows: the gap between "the file is fixed" and "the running system reflects it." A concrete process for catching the failure mode where an AI agent reports success and the fix genuinely doesn't reach production.

#### 🧵 [suite-workflow](../suite-workflow) — calibrated batch production
A four-stage pipeline (Ideate → Build → Self-check → Parallelise) for any "give me N of these" request, with a genuinely novel piece: a pre-committed prediction interview that measures whether an AI agent actually understands your decision-making, before letting it filter anything autonomously.

---

**What I'm looking to do next:** help teams and businesses actually implement AI well — not as a buzzword, but with the same rigor as the systems above: real memory design, real verification, honest about what breaks and how it gets fixed. If that's a conversation worth having, reach out.
