# 🎛️ LM Studio Presets Collection

Eine kuratierte Sammlung optimierter **System-Prompt & Inferenz-Presets für [LM Studio](https://lmstudio.ai/)**.  
Speziell abgestimmt auf **akademisches Schreiben (Gymnasium Oberstufe / Abitur), Anti-KI-Slop ("Menschlich & Natürlich") und Kreatives Schreiben / Worldbuilding**.

---

## 📋 Enthaltene Presets

| Preset-Name | Dateiname | Kernfunktion & Tonalität | Empfohlene Modelle |
| :--- | :--- | :--- | :--- |
| **🎓 Gymnasium Oberstufe (Abitur & Facharbeit)** | `Gymnasium Oberstufe.preset.json` | Gehobenes Bildungsdeutsch, KMK-Operatoren, textbezogene Analysen (Sachtext, Epik, Drama, Geschichte, Ethik). | `SauerkrautLM-Nemo-12B`, `Llama-3.1-SauerkrautLM-8B` |
| **⚡ Oberstufe: Text-Veredelung** | `Oberstufe - Text Veredelung.preset.json` | Direkte stilistische Veredelung ohne Vorab-Gelaber. Schreibt Rohtexte sofort in fehlerfreies Bildungsdeutsch um. | `Llama-3.1-SauerkrautLM-8B`, `SauerkrautLM-Nemo-12B` |
| **⚖️ Oberstufe: Erörterung & Argumentation** | `Oberstufe - Eroerterung.preset.json` | Strikte These-Begründung-Beleg Struktur, dialektische & lineare Erörterungen, reflektierte Synthesen. | `DeepSeek-R1-Distill-Qwen-14B`, `SauerkrautLM-Nemo-12B` |
| **👨‍🏫 Oberstufe: Tutor & Fachlehrer-Feedback** | `Oberstufe - Tutor und Korrektor.preset.json` | Didaktische Korrektur: Erkennt Umgangssprache, Argumentationslücken und liefert 3 konkrete Formulierungsvorschläge + Noteneinschätzung. | `SauerkrautLM-Nemo-12B`, `DeepSeek-R1-Distill-Qwen-14B` |
| **🛡️ Menschlich & Natürlich (Anti-KI)** | `Menschlich & Natuerlich.preset.json` | Bricht typische KI-Floskeln ("AI-Slop") und Bulletpoint-Wüsten. Hohe Satzrhythmus-Varianz (Burstiness), lebendige Prosa. | `Mistral-7B-Instruct`, `MistThena7BV2`, `Qwen2.5-7B/14B` |
| **📖 Kreatives Schreiben (Prosa & Dialoge)** | `Kreatives Schreiben.preset.json` | Atmosphärische Dichte, Show-don't-tell, facettenreiche Dialoge und Genre-Flexibilität (Noir, Sci-Fi, Fantasy). | `MistThena7BV2`, `Mistral-7B-Instruct-v0.3-emotional` |
| **✍️ Creative Writing (Mistral / MistThena)** | `Creative-Writing.preset.json` | Universelle Inferenz-Parameter (Temp 0.8, Repeat Penalty 1.12) für kreative Rollenspiele und Storytelling. | `MistThena7BV2`, `Mistral-7B` |

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
│ 📖 Erzählungen & Dialoge     │ 🎭 MistThena7B / Mistral     │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 📄 Lizenz
MIT License — Frei verwendbar, anpassbar und erweiterbar.
