# Ontology

- **id**: concept:ontology
- **level**: foundational
- **aliases**: [schema, conceptual model, formal specification]

## Definition

An **ontology** is a formal, explicit specification of a shared conceptualization. It defines:
- What types of entities exist in a domain
- What relationships can exist between them
- What constraints apply

## Key Components

1. **Classes**: Categories of entities (Person, Product, Event)
2. **Properties**: Attributes and relationships (hasName, worksFor)
3. **Constraints**: Rules about valid structures (cardinality, domains)
4. **Instances**: Actual entities conforming to the schema

## Why It Matters

> "Model once and represent everywhere"

- Ensures **semantic consistency** across systems
- Enables **machine reasoning** over structure
- Supports **interoperability** between data sources
- Provides **shared vocabulary** for teams

## Ontology vs. Schema

| Aspect | Database Schema | Ontology |
|--------|-----------------|----------|
| Purpose | Storage optimization | Meaning representation |
| Flexibility | Rigid | Extensible |
| Reasoning | Limited | Rich inference |
| Standards | Vendor-specific | Open (OWL, RDFS) |

## Related Concepts

- [knowledge-graph](knowledge-graph.md) - implements the ontology
- [uri-identifiers](uri-identifiers.md) - identifies ontology elements
- [semantic-layer](semantic-layer.md) - exposes ontology to apps

## Sources

- [Integration Isn't Optional](../sources/articles/integration-isnt-optional.md)
- [Knowledge Graphs Are Going Mainstream](../sources/articles/kg-going-mainstream.md)
