import os
import re
from pathlib import Path

skills_root = Path("C:/Users/walte/.agents/skills")
selected_skills = [
    "der-rat",
    "expert-council",
    "brainstorming",
    "prd",
    "lead-research-assistant",
    "meeting-insights-analyzer",
    "doc-coauthoring",
    "documentation-writer",
    "enhance-prompt",
    "karpathy-guidelines",
    "site-builder",
    "frontend-design",
    "shadcn-ui",
    "n8n-workflow-patterns",
    "n8n-code-javascript",
    "n8n-code-python",
    "n8n-expression-syntax",
    "n8n-validation-expert",
    "fast-detect-gpt"
]

results = []
for s in selected_skills:
    skill_file = skills_root / s / "SKILL.md"
    if not skill_file.exists():
        continue
    with open(skill_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Parse YAML frontmatter
    name = s
    desc = ""
    content = text
    
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            content = parts[2].strip()
            for line in fm.split("\n"):
                if line.startswith("name:"):
                    name = line.replace("name:", "").strip()
                elif line.startswith("description:"):
                    desc = line.replace("description:", "").strip()
    
    results.append({
        "id": s,
        "name": name if name else s,
        "description": desc,
        "content_len": len(content)
    })

print(f"Found {len(results)} valid skills to transfer:")
for r in results:
    print(f" • [{r['id']}] {r['name']} ({r['content_len']} chars) -> {r['description'][:70]}...")
