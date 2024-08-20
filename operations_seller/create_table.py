import streamlit as st
from db_models import Base

def create_model_tables(st_conn):
    st.write("Update Base Models")
    Base.metadata.create_all(st_conn.connect())
    st.write("Tables have been created")