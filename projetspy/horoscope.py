import os
import json
import random
import streamlit as st

st.set_page_config(
    page_title="🔮 Horoscope du jour 🔮",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("🔮 Horscope 🔮")

st.markdown("""
<style>    
.stApp { background: #d85cd9b5;}
.stSidebar { background: #d85cd9b5;} 
.stTextInput > div > div > input {
    background: #e09be0b5 !important;
    color: white !important;
    border: 2px solid white;
    padding: 12px;}       
</style>
""", unsafe_allow_html=True)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "h.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    horoscope = json.load(f)

@st.cache_data(ttl=1)  #Cache=1 seconde.
def get_horoscope(signe):
    return random.choice(horoscope[signe])

signe = st.text_input("Quel est ton signe astro ?")

if signe:
    if signe in horoscope:
        horoscope_du_jour = random.choice(horoscope[signe])
        st.success(f"✨ Ton horoscope pour **{signe}** : {horoscope_du_jour}")
    else:
        st.warning("❌ Signe non reconnu, vérifie l'orthographe :)")

