import streamlit as st

def main_container_title():
    st.markdown("""
            <style>
                   .block-container {
                        padding-top: 2em;
                        padding-bottom: 0rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
            </style>
            """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center'>Tynan Retail Store</h2", unsafe_allow_html=True)
