import sys
try:
    import open_webui
    print("Open WebUI imported!")
except Exception as e:
    print(f"Error importing open_webui: {e}")

try:
    from open_webui.models.skills import Skills, SkillForm, SkillModel
    print("Skills model found!")
    skills = Skills.get_skills()
    print(f"Skills count: {len(skills)}")
except Exception as e:
    print(f"Error checking skills model: {e}")
