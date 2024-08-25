import streamlit as st
from db_models import Base


def permission_warning():
    return st.markdown(":orange[See Database Administrator for assistance]")


def create_model_tables():
    col = st.columns((1,8,1))
    with col[1]:
        st.write("")
        st.write("You elected to Update Base Models")
        permission_warning()
        # Base.metadata.create_all(st_conn.connect())
        # st.write("Tables have been created")