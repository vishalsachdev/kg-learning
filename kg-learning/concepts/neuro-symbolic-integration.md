# Neuro-Symbolic Integration

- **id**: concept:neuro-symbolic-integration
- **level**: advanced
- **aliases**: [neuro-symbolic AI, hybrid AI, neural-symbolic]

## Definition

**Neuro-symbolic integration** combines neural networks (learning from data) with symbolic systems (reasoning over structured knowledge) to create AI that is both flexible and reliable.

## The Two Paradigms

### Neural (Distributed Representations)
- Concepts "smeared" across millions of parameters
- Excels at: pattern recognition, creativity, noise tolerance
- Struggles with: compositionality, determinism, explainability

### Symbolic (Local Representations)
- Discrete, unambiguous symbols and variables
- Excels at: logical composition, systematic generalization, verifiability
- Struggles with: handling noise, learning from raw data

## Why Integration Matters

> "Neural and symbolic systems are not rivals; they are complements."

The "Swiss Cheese Problem": LLMs can reason brilliantly across many steps, then fail catastrophically on simple logical tasks. Symbolic grounding fills the holes.

## Integration Patterns

1. **Symbols guide networks**: Ontology constraints focus neural attention
2. **Networks extend symbols**: LLMs extract new relationships for KGs
3. **Feedback loops**: Each system improves the other iteratively

## Success Examples

- **AlphaFold**: Neural + physical/geometric constraints
- **AlphaEvolve**: Neural creativity + symbolic code testing

## Related Concepts

- [knowledge-graph](knowledge-graph.md) - provides symbolic backbone
- [context-management](context-management.md) - applies structured context to LLMs

## Sources

- [The Swiss Cheese Problem](../sources/articles/swiss-cheese-problem.md)
