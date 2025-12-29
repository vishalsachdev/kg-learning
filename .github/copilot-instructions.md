# Copilot Instructions for kg-learning

This repository is a **knowledge graph-structured knowledge base** about knowledge graphs (meta!).

## Repository Structure

```
kg-learning/
├── manifest.json              ← START HERE - entry point with stats & learning path
├── schema/ontology.yaml       ← Entity types & relationship definitions
├── graph/
│   ├── entities.json          ← All nodes (concepts, articles, authors, categories)
│   └── relationships.json     ← All edges with types
├── concepts/*.md              ← Detailed concept files
├── sources/articles/*.md      ← Extracted article summaries
├── indexes/                   ← Human-readable navigation
├── scripts/                   ← Automation scripts
└── prompts/                   ← LLM prompt templates
```

## Adding an Article

When asked to add an article to the knowledge base:

1. **Fetch the article** from the provided URL
2. **Extract metadata:**
   - title, author, date, category
   - summary (2-3 sentences)
   - key concepts discussed
3. **Create article file:** `kg-learning/sources/articles/{slug}.md`
   - Use existing articles as templates (e.g., `swiss-cheese-problem.md`)
4. **Update entities.json:** Add article entry with proper ID format `article:{slug}`
5. **Update relationships.json:** Add `discusses` relationships to concepts
6. **Create new concepts** if the article introduces novel ideas not in existing concepts
7. **Update manifest.json:** Increment stats

## ID Conventions

- Articles: `article:{kebab-case-slug}`
- Concepts: `concept:{kebab-case-name}`
- Authors: `author:{firstname-lastname}`
- Categories: `category:{kebab-case-name}`

## Existing Concepts

Check `kg-learning/graph/entities.json` for existing concepts before creating new ones:
- knowledge-graph
- ontology
- neuro-symbolic-integration
- context-management
- uri-identifiers
- semantic-layer

## Relationship Types

From `schema/ontology.yaml`:
- `discusses`: Article → Concept (depth: mentions/explains/deep-dive)
- `written_by`: Article → Author
- `relates_to`: Concept → Concept (relation: requires/enables/contrasts)

## Quality Checklist

Before completing any PR:
- [ ] All file paths in `entities.json` point to existing files
- [ ] All concept cross-links in `.md` files exist
- [ ] All entity IDs in `relationships.json` exist in `entities.json`
- [ ] `manifest.json` stats are updated

## Testing

Run the ingestion scripts manually to validate:
```bash
# Test article fetch
curl -sL "https://example.com/article" > test.html

# Validate JSON files
python -c "import json; json.load(open('kg-learning/graph/entities.json'))"
python -c "import json; json.load(open('kg-learning/graph/relationships.json'))"
```
