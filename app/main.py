import streamlit as st
from links import FROH, TRAURIG

st.title("Hallo👋")

st.markdown(
    """ 
     

    **zu unserem :rainbow[Zufallsgenerator]!**
    
    
    """
)

zeige_ballons = st.button("Send balloons!")
if zeige_ballons:
   st.balloons()

alle_namen = []
neuer_name = st.text_input("Bitte gebe einen Namen ein")
alle_namen.append(neuer_name)
st.write(neuer_name)
users = st.multiselect("Personen", alle_namen)
rolling_average = st.toggle("Rolling average")
