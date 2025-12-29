# Article Extraction Prompt Template

This document defines the prompt structure used by `ingest-article.py` to extract knowledge graph data from articles.

## Context

The prompt is sent to GitHub Models API (GPT-4o) with:
- System message establishing the expert role
- User message containing the article content and extraction instructions

## Prompt Structure

### System Message
```
You are a knowledge graph expert. Output only valid JSON.
```

### User Message Template

```
You are a knowledge graph expert. Analyze this article and extract structured information.

## Existing Concepts in the Knowledge Graph
These concepts already exist - use exact IDs when the article discusses them:
- knowledge-graph
- ontology
- neuro-symbolic-integration
- context-management
- uri-identifiers
- semantic-layer

## Article Content
{article_content}

## Instructions
Extract the following as valid JSON:

1. **metadata**: title, author, date (YYYY-MM-DD), category
2. **summary**: 2-3 sentence summary of key points
3. **key_concepts**: List of concept IDs this article discusses
4. **new_concepts**: For novel concepts not in existing list
5. **relationships**: Edges connecting article to concepts

## Output Format
{json_schema}
```

## Expected Output Schema

```json
{
  "metadata": {
    "title": "Article Title",
    "author": "Author Name",
    "date": "YYYY-MM-DD",
    "category": "Category Name"
  },
  "summary": "2-3 sentence summary...",
  "key_concepts": ["concept-id-1", "concept-id-2"],
  "new_concepts": [
    {
      "id": "kebab-case-id",
      "name": "Human Readable Name",
      "definition": "One sentence definition",
      "level": "foundational|intermediate|advanced"
    }
  ],
  "relationships": [
    {
      "type": "discusses",
      "to": "concept-id",
      "depth": "mentions|explains|deep-dive"
    },
    {
      "type": "relates_to",
      "from": "new-concept",
      "to": "existing-concept",
      "relation": "requires|enables|contrasts"
    }
  ]
}
```

## Concept Matching Heuristics

When the article mentions concepts, the model should:

1. **Exact match**: "knowledge graph" → `knowledge-graph`
2. **Alias match**: "KG" → `knowledge-graph`
3. **Partial match**: "ontological modeling" → `ontology`
4. **New concept**: If no match, suggest new ID

## Relationship Depth Guidelines

| Depth | Criteria |
|-------|----------|
| `mentions` | Concept named but not explained |
| `explains` | Concept defined or described |
| `deep-dive` | Concept is central to article's thesis |

## Updating This Template

When adding new concepts to the knowledge graph, update the "Existing Concepts" list in `ingest-article.py` to ensure proper matching.
