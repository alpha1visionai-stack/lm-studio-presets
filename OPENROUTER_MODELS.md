# 🌐 OpenRouter & Open WebUI Modell-Empfehlungen für Presets

Diese Dokumentation beschreibt die besten Modelle auf **[OpenRouter](https://openrouter.ai/)** zur Verwendung mit den Presets dieser Sammlung in **[Open WebUI](https://github.com/open-webui/open-webui)** oder jedem OpenAI-kompatiblen Frontend.

---

## 🏆 Top-Modelle nach Einsatzbereich

| Einsatzbereich / Presets | Erstwahl (Beste Qualität) | Preis-Leistungs-Tipp |
|---|---|---|
| 🛡️ **Master Anti-KI & Essay**<br>`/menschlich`, `/essay` | **Claude 3.5 Sonnet / 3.7 Sonnet**<br>`anthropic/claude-3.5-sonnet` | **Qwen 2.5 72B Instruct**<br>`qwen/qwen-2.5-72b-instruct` |
| 🎓 **Gymnasiale Oberstufe & Abitur**<br>`/oberstufe`, `/veredelung` | **Claude 3.5 Sonnet**<br>`anthropic/claude-3.5-sonnet` | **Llama 3.3 70B Instruct**<br>`meta-llama/llama-3.3-70b-instruct` |
| ⚖️ **Erörterung & Gutachten**<br>`/eroerterung`, `/korrektur` | **DeepSeek R1 (Reasoning)**<br>`deepseek/deepseek-r1` | **DeepSeek V3**<br>`deepseek/deepseek-chat` |
| 💼 **Business & Marketing E-Mail**<br>`/business`, `/email` | **Qwen 2.5 72B Instruct**<br>`qwen/qwen-2.5-72b-instruct` | **Mistral Small 3 (24B)**<br>`mistralai/mistral-small-24b-instruct-2501` |
| 📖 **Kreatives Schreiben & Story**<br>`/kreativ`, `/story` | **Mistral Large 2 (2407)**<br>`mistralai/mistral-large-2407` | **Mistral Nemo / Small**<br>`mistralai/mistral-nemo` |

---

## 🔍 Detaillierte Empfehlungen

### 🥇 1. Claude 3.5 Sonnet / 3.7 Sonnet (`anthropic/claude-3.5-sonnet`)
* **Stärken:** Höchste Differenziertheit im deutschen Sprachraum, subtiles Rhythmusgefühl, elegante Satzstrukturen.
* **Besonderheit:** Absolut führend bei der Einhaltung von Negativlisten (Anti-Slop). Schreibt organisch und unverkennbar menschlich.
* **Beste Einsatzgebiete:** `/menschlich`, `/essay`, `/veredelung`, gymnasiale Facharbeiten und Kolumnen.

### 🥈 2. Qwen 2.5 72B Instruct (`qwen/qwen-2.5-72b-instruct`)
* **Stärken:** Enorme argumentative Härte, zupackende Sprache, exzellente deutsche Syntax bei sehr geringen Inferenzkosten.
* **Besonderheit:** Perfekt für B2B-Texte ohne Weichspüler oder esoterisches Geschwurbel.
* **Beste Einsatzgebiete:** `/business`, `/email`, `/eroerterung`.

### 🧠 3. DeepSeek R1 (`deepseek/deepseek-r1`)
* **Stärken:** Reasoning-Architektur mit internem Denkprozess (Chain-of-Thought).
* **Besonderheit:** Baut logisch zwingende dialektische Argumentationsketten auf (These $\leftrightarrow$ Antithese $\rightarrow$ Synthese mit Kriterien-Hierarchie).
* **Beste Einsatzgebiete:** `/eroerterung` (Abitur-Erörterungen) und `/korrektur` (Didaktische Fehlerdiagnose & Notenfindung).

### 🎭 4. Mistral Large 2 (2407) (`mistralai/mistral-large-2407`)
* **Stärken:** Europäische Sprachgewandtheit, kein steriles Übersetzungs-Deutsch.
* **Besonderheit:** Herausragend bei Show-don't-tell, lebendigen Charakter-Dialogen und atmosphärischer Dichte.
* **Beste Einsatzgebiete:** `/kreativ`, `/story`, Drehbücher und literarische Prosa.

---

## ⚙️ Empfohlene Inferenz-Parameter

```json
{
  "temperature": 0.75,
  "top_p": 0.90,
  "frequency_penalty": 0.08,
  "presence_penalty": 0.05
}
```

---

## ⚡ Schnellstart in Open WebUI

1. Importiere `openwebui_prompts_export.json` unter **Workspace $\rightarrow$ Prompts $\rightarrow$ Import Prompts**.
2. Nutze im Chat einfach die entsprechenden Slash-Befehle (`/menschlich`, `/business`, `/oberstufe` etc.).
