# SS25 Mathe Assignment – ToolAgentLab

Dieses Repository enthält ein vollständiges KI-gestütztes Mathematik-Assignment-Framework bestehend aus zwei Hauptteilen:

- **assignement/**: Aufgabenstellung, Einstiegsskripte und Projektdateien für die konkrete Aufgabenbearbeitung.
- **toolagentlab/**: Modularer Python-Agent (ToolAgentLab) mit flexiblen mathematischen Tools, Logging, Plotting und ReAct-Pattern.

## Projektstruktur

```
ss25_mathe-assignement/
├── assignement/           # Aufgabenstellung, Einstiegsskripte
│   ├── prompt_engineering.py
│   ├── pyproject.toml
│   ├── README.md
│   └── ...
├── toolagentlab/          # Agent, Tools, Tests, Doku, Output
│   ├── agent/             # Agent-Logik
│   ├── docs/              # System-Prompt, Aufgabenstellung, Logfiles
│   ├── output/plot/       # Automatisch generierte Plots
│   ├── test/              # Pytest-Tests für alle Tools und Agenten
│   ├── tools/             # Mathematische Tools (symbolisch, numerisch, Plotting, etc.)
│   ├── README.md
│   └── ...
├── README.md              # (Diese Datei)
└── ...
```

## Features
- **ReAct-Pattern**: Thought → Action → Observation → Answer, Schritt-für-Schritt-Lösung
- **Flexible Tools**: Symbolische & numerische Mathematik, 2D/3D-Plotting, Vektor-Overlays
- **Automatisches Logging**: Jeder Dialog wird in `toolagentlab/docs/log/` gespeichert
- **Plot-Ausgabe**: Plots werden in `toolagentlab/output/plot/` abgelegt
- **System-Prompt**: Alle verfügbaren Tools und Beispiele in `toolagentlab/docs/system_prompt.txt`
- **Tests**: Umfangreiche Pytest-Tests für Agent und Tools

## Schnellstart
1. **Repository klonen**
2. **Virtuelle Umgebung anlegen & aktivieren**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Abhängigkeiten installieren**
   ```bash
   pip install -e toolagentlab
   pip install -r assignement/pyproject.toml
   ```
4. **.env Datei mit Google API Key anlegen**
   ```
   GOOGLE_API_KEY=dein-key-hier
   ```
5. **Skript starten**
   - Skript: `python assignement/prompt_engineering.py`

## Beispiel für Agent-Nutzung
```python
from agent.agent import Agent
agent = Agent()
query = "Was ist die Ableitung von x**2 + y**2 nach x an der Stelle x=2, y=3? Bitte zeige auch die Plots."
result = agent(query)
print(result)
```

## Hinweise
- **Alle Plots** werden automatisch im Ordner `toolagentlab/output/plot/` gespeichert.
- **Jede Konversation** wird als Logfile in `toolagentlab/docs/log/` abgelegt.
- **System-Prompt** und Tool-Beschreibungen siehe `toolagentlab/docs/system_prompt.txt`.
- **Debug-Ausgaben** wurden entfernt, die Ausgabe ist jetzt sauber.

## Autoren & Support
- Thomas Proksch
- Für Fragen oder Beiträge: Issue oder Pull Request auf GitHub.

---

**Viel Erfolg beim Bearbeiten des Assignments!**
