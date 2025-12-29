# When Your Knowledge Graph Graduates: From Experiment to Autonomous System

*A journey through building a self-feeding knowledge base, and the unexpected discovery that changed everything*

---

## The Setup: Experiments as Siblings, Not Children

I have a repo called `helloworld` that serves as an experiment framework. It's not a typical project—it's a launchpad. Every experiment gets its own branch and worktree, living as a *sibling folder* rather than a subfolder. The mental model matters: experiments are peers, not nested children.

```
/Users/vishal/code/
├── helloworld/            ← The framework (main branch)
├── gies-agent-demo/       ← An experiment
├── factorio-skills/       ← Another experiment
├── kg-learning/           ← Today's story
└── ...
```

This structure uses git worktrees—one git history, multiple working directories. Each experiment has its own `CLAUDE.md` with project context, its own roadmap, its own session log. When an experiment matures, it "graduates" to a standalone repository.

Today, `kg-learning` was ready to graduate.

---

## The Knowledge Graph About Knowledge Graphs

The experiment itself was delightfully meta: a knowledge graph-structured repository for learning about knowledge graphs. I'd built it to explore ideas from [The Knowledge Graph Guys blog](https://www.knowledge-graph-guys.com/blog)—articles about neuro-symbolic integration, context management, and why LLMs need symbolic backbones.

The structure was deliberately agent-friendly:

