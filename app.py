import streamlit as st
from app_login import app_login_func


from pages.seller_page import seller_operations

def main():
    st.markdown("<h2 style='text-align: center'>Tynan Retail Store</h2", unsafe_allow_html=True)
    # app_login_func()
    seller_operations()


if __name__ == "__main__":
    main()



