import streamlit as st
from links import FROH, TRAURIG

state = st.session_state
if "alle_namen" not in state:
   state["alle_namen"] = []


st.title("Hallo👋")

st.markdown(
    """ 
    **zu unserem :rainbow[Zufallsgenerator]!**
    """
)

zeige_ballons = st.button("Send balloons!")
if zeige_ballons:
   st.balloons()

neuer_name = st.text_input("Bitte gebe einen Namen ein", value=None)
if neuer_name is not None and neuer_name not in state["alle_namen"]:
    state["alle_namen"].append(neuer_name)

st.write(state["alle_namen"])
users = st.multiselect("Personen", state["alle_namen"], state["alle_namen"])
rolling_average = st.toggle("Rolling average")

import streamlit as st

option = st.selectbox(
    "Wie viele Personen sollen in einer Gruppe sein",
    ("2", "3", "4", "5", "6"),
)
