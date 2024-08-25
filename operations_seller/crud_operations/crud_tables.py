import streamlit as st


crud_dict = {
    "BusinessLine":"Business Line Table",
    "ProductCategory": "Product Category Table",
    "ProductInventory": "Product Inventory Table"
}


def crud_table_radio():
    table_choice = st.radio("Select table:", options=crud_dict.keys())
    return table_choice

