import streamlit as st
from db_models import BusinessLine, ProductCategory, ProductInventory
from sqlalchemy import select


available_tables = ["Business Line",
                    "Product Category",
                    "Product Inventory",
                    "Product Dimensions",
                    "Product Business Line"]


def view_tables(session):

    table = st.radio("Select table to view:", available_tables)
    if table == "Business Line":
        st.subheader("Business Line Table")
        with session as session:
            result = session.execute(select(BusinessLine.line_id,
                                            BusinessLine.line_name)
                                     )
            st.dataframe(result, hide_index=True)
    elif table == "Product Inventory":
        st.subheader("Product Inventory")
        with session as session:
            result = session.execute(select(ProductInventory.prod_id,
                                            ProductInventory.prod_name,
                                            ProductInventory.prod_price,
                                            ProductInventory.prod_photo,
                                            ProductInventory.line_id,
                                            ProductInventory.prod_cat)
                                     )
            st.dataframe(result, hide_index=True)
    elif table == "Product Dimensions":
        st.subheader("Product Dimensions")
        with session as session:
            result = session.execute(select(ProductInventory.prod_id,
                                            ProductInventory.prod_name,
                                            ProductInventory.prod_width,
                                            ProductInventory.prod_height,
                                            ProductInventory.prod_depth)
                                     )
            st.dataframe(result, hide_index=True)
    elif table == "Product Category":
        st.subheader("Product Category")
        with session as session:
            result = session.execute(select(ProductCategory.prod_cat,
                                            ProductCategory.cat_name,
                                            ProductCategory.line_id)
                                     )
            st.dataframe(result, hide_index=True)
    elif table == "Product Business Line":
        st.subheader("Product with Business Line Name")
        with session as session:
            result = session.execute(select(ProductInventory.prod_id,
                                            ProductInventory.prod_name,
                                            ProductInventory.line_id,
                                            BusinessLine.line_name)
                                     .join(BusinessLine)
                                     )
            st.dataframe(result, hide_index=True)
