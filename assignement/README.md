# Setup-Anleitung für die Nutzung des Notebooks mit dem Agenten

Um dieses Assignment-Notebook mit dem Agenten aus dem `toolagentlab`-Repo zu nutzen, folge diesen Schritten:

1. **Repos klonen**
   - Klone sowohl dieses Assignment-Repo als auch das `toolagentlab`-Repo (beide sollten im gleichen Verzeichnis liegen oder passe den Pfad entsprechend an).

2. **Virtuelle Umgebung erstellen & aktivieren**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt  # oder: pip install -r pyproject.toml
   pip install notebook ipykernel python-dotenv
   ```

4. **Agent als editierbares Paket installieren**
   ```bash
   pip install -e ../toolagentlab
   ```
   Passe den Pfad ggf. an, falls sich das `toolagentlab`-Repo an einem anderen Ort befindet.

5. **Jupyter starten & Kernel auswählen**
   - Starte Jupyter Notebook oder öffne das Notebook in VS Code.
   - Wähle das Python-Environment aus Schritt 2 als Kernel aus.

6. **Notebook ausführen**
   - Jetzt kannst du den Agenten direkt mit `from agent.agent import Agent` importieren und nutzen.

**Hinweis:**
- Änderungen am Agenten im `toolagentlab`-Repo werden sofort übernommen, da das Paket im editierbaren Modus installiert ist.
- Bei Problemen prüfe die Environment-Auswahl und installiere ggf. fehlende Pakete.

# Hinweise zur Nutzung und Features

- Die Agenten-Logik und alle Tools befinden sich im Verzeichnis `../toolagentlab`.
- Die System-Prompt und alle verfügbaren Tools sind in `../toolagentlab/docs/system_prompt.txt` dokumentiert.
- Plots und Visualisierungen werden automatisch im Ordner `../toolagentlab/output/plot/` gespeichert.
- Jeder Agenten-Dialog (Message-History) wird automatisch in `../toolagentlab/docs/log/` als `log<N>.txt` gespeichert.
- Die System-Prompt wird dem LLM bei jedem Durchlauf als Kontext mitgegeben (siehe Code in `agent/agent.py`).
- Die 3D-Plots unterstützen Vektor-Overlays für Lösungsschritte (siehe Beispiel in der System-Prompt).

# Beispiel für die Nutzung im Notebook

```python
from agent.agent import Agent
agent = Agent()
query = "Was ist die Ableitung von x**2 + y**2 nach x an der Stelle x=2, y=3? Bitte zeige auch die Plots."
result = agent(query)
print(result)
```

# Troubleshooting
- Falls Plots nicht angezeigt werden, prüfe den Ordner `../toolagentlab/output/plot/`.
- Bei Fehlern im Agentenlauf siehe die Logdateien in `../toolagentlab/docs/log/`.
- Debug-Ausgaben wurden entfernt, sodass die Ausgabe jetzt nur noch relevante Informationen enthält.

# Autoren & Support
- Für Fragen oder Probleme: Siehe README im `toolagentlab`-Repo oder öffne ein Issue.
