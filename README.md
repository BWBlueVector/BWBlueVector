### Hi, I'm Braxton — I design and ship real, working AI agent systems.

12+ years as a U.S. Air Force public affairs officer, now pivoting that same discipline — clear communication, process rigor, real accountability — into building and implementing AI systems for real work, not demos.

**What I actually build:** persistent AI assistants with real memory, real verification discipline, and real production incidents I've debugged and fixed. The repos below aren't tutorials I copied — they're the exact tooling from a working system I run daily, cleaned up and generalized so you can use it too.

---

<!-- REPOS:START -->
#### 🧠 [scout-blueprint](https://github.com/BWBlueVector/scout-blueprint) — build your own persistent AI assistant
A complete, copy-paste spec for a voice-enabled AI assistant with real memory, a local dashboard, and $0/month cost beyond your existing Claude subscription. Documents the real failure modes (stale dashboards, broken links, permission sprawl) that only show up once you actually run something like this for a while.

#### 📓 [obsidian-vault-conventions](https://github.com/BWBlueVector/obsidian-vault-conventions) — reliable AI-agent memory
A Claude Code skill that keeps an AI's persistent memory correctly readable by both the AI and a human browsing it in Obsidian — built after two real bugs (broken wikilinks, vanishing tags) taught me the hard way that these two "readers" don't agree on what a valid file looks like.

#### ✅ [post-change-verification](https://github.com/BWBlueVector/post-change-verification) — don't trust, verify
The single most useful discipline I've built into my own agent workflows: the gap between "the file is fixed" and "the running system reflects it." A concrete process for catching the failure mode where an AI agent reports success and the fix genuinely doesn't reach production.

#### 🧵 [suite-workflow](https://github.com/BWBlueVector/suite-workflow) — calibrated batch production
A four-stage pipeline (Ideate → Build → Self-check → Parallelise) for any "give me N of these" request, with a genuinely novel piece: a pre-committed prediction interview that measures whether an AI agent actually understands your decision-making, before letting it filter anything autonomously.
<!-- REPOS:END -->

---

**What I'm looking to do next:** help teams and businesses actually implement AI well — not as a buzzword, but with the same rigor as the systems above: real memory design, real verification, honest about what breaks and how it gets fixed. If that's a conversation worth having, reach out.
