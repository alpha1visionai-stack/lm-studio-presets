# 🎛️ LM Studio Presets Collection

Eine kuratierte Sammlung optimierter **System-Prompt & Inferenz-Presets für [LM Studio](https://lmstudio.ai/)**.  
Speziell abgestimmt auf **akademisches Schreiben (Gymnasium Oberstufe / Abitur), Anti-KI-Slop ("Menschlich & Natürlich"), Business- & B2B-Marketing sowie Kreatives Schreiben**.

---

## 📋 Enthaltene Presets (10 Presets)

| Preset-Name | Dateiname | Kernfunktion & Tonalität | Empfohlene Modelle |
| :--- | :--- | :--- | :--- |
| **🎓 Gymnasium Oberstufe (Allgemein)** | `Gymnasium Oberstufe.preset.json` | Gehobenes Bildungsdeutsch, KMK-Operatoren, textbezogene Analysen (Sachtext, Epik, Drama, Geschichte, Ethik). | `SauerkrautLM-Nemo-12B`, `Llama-3.1-SauerkrautLM-8B` |
| **⚡ Oberstufe: Text-Veredelung** | `Oberstufe - Text Veredelung.preset.json` | Direkte stilistische Veredelung ohne Vorab-Gelaber. Schreibt Rohtexte sofort in fehlerfreies Bildungsdeutsch mit starken Verben um. | `Llama-3.1-SauerkrautLM-8B`, `SauerkrautLM-Nemo-12B` |
| **⚖️ Oberstufe: Erörterung & Argumentation** | `Oberstufe - Eroerterung.preset.json` | Dialektische & lineare Erörterungen, Kriterien-Hierarchie in der Synthese, Entschlackung von Konnektoren-Slop. | `DeepSeek-R1-Distill-Qwen-14B`, `SauerkrautLM-Nemo-12B` |
| **👨‍🏫 Oberstufe: Tutor & Fachlehrer-Gutachten** | `Oberstufe - Tutor und Korrektor.preset.json` | Amtliches Fachleiter-Gutachten: Diagnostiziert Sprache/Inhalt, liefert 3 konkrete Satz-Veredelungen + KMK-Notenfindung (0–15 Punkte). | `SauerkrautLM-Nemo-12B`, `DeepSeek-R1-Distill-Qwen-14B` |
| **✒️ Verbesserter Essay-Stil** | `Verbesserter Essay Stil.preset.json` | Radikale Satzlängen-Asymmetrie, Vermeidung von Bandwurmsätzen und Stakkato, spürbare Autorenhaltung. | `SauerkrautLM-Nemo-12B`, `Qwen2.5-14B/32B` |
| **🛡️ Menschlich & Natürlich (Master Anti-KI)** | `Menschlich & Natürlich.preset.json` | Bricht typische KI-Floskeln ("AI-Slop") und Bulletpoint-Wüsten. Hohe Satzrhythmus-Varianz (Burstiness), lebendige Prosa. | `Mistral-7B-Instruct`, `MistThena7BV2`, `Qwen2.5-7B/14B` |
| **💼 Business & Marketing Stil** | `Businesss und Marketing Stil.preset.json` | Executive Tone für C-Level/Entscheider: Null-Toleranz für Corporate-Bullshit, direkte Mechanik & messbarer ROI. | `Qwen2.5-14B/32B`, `SauerkrautLM-Nemo-12B` |
| **📧 Business & Marketing E-Mail** | `Business & Marketing E-Mail.preset.json` | High-Conversion B2B/B2C E-Mails, 3 Betreffzeilen, Pattern-Interrupt Hooks, Low-Friction CTAs, kein Spam/Jargon. | `Qwen2.5-14B/32B`, `SauerkrautLM-Nemo-12B`, `Mistral-Small` |
| **📖 Kreatives Schreiben (Prosa & Dialoge)** | `Kreatives Schreiben.preset.json` | Atmosphärische Dichte, Show-don't-tell, facettenreiche Dialoge und Genre-Flexibilität (Noir, Sci-Fi, Fantasy). | `MistThena7BV2`, `Mistral-7B-Instruct-v0.3-emotional` |
| **✍️ Creative Writing (Inferenz-Setup)** | `Creative-Writing.preset.json` | Universelle Inferenz-Parameter (Temp 0.8, Repeat Penalty 1.12) für kreative Rollenspiele und Storytelling. | `MistThena7BV2`, `Mistral-7B` |

---

## 🚀 Installation & Einrichten

### Option 1: 1-Klick-Installation (Windows PowerShell)
Öffne PowerShell im Repository-Ordner und führe aus:
```powershell
.\install.ps1
```

### Option 2: 1-Klick-Installation (Python – Windows / macOS / Linux)
```bash
python install.py
```

### Option 3: Manuelle Installation
Kopiere alle `.json`-Dateien aus dem Ordner `presets/` in das Konfigurationsverzeichnis von LM Studio:
* **Windows:** `C:\Users\<DeinBenutzer>\.lmstudio\config-presets\`
* **macOS / Linux:** `~/.lmstudio/config-presets/`

Starte danach LM Studio neu oder wähle die Presets direkt in der rechten Seitenleiste aus.

---

## 🎯 Empfohlene Modell-Kombinationen

```text
┌─────────────────────────────────────────────────────────────┐
│                      LM STUDIO PRESETS                      │
├──────────────────────────────┬──────────────────────────────┤
│ 🎓 Oberstufen-Aufgaben       │ ⚡ SauerkrautLM-8B / Nemo-12B │
│ 🧠 Mathe, Logik, Klausur     │ 🧠 DeepSeek-R1-Distill-14B   │
│ 🛡️ Natürliche Blogtexte      │ 🍃 Mistral-7B / Qwen-2.5     │
│ 💼 B2B & Marketing Texte     │ 🎯 Qwen-2.5-14B / Sauerkraut │
│ 📖 Erzählungen & Dialoge     │ 🎭 MistThena7B / Mistral     │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 🌐 Open WebUI & OpenRouter Integration

Die Presets können direkt in **Open WebUI** (z. B. auf einem Server oder Docker-Container) genutzt werden:

1. **Prompt-Import:** Importiere `openwebui_prompts_export.json` unter **Workspace $\rightarrow$ Prompts $\rightarrow$ Import Prompts**.
2. **Slash-Befehle im Chat:** Nutze `/menschlich`, `/business`, `/email`, `/oberstufe`, `/eroerterung`, `/veredelung`, `/korrektur`, `/essay`, `/kreativ`, `/story`.
3. **Modell-Empfehlungen für OpenRouter:** Siehe ausführlichen Leitfaden in [`OPENROUTER_MODELS.md`](OPENROUTER_MODELS.md).

---

## 📄 Lizenz
MIT License — Frei verwendbar, anpassbar und erweiterbar.
