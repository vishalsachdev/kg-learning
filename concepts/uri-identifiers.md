# URI Identifiers

- **id**: concept:uri-identifiers
- **level**: foundational
- **aliases**: [URIs, Uniform Resource Identifiers, entity identifiers, IRIs]

## Definition

**URIs (Uniform Resource Identifiers)** are stable, globally unique identifiers for entities in knowledge systems. They provide unambiguous identity that persists across systems and time.

## Why URIs Matter

1. **Stable Identity**: Same entity = same identifier everywhere
2. **Global Uniqueness**: No collisions across organizations
3. **Resolvability**: Can link to more information (like URLs)
4. **Integration**: Enables connecting data across sources

## URI Patterns

```
# Examples
https://example.org/entities/customer/12345
urn:isbn:978-3-16-148410-0
https://www.wikidata.org/entity/Q937
```

## URIs vs. Database IDs

| Aspect | Database ID | URI |
|--------|-------------|-----|
| Scope | Local to system | Global |
| Stability | May change | Designed to persist |
| Meaning | Arbitrary | Can be meaningful |
| Linkability | Requires mapping | Direct linking |

## The Integration Imperative

> URIs and ontologies are not optional extras—they are prerequisites for AI-ready data.

Without stable identifiers, AI agents face:
- Ambiguity about what entities they're reasoning about
- Broken links between data sources
- Duplicated effort to reconcile identities

## Related Concepts

- [ontology](ontology.md) - defines what URIs identify
- [knowledge-graph](knowledge-graph.md) - uses URIs as node identifiers
- [data-integration](data-integration.md) - enabled by URIs

## Sources

- [Integration Isn't Optional](../sources/articles/integration-isnt-optional.md)
