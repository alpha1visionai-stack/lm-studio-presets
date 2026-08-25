import os
import json
import time
import uuid
from pathlib import Path

# Paths to search for skills
skill_paths = [
    Path("C:/Users/walte/.agents/skills/der-rat/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/expert-council/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/brainstorming/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/prd/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/lead-research-assistant/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/meeting-insights-analyzer/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/doc-coauthoring/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/documentation-writer/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/enhance-prompt/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/karpathy-guidelines/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/site-builder/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/frontend-design/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/shadcn-ui/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/taste-design/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/alpha-inspiration-design/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/n8n-workflow-patterns/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/n8n-code-javascript/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/n8n-code-python/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/n8n-expression-syntax/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/n8n-validation-expert/SKILL.md"),
    Path("C:/Users/walte/.gemini/config/skills/chat-knowledge-manager/SKILL.md"),
    Path("C:/Users/walte/.gemini/config/skills/tax-automation-consultant/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/fast-detect-gpt/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/human-text-presets/SKILL.md"),
]

skills_data = []

for p in skill_paths:
    if not p.exists():
        continue
    skill_id = p.parent.name
    with open(p, "r", encoding="utf-8") as f:
        raw_text = f.read()
        
    name = skill_id
    description = ""
    content = raw_text
    
    if raw_text.startswith("---"):
        parts = raw_text.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            content = parts[2].strip()
            
            # Simple frontmatter parser
            for line in fm.strip().split("\n"):
                if line.startswith("name:"):
                    name = line.replace("name:", "").strip().strip("\"'")
                elif line.startswith("description:"):
                    description = line.replace("description:", "").strip().strip("\"'")
                    
    if not description:
        description = f"Skill: {name}"
        
    skills_data.append({
        "id": skill_id,
        "name": name,
        "description": description,
        "content": content
    })

print(f"Prepared {len(skills_data)} skills for Open WebUI.")

# Save local JSON export
output_json = Path("D:/OneDrive/Development/lm-studio-presets/openwebui_skills_export.json")
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(skills_data, f, ensure_ascii=False, indent=2)

print(f"Saved export to {output_json}")
