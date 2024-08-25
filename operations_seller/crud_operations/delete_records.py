import streamlit as st
from sqlalchemy import delete
from db_models import BusinessLine, ProductCategory, ProductInventory


def blank_warning():
    return st.markdown(":orange[If 'PRIMARY KEY' in the database table is empty string, click 'Submit' button.]")


class DeleteRecords:
    def __init__(self, session_conn):
        self.session = session_conn

    def delete_records_line(self):
        with st.form("Delete Record from Business Line", clear_on_submit=True):
            blank_warning()
            record_input = st.text_input("Enter line_id code : ")
            delete_stmt = (delete(BusinessLine)
                           .where(BusinessLine.line_id.in_([record_input]))
                           )
            if st.form_submit_button("Submit"):
                with self.session as session:
                    session.execute(delete_stmt)
                    session.commit()

    def delete_records_category(self):
        with st.form("Delete Record from Product Category", clear_on_submit=True):
            blank_warning()
            record_input = st.text_input("prod_cat code : ")
            delete_stmt = (delete(ProductCategory)
                           .where(ProductCategory.prod_cat.in_([record_input]))
                           )
            if st.form_submit_button("Submit"):
                with self.session as session:
                    session.execute(delete_stmt)
                    session.commit()

    def delete_records_product(self):
        with st.form("Delete Record from Product Inventory", clear_on_submit=True):
            blank_warning()
            record_input = st.text_input("prod_id code : ")
            delete_stmt = (delete(ProductInventory)
                           .where(ProductInventory.prod_id.in_([record_input]))
                           )
            if st.form_submit_button("Submit"):
                with self.session as session:
                    session.execute(delete_stmt)
                    session.commit()
