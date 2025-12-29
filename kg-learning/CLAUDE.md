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
kg-learning/
├── schema/ontology.yaml   # Entity types & relationship definitions
├── sources/articles/      # Extracted source materials (markdown)
├── concepts/              # Core concepts as individual files
├── graph/
│   ├── entities.json      # All nodes
│   └── relationships.json # All edges
└── indexes/               # Navigation entry points
```

## For AI Agents

### Quick Navigation
- **Find a concept**: Check `concepts/{concept-name}.md` or `indexes/by-concept.md`
- **Find sources on a topic**: Check `indexes/by-category.md`
- **Understand relationships**: Read `graph/relationships.json`

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

## Contributing

When adding new sources:
1. Follow the ontology schema
2. Extract concepts with clear definitions
3. Establish relationships to existing concepts
4. Update indexes for discoverability
