import streamlit as st
from db_models import BusinessLine, ProductCategory
from sqlalchemy import update


class UpdateRecords:
    def __init__(self, session_conn):
        self.session = session_conn

    def update_records_line(self):
        with st.form("Update Business Line", clear_on_submit=True):
            target_record = st.text_input("Target line_id to update : ")
            new_record = st.text_input("New line_name : ")
            update_stmt = (update(BusinessLine)
                    .where(BusinessLine.line_id == target_record)
                    .values(line_name=new_record)
                    )
            if st.form_submit_button("Submit"):
                with self.session as session:
                    session.execute(update_stmt)
                    session.commit()

    def update_records_category(self):
        with st.form("Update Product Category", clear_on_submit=True):
            target_record = st.text_input("Target prod_cat to update : ")
            new_cat_name = st.text_input("New cat_name : ")
            new_line_id = st.text_input("New line_id : ")
            update_stmt = (update(ProductCategory)
                    .where(ProductCategory.prod_cat == target_record)
                    .values(cat_name=new_cat_name, line_id=new_line_id)
                    )
            if st.form_submit_button("Submit"):
                with self.session as session:
                    session.execute(update_stmt)
                    session.commit()


    def update_records_product(self):
        st.markdown(":orange[Please contact Database Administrator]")