- **manifest.json** — A single entry point with stats, learning paths, and quick-start instructions for AI agents
- **schema/ontology.yaml** — Entity types (Concept, Article, Author) and relationship types (discusses, requires, enables)
- **graph/entities.json** + **relationships.json** — The actual graph data, 19 entities connected by 18 relationships
- **concepts/*.md** — Human-readable concept files with definitions and cross-links

The repo embodied its own subject matter. It used URI-style identifiers (`concept:knowledge-graph`, `article:swiss-cheese-problem`), ontology-first design, and graph-navigable relationships. Dogfooding at its finest.

But it had a problem: adding new articles was manual. Five steps, multiple JSON edits, easy to make mistakes. If I wanted this knowledge base to grow, I needed automation.

---

## Graduation Day

The first step was graduating kg-learning to its own repository. The worktree pattern made this clean:

1. Create the new repo on GitHub
2. Push the experiment branch as `main`
3. Remove the worktree from helloworld
4. Delete the experiment branch

Within minutes, `kg-learning` was a standalone citizen at [github.com/vishalsachdev/kg-learning](https://github.com/vishalsachdev/kg-learning).

Now came the interesting part: building an article ingestion pipeline.

---

## The Automation Dream: Phone to Knowledge Graph

The vision was simple: I should be able to add an article to my knowledge graph from my phone while waiting for coffee.

The workflow I designed:

1. **Create a GitHub Issue** with the article URL (works from GitHub mobile)
2. **GitHub Action triggers** on the `article-ingest` label
3. **LLM extracts** metadata, concepts, and relationships
4. **Script generates** all the files and JSON updates
5. **Auto-merge** to main (no PR review needed)

I built it all: the workflow YAML, the issue template, the Python scripts for extraction and file generation. The architecture was clean—fetch article, call API, generate files, commit.

Then it failed.

---

## The First Roadblock: Authentication

The GitHub Models API (the endpoint for using GPT-4o through GitHub) returned 401 Unauthorized. The default `GITHUB_TOKEN` in Actions has repo permissions but not access to the Models API.

This is a classic DevOps puzzle. The token that can commit code can't call the LLM. I updated the script to support both OpenAI API and GitHub Models, added documentation about adding secrets.

But then I asked a question that changed everything: *Why can't we just use GitHub Copilot?*

---

## The Discovery: Copilot as Teammate

The web search revealed something I hadn't known: GitHub Copilot now has a **Coding Agent**. It's not just autocomplete anymore. You can *assign an issue to Copilot*, and it works like a junior developer—reading your codebase, understanding the task, creating a PR.

The workflow becomes radically simpler:

1. Create issue with article URL
2. Assign to `@copilot`
3. Copilot reads the repo (including `manifest.json`, the ontology, existing articles)
4. Copilot creates a PR with all the right files

No custom scripts. No API keys. No maintenance burden.

I enabled Copilot for the repo and assigned my test issue. Within seconds, Copilot had:
- Explored the repository structure
- Reviewed the existing ingestion scripts
- Checked the knowledge graph data
- Created a draft PR with a checklist of what it was doing

It was *thinking* about the problem, not just executing instructions.

---

## Two Philosophies of AI Automation

What struck me was the contrast between the two approaches:

| Aspect | Custom Workflow | Copilot Agent |
|--------|-----------------|---------------|
| Trigger | Issue label | Assignee |
| Processing | Script + API call | Full agent exploration |
| Speed | ~30 seconds | ~5-10 minutes |
| Intelligence | Fixed prompt | Adaptive to repo context |
| Output | Direct commit | PR for review |
| Maintenance | You own it | GitHub owns it |

The custom workflow is **control**. You specify exactly what happens, how the prompt is structured, what files get created. It's fast, deterministic, and fully automated.

The Copilot agent is **trust**. You describe the outcome, and the agent figures out the path. It's slower, but it adapts. It reads your `CLAUDE.md` and understands your conventions. It creates a checklist and works through it methodically.

Both are valid. The question is: what are you optimizing for?

---

## The Compound Engineering Loop

This session was a perfect example of what I've been calling [compound engineering](https://chatwithgpt.substack.com/p/compound-engineering-use-it-before)—building on existing tools rather than starting from scratch, and letting discoveries compound into better systems.

The loop went like this:

1. **Use existing tools** (worktree pattern, graduation workflow)
2. **Hit a limitation** (manual article ingestion)
3. **Build a solution** (GitHub Action + scripts)
4. **Discover a better way** (Copilot Agent)
5. **Keep both** (fast automation + intelligent agent)

Along the way, I also improved the framework itself. The `start-session` skill now checks for remote branches that might exist from other devices or Claude Code sessions. A small improvement, but one that compounds—every future session benefits.

---

## The Meta Lesson: Knowledge Graphs for AI Context

There's a deeper connection here. The articles I was ingesting—about neuro-symbolic integration, context management, the "Swiss Cheese Problem"—argue that LLMs need structured knowledge to reason reliably.

The `kg-learning` repo *is* that structured knowledge. The `manifest.json` tells an AI agent exactly how to navigate the repo. The ontology schema defines what entities and relationships can exist. The JSON graph provides traversable, queryable structure.

When I assigned the issue to Copilot, it worked *because* the repo was well-structured. Copilot read the manifest, understood the conventions, and knew what files to create. The knowledge graph made the AI agent smarter.

That's the promise of this whole field: structure enables intelligence. Not just for retrieval, but for action.

---

## What's Next

The kg-learning repo now has two ingestion paths:
- **Custom workflow** for batch processing (once I add the API key)
- **Copilot agent** for thoughtful, one-off additions

I also created a `.github/copilot-instructions.md` file—essentially onboarding documentation for Copilot. Future tasks will benefit from that context.

The pending articles list still has 16 items from The Knowledge Graph Guys blog. Each one will expand the graph, and each expansion makes the structure more useful for AI reasoning.

It's a self-reinforcing system: the more I add, the smarter the agents become at adding more.

---

## The Takeaway

If you're building systems that AI agents will interact with, invest in structure:

1. **manifest.json** — A single entry point that explains everything
2. **Schema definitions** — What can exist and how things relate
3. **Onboarding docs** — Tell the AI how to work in your repo

The age of "vibe coding" is giving way to spec-first development. Not because vibes don't work, but because structure compounds. Every well-defined schema is a force multiplier for every AI that reads it.

My knowledge graph graduated today. And in a way, so did my understanding of what AI automation can be.

---

*This article was written during a live collaboration session with Claude Code. The session included graduating an experiment repo, building a GitHub Actions pipeline, discovering GitHub Copilot Coding Agent, and reflecting on two philosophies of AI automation.*
