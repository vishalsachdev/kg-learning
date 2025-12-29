# KG Learning Repository

A knowledge graph-structured repository for learning about knowledge graphs.

## Repo Type
type: knowledge-base

## Purpose

This repository uses **knowledge graph principles** to organize knowledge about knowledge graphs. It serves as:
1. A learning resource for KG concepts
2. An AI-agent friendly knowledge base
3. A demonstration of KG-based information architecture

## Repository Structure

```
├── manifest.json          # START HERE - agent entry point
├── schema/ontology.yaml   # Entity types & relationship definitions
├── sources/articles/      # Extracted source materials (markdown)
├── concepts/              # Core concepts as individual files
├── graph/
│   ├── entities.json      # All nodes
│   └── relationships.json # All edges
├── indexes/               # Navigation entry points (human-readable)
├── articles/              # Newsletter articles about this project
└── scripts/               # Automation scripts
```

## For AI Agents

### Quick Start (5 steps)
1. **Load `manifest.json`** — understand structure, stats, learning path
2. **Load `graph/entities.json`** — all nodes (concepts, articles, authors)
3. **Load `graph/relationships.json`** — all edges with types
4. **Read `concepts/{id}.md`** — detailed concept content
5. **Read `sources/articles/{id}.md`** — source material

### Quick Navigation
- **Find a concept**: Check `concepts/{concept-name}.md` or `indexes/by-concept.md`
- **Find sources on a topic**: Check `indexes/by-category.md`
- **Understand relationships**: Read `graph/relationships.json`
- **Get learning path**: Check `manifest.json` → `learningPath.order`

### Adding New Content

1. **Add a source article**:
   - Create `sources/articles/{source-id}.md`
   - Extract key concepts and add to `graph/entities.json`
   - Add relationships to `graph/relationships.json`
   - Update relevant indexes

2. **Add a concept**:
   - Create `concepts/{concept-id}.md` with definition, examples, related concepts
   - Add to `graph/entities.json`
   - Link to existing concepts in `graph/relationships.json`

3. **Query the knowledge base**:
   - For concept definitions: read `concepts/`
   - For source material: read `sources/articles/`
   - For relationship traversal: parse `graph/relationships.json`

### Schema Reference
See `schema/ontology.yaml` for entity types and relationship definitions.

## Key Concepts Covered

Based on Knowledge Graph Guys blog:
- **Neuro-Symbolic Integration**: Combining neural (LLM) and symbolic (KG) approaches
- **Ontologies**: Formal specifications of domain concepts
- **Semantic Layer**: Meaning layer between data and applications
- **URI Identifiers**: Stable, resolvable identifiers for data
- **Context Management**: Precise context for LLM grounding
- **Agentic AI**: AI agents operating with KG foundations

## Sources

Primary source: [The Knowledge Graph Guys Blog](https://www.knowledge-graph-guys.com/blog)

## Adding Articles (Automated)

The easiest way to add articles is via **GitHub Issue**:

### From Phone or Desktop
1. Go to [New Issue](../../issues/new/choose)
2. Select "Add Article to Knowledge Base"
3. Paste the article URL
4. Submit!

The GitHub Action will automatically:
- Fetch and parse the article
- Extract metadata, concepts, and relationships
- Generate all necessary files
- Commit directly to main

### Alternative: Assign to Copilot
1. Create an issue with the article URL
2. Assign to `@copilot`
3. Copilot will create a PR with all necessary changes

### Manual Fallback
If automation fails:
1. Follow the ontology schema
2. Extract concepts with clear definitions
3. Establish relationships to existing concepts
4. Update indexes for discoverability

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/ingest-article.py` | Extract metadata from article using GitHub Models API |
| `scripts/generate-files.py` | Generate markdown and update JSON files |

### Running Manually
```bash
# Fetch article content
curl -o article.html "https://example.com/article"

# Extract with GitHub Models API
GITHUB_TOKEN=xxx python scripts/ingest-article.py \
  --url "https://example.com/article" \
  --content article.html \
  --output extraction.json

# Generate files
python scripts/generate-files.py --extraction extraction.json
```

## Validation Checklist

Before committing changes, verify:

- [ ] All `file` paths in `entities.json` point to existing files
- [ ] All `## Related Concepts` links in `.md` files exist
- [ ] All entity IDs in `relationships.json` exist in `entities.json`
- [ ] No orphan entities (every concept has at least one relationship)
- [ ] `manifest.json` stats are up-to-date

**Common issues:**
- Adding concept to markdown but forgetting `entities.json`
- Cross-linking to concepts not yet created (like `graphrag.md`)
- Updating content without updating `lastUpdated` in manifest
