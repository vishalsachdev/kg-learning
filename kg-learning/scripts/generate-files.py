#!/usr/bin/env python3
"""
File Generation Script

Takes extraction JSON and generates/updates all necessary files:
- sources/articles/{slug}.md
- graph/entities.json
- graph/relationships.json
- concepts/*.md (for new concepts)
- indexes/by-source.md
- manifest.json

Usage:
    python generate-files.py --extraction extraction.json
"""

import argparse
import json
from datetime import date
from pathlib import Path


def load_extraction(path: str) -> dict:
    """Load extraction JSON."""
    with open(path, "r") as f:
        return json.load(f)


def load_json(path: Path) -> dict:
    """Load existing JSON file."""
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return {}


def save_json(path: Path, data: dict):
    """Save JSON file with nice formatting."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def generate_article_markdown(extraction: dict) -> str:
    """Generate article markdown file content."""
    meta = extraction["metadata"]
    concepts_str = ", ".join(extraction["key_concepts"])

    return f"""# {meta['title']}

- **id**: {extraction['article_id']}
- **url**: {extraction['url']}
- **author**: {meta['author']}
- **date**: {meta['date']}
- **category**: {meta['category']}
- **key_concepts**: [{concepts_str}]

## Summary

{extraction['summary']}

## Key Takeaway

See the original article for full content.
"""


def generate_concept_markdown(concept: dict) -> str:
    """Generate concept markdown file content."""
    return f"""# {concept['name']}

- **id**: concept:{concept['id']}
- **level**: {concept['level']}
- **aliases**: []

## Definition

{concept['definition']}

## Related Concepts

(To be filled in as more content is added)

## Sources

(Auto-generated - sources will be linked as articles are added)
"""


def update_entities(entities_path: Path, extraction: dict):
    """Add article entity and any new concepts to entities.json."""
    data = load_json(entities_path)

    if "entities" not in data:
        data["entities"] = {"concepts": [], "articles": [], "authors": [], "categories": []}

    # Add article entity
    article_entity = {
        "id": extraction["article_id"],
        "type": "Article",
        "title": extraction["metadata"]["title"],
        "author": f"author:{extraction['metadata']['author'].lower().replace(' ', '-')}",
        "date": extraction["metadata"]["date"],
        "category": f"category:{extraction['metadata']['category'].lower().replace(' ', '-')}",
        "file": f"sources/articles/{extraction['slug']}.md",
    }

    # Check if article already exists
    existing_ids = {a["id"] for a in data["entities"]["articles"]}
    if extraction["article_id"] not in existing_ids:
        data["entities"]["articles"].append(article_entity)

    # Add new concepts
    existing_concept_ids = {c["id"] for c in data["entities"]["concepts"]}
    for new_concept in extraction.get("new_concepts", []):
        concept_id = f"concept:{new_concept['id']}"
        if concept_id not in existing_concept_ids:
            concept_entity = {
                "id": concept_id,
                "type": "Concept",
                "name": new_concept["name"],
                "level": new_concept["level"],
                "file": f"concepts/{new_concept['id']}.md",
            }
            data["entities"]["concepts"].append(concept_entity)

    save_json(entities_path, data)


def update_relationships(relationships_path: Path, extraction: dict):
    """Add relationships from extraction."""
    data = load_json(relationships_path)

    if "relationships" not in data:
        data["relationships"] = []

    existing_rels = len(data["relationships"])

    for rel in extraction.get("relationships", []):
        new_rel = {"id": f"rel:{existing_rels + 1}", "type": rel["type"]}

        if rel["type"] == "discusses":
            new_rel["from"] = extraction["article_id"]
            new_rel["to"] = f"concept:{rel['to']}"
            new_rel["depth"] = rel.get("depth", "mentions")
        elif rel["type"] == "relates_to":
            new_rel["from"] = f"concept:{rel['from']}"
            new_rel["to"] = f"concept:{rel['to']}"
            new_rel["relation"] = rel.get("relation", "relates")
        elif rel["type"] == "written_by":
            new_rel["from"] = extraction["article_id"]
            new_rel["to"] = rel["to"]

        data["relationships"].append(new_rel)
        existing_rels += 1

    # Add written_by relationship
    author_id = f"author:{extraction['metadata']['author'].lower().replace(' ', '-')}"
    data["relationships"].append(
        {
            "id": f"rel:{existing_rels + 1}",
            "type": "written_by",
            "from": extraction["article_id"],
            "to": author_id,
        }
    )

    save_json(relationships_path, data)


def update_manifest(manifest_path: Path, extraction: dict):
    """Update manifest.json stats."""
    data = load_json(manifest_path)

    if "stats" in data:
        # Increment article count
        data["stats"]["articles"] = data["stats"].get("articles", 0) + 1
        data["stats"]["lastUpdated"] = date.today().isoformat()

        # Add new concepts count
        new_concepts = len(extraction.get("new_concepts", []))
        if new_concepts > 0:
            data["stats"]["concepts"] = data["stats"].get("concepts", 0) + new_concepts

    save_json(manifest_path, data)


def main():
    parser = argparse.ArgumentParser(description="Generate files from extraction")
    parser.add_argument("--extraction", required=True, help="Path to extraction JSON")
    args = parser.parse_args()

    extraction = load_extraction(args.extraction)
    base_path = Path("kg-learning")

    # 1. Generate article markdown
    article_path = base_path / "sources" / "articles" / f"{extraction['slug']}.md"
    article_path.parent.mkdir(parents=True, exist_ok=True)
    article_path.write_text(generate_article_markdown(extraction))
    print(f"Created: {article_path}")

    # 2. Generate new concept files
    for concept in extraction.get("new_concepts", []):
        concept_path = base_path / "concepts" / f"{concept['id']}.md"
        concept_path.write_text(generate_concept_markdown(concept))
        print(f"Created: {concept_path}")

    # 3. Update entities.json
    entities_path = base_path / "graph" / "entities.json"
    update_entities(entities_path, extraction)
    print(f"Updated: {entities_path}")

    # 4. Update relationships.json
    relationships_path = base_path / "graph" / "relationships.json"
    update_relationships(relationships_path, extraction)
    print(f"Updated: {relationships_path}")

    # 5. Update manifest.json
    manifest_path = base_path / "manifest.json"
    update_manifest(manifest_path, extraction)
    print(f"Updated: {manifest_path}")

    print("\nFile generation complete!")


if __name__ == "__main__":
    main()
