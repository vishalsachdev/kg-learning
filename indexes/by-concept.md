# Concepts Index

Navigate the knowledge base by concept.

## Foundational Concepts

Start here if you're new to knowledge graphs.

| Concept | Description | Key Article |
|---------|-------------|-------------|
| [Knowledge Graph](../concepts/knowledge-graph.md) | Structured representation connecting entities through relationships | [KG Going Mainstream](../sources/articles/kg-going-mainstream.md) |
| [Ontology](../concepts/ontology.md) | Formal specification of domain concepts and relationships | [Integration Isn't Optional](../sources/articles/integration-isnt-optional.md) |
| [URI Identifiers](../concepts/uri-identifiers.md) | Stable, globally unique entity identifiers | [Integration Isn't Optional](../sources/articles/integration-isnt-optional.md) |

## Intermediate Concepts

Build on foundational knowledge.

| Concept | Description | Key Article |
|---------|-------------|-------------|
| [Semantic Layer](../concepts/semantic-layer.md) | Abstraction translating data to business meaning | [KG Going Mainstream](../sources/articles/kg-going-mainstream.md) |
| [Context Management](../concepts/context-management.md) | Precise context curation for LLMs | [Context Rot](../sources/articles/context-rot.md) |

## Advanced Concepts

For deep understanding.

| Concept | Description | Key Article |
|---------|-------------|-------------|
| [Neuro-Symbolic Integration](../concepts/neuro-symbolic-integration.md) | Combining neural networks with symbolic reasoning | [Swiss Cheese Problem](../sources/articles/swiss-cheese-problem.md) |

## Concept Relationships

```
                    ┌─────────────────────┐
                    │ Neuro-Symbolic      │
                    │ Integration         │
                    └─────────┬───────────┘
                              │ requires
                              ▼
┌───────────────┐   ┌─────────────────────┐   ┌─────────────────┐
│ Context       │──▶│ Knowledge Graph     │◀──│ Semantic Layer  │
│ Management    │   └─────────┬───────────┘   └─────────────────┘
└───────────────┘             │ requires
        enables               ▼
                    ┌─────────────────────┐
                    │ Ontology            │
                    └─────────┬───────────┘
                              │ requires
                              ▼
                    ┌─────────────────────┐
                    │ URI Identifiers     │
                    └─────────────────────┘
```
