import streamlit as st
import operations_seller.crud_operations as CRUD
import operations_seller.view_cards as CARDS
from st_connection_load import st_conn

_conn = st_conn.session

seller_operations_dict = {"CRUD": "Create, Read, Update, Delete",
                          "Product Cards": "View Product & Information",
                          "Inventory Reports": "Custom Seller Reports"
                          }


def seller_operations_selection():
    operation_choice = st.sidebar.selectbox("Select Seller Operation:", seller_operations_dict.keys())
    return operation_choice


def seller_operations():
    selection = seller_operations_selection()

    if selection == "CRUD":
        CRUD.crud_operations_func()
    elif selection == "Product Cards":
        CARDS.load_cards()
    elif selection == "Inventory Reports":
        pass


seller_operations()
