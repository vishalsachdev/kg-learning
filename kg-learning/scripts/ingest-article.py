#!/usr/bin/env python3
"""
Article Ingestion Script

Extracts metadata, concepts, and relationships from article content
using GitHub Models API (OpenAI-compatible).

Usage:
    python ingest-article.py --url URL --content FILE --output OUTPUT.json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import requests

# GitHub Models API endpoint (OpenAI-compatible)
GITHUB_MODELS_URL = "https://models.inference.ai.azure.com/chat/completions"

# Existing concepts in the knowledge graph
EXISTING_CONCEPTS = [
    "knowledge-graph",
    "ontology",
    "neuro-symbolic-integration",
    "context-management",
    "uri-identifiers",
    "semantic-layer",
]

EXTRACTION_PROMPT = """You are a knowledge graph expert. Analyze this article and extract structured information.

## Existing Concepts in the Knowledge Graph
These concepts already exist - use exact IDs when the article discusses them:
{existing_concepts}

## Article Content
{content}

## Instructions
Extract the following as valid JSON:

1. **metadata**: title, author, date (YYYY-MM-DD), category
2. **summary**: 2-3 sentence summary of key points
3. **key_concepts**: List of concept IDs this article discusses
   - Use existing concept IDs if they match
   - Suggest new concept IDs (kebab-case) for novel concepts
4. **new_concepts**: For each new concept, provide:
   - id (kebab-case)
   - name (Title Case)
   - definition (1-2 sentences)
   - level (foundational/intermediate/advanced)
5. **relationships**: List of edges to add
   - For article→concept: type="discusses", depth="mentions"|"explains"|"deep-dive"
   - For concept→concept: type="relates_to", relation="requires"|"enables"|"contrasts"

## Output Format
Return ONLY valid JSON, no markdown code blocks:
{{
  "metadata": {{
    "title": "...",
    "author": "...",
    "date": "YYYY-MM-DD",
    "category": "..."
  }},
  "summary": "...",
  "key_concepts": ["concept-id-1", "concept-id-2"],
  "new_concepts": [
    {{
      "id": "new-concept-id",
      "name": "New Concept Name",
      "definition": "...",
      "level": "intermediate"
    }}
  ],
  "relationships": [
    {{"type": "discusses", "to": "concept-id", "depth": "deep-dive"}},
    {{"type": "relates_to", "from": "new-concept", "to": "existing-concept", "relation": "requires"}}
  ]
}}
"""


def load_content(content_path: str) -> str:
    """Load article content from file."""
    with open(content_path, "r") as f:
        return f.read()


def call_github_models(prompt: str) -> dict:
    """Call GitHub Models API to extract information."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a knowledge graph expert. Output only valid JSON."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
        "max_tokens": 4000,
    }

    response = requests.post(GITHUB_MODELS_URL, headers=headers, json=payload)
    response.raise_for_status()

    result = response.json()
    content = result["choices"][0]["message"]["content"]

    # Parse JSON from response (handle potential markdown code blocks)
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\n?", "", content)
        content = re.sub(r"\n?```$", "", content)

    return json.loads(content)


def generate_slug(title: str) -> str:
    """Generate URL-friendly slug from title."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug[:50]


def main():
    parser = argparse.ArgumentParser(description="Extract article information for knowledge graph")
    parser.add_argument("--url", required=True, help="Original article URL")
    parser.add_argument("--content", required=True, help="Path to article content file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    # Load article content
    content = load_content(args.content)

    # Truncate if too long (token limits)
    if len(content) > 15000:
        content = content[:15000] + "\n\n[Content truncated...]"

    # Build prompt
    existing_concepts_str = "\n".join(f"- {c}" for c in EXISTING_CONCEPTS)
    prompt = EXTRACTION_PROMPT.format(
        existing_concepts=existing_concepts_str,
        content=content,
    )

    # Call API
    print("Calling GitHub Models API for extraction...")
    extraction = call_github_models(prompt)

    # Add URL and generate slug
    extraction["url"] = args.url
    extraction["slug"] = generate_slug(extraction["metadata"]["title"])
    extraction["article_id"] = f"article:{extraction['slug']}"

    # Write output
    with open(args.output, "w") as f:
        json.dump(extraction, f, indent=2)

    print(f"Extraction complete: {args.output}")
    print(f"  Title: {extraction['metadata']['title']}")
    print(f"  Concepts: {len(extraction['key_concepts'])}")
    print(f"  New concepts: {len(extraction.get('new_concepts', []))}")


if __name__ == "__main__":
    main()
