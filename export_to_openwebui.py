import json
from pathlib import Path

presets_dir = Path("D:/OneDrive/Development/lm-studio-presets/presets")
output_prompts_file = Path("D:/OneDrive/Development/lm-studio-presets/openwebui_prompts_export.json")
output_models_file = Path("D:/OneDrive/Development/lm-studio-presets/openwebui_models_export.json")

prompts_list = []
models_list = []

command_map = {
    "Gymnasium Oberstufe.preset.json": "/oberstufe",
    "Oberstufe - Text Veredelung.preset.json": "/veredelung",
    "Oberstufe - Eroerterung.preset.json": "/eroerterung",
    "Oberstufe - Tutor und Korrektor.preset.json": "/korrektur",
    "Verbesserter Essay Stil.preset.json": "/essay",
    "Menschlich & Natürlich.preset.json": "/menschlich",
    "Businesss und Marketing Stil.preset.json": "/business",
    "Business & Marketing E-Mail.preset.json": "/email",
    "Kreatives Schreiben.preset.json": "/kreativ",
    "Creative-Writing.preset.json": "/story"
}

for json_file in sorted(presets_dir.glob("*.json")):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    name = data.get("name", json_file.stem.replace(".preset", ""))
    system_prompt = ""
    temp = 0.7
    top_p = 0.9
    repeat_penalty = 1.05
    
    fields = data.get("operation", {}).get("fields", [])
    for field in fields:
        k = field.get("key", "")
        v = field.get("value")
        if k == "llm.prediction.systemPrompt":
            system_prompt = v
        elif k == "llm.prediction.temperature":
            temp = float(v)
        elif k == "llm.prediction.topPSampling":
            top_p = float(v.get("value", 0.9) if isinstance(v, dict) else v)
        elif k == "llm.prediction.repeatPenalty":
            repeat_penalty = float(v.get("value", 1.05) if isinstance(v, dict) else v)
            
    if not system_prompt:
        continue
        
    cmd = command_map.get(json_file.name, "/" + json_file.stem.lower().replace(" ", "-").replace(".preset", ""))
    
    # 1. Open WebUI Prompt Format
    prompt_entry = {
        "command": cmd,
        "title": name,
        "content": system_prompt
    }
    prompts_list.append(prompt_entry)
    
    # 2. Open WebUI Custom Model Template Format
    model_id = cmd.replace("/", "")
    model_entry = {
        "id": model_id,
        "name": name,
        "meta": {
            "description": f"Preset: {name} (Anti-KI / Hohe Qualität)",
            "profile_image_url": "/static/favicon.png",
            "capabilities": {
                "vision": True,
                "usage": True
            }
        },
        "params": {
            "system": system_prompt,
            "temperature": temp,
            "top_p": top_p,
            "frequency_penalty": repeat_penalty - 1.0 if repeat_penalty > 1.0 else 0.0
        }
    }
    models_list.append(model_entry)

with open(output_prompts_file, "w", encoding="utf-8") as f:
    json.dump(prompts_list, f, ensure_ascii=False, indent=2)

with open(output_models_file, "w", encoding="utf-8") as f:
    json.dump(models_list, f, ensure_ascii=False, indent=2)

print(f"Exported {len(prompts_list)} prompts to {output_prompts_file.name}")
print(f"Exported {len(models_list)} models to {output_models_file.name}")
