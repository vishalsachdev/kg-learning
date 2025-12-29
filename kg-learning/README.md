# KG Learning

A knowledge graph-structured repository for learning about knowledge graphs.

> "Using knowledge graph principles to learn about knowledge graphs" (meta!)

## Quick Start

### For Humans

1. **New to KGs?** Start with [Concepts → Foundational](indexes/by-concept.md#foundational-concepts)
2. **Want to read articles?** Browse [Sources Index](indexes/by-source.md)
3. **Looking for a topic?** Check [Category Index](indexes/by-category.md)

### For AI Agents

1. **Understand the schema**: Read `schema/ontology.yaml`
2. **Navigate entities**: Parse `graph/entities.json`
3. **Traverse relationships**: Query `graph/relationships.json`
4. **Get detailed content**: Read `concepts/*.md` or `sources/articles/*.md`

## Repository Structure

```
kg-learning/
├── CLAUDE.md              # Agent instructions
├── schema/
│   └── ontology.yaml      # Entity types & relationships
├── sources/
│   └── articles/          # Extracted source materials
├── concepts/              # Core KG concepts
├── graph/
│   ├── entities.json      # All nodes
│   └── relationships.json # All edges
└── indexes/               # Navigation entry points
    ├── by-concept.md      # Concept hierarchy
    ├── by-source.md       # Source materials
    └── by-category.md     # Topic categories
```

## Current Knowledge Graph

### Entities
- **6 Concepts**: knowledge-graph, ontology, neuro-symbolic-integration, context-management, uri-identifiers, semantic-layer
- **4 Articles**: from The Knowledge Graph Guys blog
- **2 Authors**: Tony Seale, Callum Hornblower
- **7 Categories**: Knowledge Graphs, AI, Enterprise AI, Semantics, LLMs, AI Agents, Agentic AI

### Relationships
- **18 edges** connecting articles to concepts, concepts to concepts, and articles to authors

## Key Insights from Sources

1. **The Swiss Cheese Problem**: LLMs fail unpredictably on simple tasks. Solution: neuro-symbolic integration with knowledge graphs as symbolic backbone.

2. **Context Rot**: Bigger context windows don't solve retrieval. Solution: precise, ontology-guided context management.

3. **Integration Isn't Optional**: AI-ready data requires URIs and ontologies. Deferring integration creates compounding costs.

4. **KGs Going Mainstream**: SAP, Netflix, ServiceNow, Samsung adopting KGs as foundational infrastructure, not optional tech.

## Adding New Content

See [CLAUDE.md](CLAUDE.md) for detailed instructions on:
- Adding source articles
- Creating concept entries
- Updating the graph

## Primary Source

[The Knowledge Graph Guys Blog](https://www.knowledge-graph-guys.com/blog) - 20+ articles on knowledge graphs, ontologies, and AI.
