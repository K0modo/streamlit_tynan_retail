import streamlit as st

# @st.cache_resource
# def create_db_connection():
#     return st.connection('db_home_retail', type='sql')

st_conn = st.connection('db_home_retail', type='sql')