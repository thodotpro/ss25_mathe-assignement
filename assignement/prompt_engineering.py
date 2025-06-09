# Patch sys.path to ensure toolagentlab is importable if editable install is not picked up
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../toolagentlab')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure .env is loaded for GOOGLE_API_KEY
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Change working directory so relative paths in toolagentlab work
os.chdir(os.path.join(os.path.dirname(__file__), '../toolagentlab'))

from toolagentlab.agent.agent import Agent

query = """
Sei S die Fläche, die der Graph der Funktion 𝑓(𝑥, 𝑦) = 10 − 𝑥
2 − 𝑦
2
ist. Nehmen Sie an, dass die
Temperatur im Raum in jedem Punkt (𝑥, 𝑦, 𝑧) durch 𝑇(𝑥, 𝑦, 𝑧) = 𝑥
2𝑦 + 𝑦
2𝑥 + 4𝑥 + 14𝑦 + 𝑧
gegeben ist. 

Aufgabenstellung für KI
▪ visuelle Darstellung der Angabe
▪ Wahl der Richtung, die im Punkt (0,0,10) tangential an die Fläche S ist und bei der die
Änderungsrate im Punkt (0,0,10) maximal ist.
(mit Schritt-für-Schritt-Darstellung für die Bestimmung der Richtung)
▪ Bestimmung der Richtung, die im Punkt (0,0,8) tangential an die Fläche S ist und deren
Änderungsrate maximal ist
▪ visuelle Darstellung der Lösung
"""

agent = Agent()
result = agent(query)
print(result)