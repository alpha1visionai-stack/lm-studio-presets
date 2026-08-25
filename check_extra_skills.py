from pathlib import Path

extra_skills = [
    Path("C:/Users/walte/.gemini/config/skills/tax-automation-consultant/SKILL.md"),
    Path("C:/Users/walte/.gemini/config/skills/chat-knowledge-manager/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/alpha-inspiration-design/SKILL.md"),
    Path("C:/Users/walte/.agents/skills/taste-design/SKILL.md")
]

for p in extra_skills:
    if p.exists():
        print("Found extra skill:", p.parent.name)
