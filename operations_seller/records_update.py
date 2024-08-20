import streamlit as st
from db_models import BusinessLine, ProductCategory, ProductInventory
from sqlalchemy import update, select, column

def update_records_table(st_conn):
    table_data = st.radio("Select table with record:",
                          options=["Business Line",
                                   "Product Category",
                                   "Product Inventory"]
                          )
    if table_data == "Business Line":
        with st.form("Update Business Line", clear_on_submit=True):
            target_record = st.text_input("Target line_id to update : ")
            new_record = st.text_input("New line_name : ")
            stmt = (update(BusinessLine)
                    .where(BusinessLine.line_id == target_record)
                    .values(line_name=new_record)
                    )
            if st.form_submit_button("Submit"):
                with st_conn.session as session:
                    session.execute(stmt)
                    session.commit()
    elif table_data == "Product Category":
        with st.form("Update Product Category", clear_on_submit=True):
            target_record = st.text_input("Target prod_cat to update : ")
            new_record = st.text_input("New cat_name : ")
            stmt = (update(ProductCategory)
                    .where(ProductCategory.prod_cat == target_record)
                    .values(cat_name=new_record)
                    )
            if st.form_submit_button("Submit"):
                with st_conn.session as session:
                    session.execute(stmt)
                    session.commit()
    elif table_data == "Product Inventory":
        pass
        # with st.form("Update Product Inventory", clear_on_submit=True):
        #     target_record = st.text_input("Target prod_id to update : ")
        #     new_record = st.text_input("New cat_name : ")
        #     stmt = (update(ProductCategory)
        #             .where(ProductCategory.prod_cat == target_record)
        #             .values(=new_record)
        #             )
        #     if st.form_submit_button("Submit"):
        #         with st_conn.session as session:
        #             session.execute(stmt)
        #             session.commit()

