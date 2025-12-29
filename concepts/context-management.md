# Context Management

- **id**: concept:context-management
- **level**: intermediate
- **aliases**: [context engineering, context curation, prompt context]

## Definition

**Context management** is the deliberate curation and structuring of information provided to LLMs, focusing on precision and relevance rather than volume.

## The Problem: Context Rot

> "Long context often makes things worse"

Bigger context windows don't solve retrieval challenges:
- Reasoning collapses when signal gets lost in noise
- Semantic similarity causes confusion
- Distractor facts degrade performance
- Information ordering matters

## Context Engineering Principles

1. **Strategic selection**: Choose what to include carefully
2. **Optimal placement**: Position matters for attention
3. **Focus maintenance**: Don't dilute with irrelevant tokens
4. **Structure preservation**: Keep semantic relationships clear

## How Knowledge Graphs Help

KGs enable precise context through:
- **Ontological constraints**: Reduce search space
- **Disambiguation**: Clarify similar matches
- **Intelligent filtering**: Relevance-based selection
- **Reasoning chains**: Explain why context is relevant

## Key Insight

> "Long context is a tool"—valuable but insufficient alone.

Genuine performance comes from "reasoned, precise context" not comprehensive prompt saturation.

## Related Concepts

- [knowledge-graph](knowledge-graph.md) - provides structured context
- [neuro-symbolic-integration](neuro-symbolic-integration.md) - broader pattern

## Sources

- [Context Rot](../sources/articles/context-rot.md)
