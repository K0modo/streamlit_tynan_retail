import streamlit as st
from sqlalchemy import delete
from db_models import BusinessLine, ProductCategory, ProductInventory


def delete_records_from_table(st_conn):
    table_data = st.radio("Select table to add data:",
                          options=["Business Line",
                                   "Product Category",
                                   "Product Inventory"]
                          )
    if table_data == "Business Line":
        with st.form("Delete Record from Business Line", clear_on_submit=True):
            record_input = st.text_input("Enter line_id code : ")
            delete_stmt = (delete(BusinessLine)
                           .where(BusinessLine.line_id.in_([record_input]))
                           )
            if st.form_submit_button("Submit"):
                with st_conn.session as session:
                    session.execute(delete_stmt)
                    session.commit()
    elif table_data == "Product Category":
        with st.form("Delete Record from Product Category", clear_on_submit=True):
            st.write("If prod_cat column in Table is blank, click 'Submit' button.")
            record_input = st.text_input("prod_cat code : ")
            delete_stmt = (delete(ProductCategory)
                           .where(ProductCategory.prod_cat.in_([record_input]))
                           )
            if st.form_submit_button("Submit"):
                with st_conn.session as session:
                    session.execute(delete_stmt)
                    session.commit()
    elif table_data == "Product Inventory":
        with st.form("Delete Record from Product Inventory", clear_on_submit=True):
            st.write("If prod_id column in Table is blank, click 'Submit' button.")
            record_input = st.text_input("prod_cat code : ")
            delete_stmt = (delete(ProductInventory)
                           .where(ProductInventory.prod_id.in_([record_input]))
                           )
            if st.form_submit_button("Submit"):
                with st_conn.session as session:
                    session.execute(delete_stmt)
                    session.commit()

#