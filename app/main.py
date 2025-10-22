import streamlit as st
from links import FROH, TRAURIG
import random
import pandas as pd
state = st.session_state
if "alle_namen" not in state:
   state["alle_namen"] = []

st.title(":rainbow[Zufallsgenerator]")

st.markdown("um Gruppen in der Klasse zu generieren")

zeige_ballons = st.button("Ballons")
if zeige_ballons:
   st.balloons()

state["klasse"] = st.toggle("Klasse 8c")


if state["klasse"]:
   state["alle_namen"] = [
      "Lutz", "Olivia", "Clementine", "Frederick", "Elias", "Finja", "Vincent", "Lukas", "Luisa", "Lara",
      "Hilde", "Frida", "Arthur", "Konstantin", "Adrian", "Anton", "Amelie", "Mariia", "Hannes", "Eos", "Oda", "Thekla", "Klee", "Lena", "Benjamin" ,"Bela"
   ]
else:
   state["alle_namen"] = []  


neuer_name = st.text_input("Bitte gebe einen Namen ein", value="")
if neuer_name != "" and neuer_name not in state["alle_namen"]:
    state["alle_namen"].append(neuer_name)

state["alle_namen"] = st.multiselect("Personen", state["alle_namen"], state["alle_namen"])

Auswahl = st.selectbox(
   "Möchtest du die anzahl an Personen oder Gruppen bestimmen?"
   ,("Personen", "Gruppen")
)


if Auswahl == "Personen":
   gruppen_größe = st.selectbox(
    "Wie viele Personen sollen in einer Gruppe sein",
    (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
   )
   personen_auswahl = st.button("Gruppenzuweisung")
   if personen_auswahl:
      #persons = numpy.random.choice(state["alle_namen"],size = option,replace = False)
      #st.write(persons)
      mögliche_personen = list(state["alle_namen"])
      gruppen = []
      nächste_gruppe = []
      while len(mögliche_personen) > 0:
         person = random.choice(mögliche_personen)
         mögliche_personen.remove(person)
         nächste_gruppe.append(person)
         if len(nächste_gruppe) == gruppen_größe:
            gruppen.append(nächste_gruppe)
            nächste_gruppe = []
      
      restpersonen = nächste_gruppe

      if len(restpersonen) > 0:
         gruppen_id = 0
         for person in list(restpersonen):
            gruppe = gruppen[gruppen_id]
            gruppe.append(person)
            nächste_gruppe.remove(person)
            gruppen_id += 1
            if gruppen_id >= len(gruppen):
               gruppen_id = 0

               max_personen = max(len(gruppe) for gruppe in gruppen) if gruppen else 0

      

      df = pd.DataFrame(
         gruppen, 
         index=[f"Gruppe {i+1}" for i in range(len(gruppen))],
         columns=[f"Person {i+1}" for i in range(len(gruppen[0]))]
      )
      st.dataframe(df.T)


if Auswahl == "Gruppen":
   anzahl_gruppen = st.selectbox(
    "Wie viele Gruppen soll es geben",
    (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
   )

   gruppen_auswahl = st.button("Gruppenzuweisung")
   if gruppen_auswahl:
      mögliche_personen = list(state["alle_namen"])
      gruppen = [[] for _ in range(anzahl_gruppen)]
      gruppen_nr = 0
      nächste_gruppe = gruppen[gruppen_nr]
      while len(mögliche_personen) > 0:
         person = random.choice(mögliche_personen)
         mögliche_personen.remove(person)
         nächste_gruppe.append(person)
         gruppen_nr += 1
         if gruppen_nr >= len(gruppen):
            gruppen_nr = 0
         nächste_gruppe = gruppen[gruppen_nr]
      
      # restpersonen = nächste_gruppe

      # if len(restpersonen) > 0:
      #    gruppen_id = 0
      #    for person in list(restpersonen):
      #       gruppe = gruppen[gruppen_id]
      #       gruppe.append(person)
      #       nächste_gruppe.remove(person)
      #       gruppen_id += 1
      #       if gruppen_id >= len(gruppen):
      #          gruppen_id = 0

      max_personen = max(len(gruppe) for gruppe in gruppen) if gruppen else 0


      df = pd.DataFrame(
         gruppen, 
         index=[f"Gruppe {i+1}" for i in range(len(gruppen))],
         columns=[f"Person {i+1}" for i in range(max_personen)]
      )
      st.dataframe(df.T)


