# Semantic Layer

- **id**: concept:semantic-layer
- **level**: intermediate
- **aliases**: [meaning layer, business semantics layer]

## Definition

A **semantic layer** is an abstraction that sits between raw data and applications, translating technical data structures into business-meaningful concepts that humans and AI can understand.

## Purpose

1. **Translation**: Technical schemas → business vocabulary
2. **Accessibility**: Enable non-technical users to query data
3. **Consistency**: Single source of truth for definitions
4. **AI Grounding**: Provide context for AI systems

## How It Works

```
[Raw Data] → [Semantic Layer] → [Applications/AI]
   ↓              ↓                    ↓
 Tables      Business Terms       Natural Language
 Joins       Relationships        Questions
 Keys        Identities           Answers
```

## Benefits

- **Business users**: Ask questions without SQL
- **AI systems**: Understand domain context
- **Data teams**: Define once, use everywhere
- **Organizations**: Unified vocabulary

## Relationship to Knowledge Graphs

Knowledge graphs implement semantic layers by:
- Modeling business entities explicitly
- Defining relationships formally
- Providing traversable structure
- Enabling natural language interfaces

## Related Concepts

- [ontology](ontology.md) - formal specification behind the layer
- [knowledge-graph](knowledge-graph.md) - implementation vehicle
- [data-integration](data-integration.md) - what semantic layer enables

## Sources

- [Knowledge Graphs Are Going Mainstream](../sources/articles/kg-going-mainstream.md)
