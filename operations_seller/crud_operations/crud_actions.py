import streamlit as st


crud_actions = [
    "Home",
    "Create Records",
    "Read Records",
    "Update Records",
    "Delete Records",
    "Create Tables",

]

def crud_actions_selectbox():
    action = st.sidebar.selectbox("Select CRUD Operations", crud_actions)
    return action