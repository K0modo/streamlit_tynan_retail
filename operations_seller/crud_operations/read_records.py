import streamlit as st
from db_models import BusinessLine, ProductCategory, ProductInventory
from sqlalchemy import select


class ReadRecords:
    def __init__(self, session_conn):
        self.session = session_conn

    def read_records_line(self):
        st.subheader("BusinessLine Table")
        with self.session as session:
            result = session.execute(select(BusinessLine.line_id,
                                                BusinessLine.line_name)
                                         )
            st.dataframe(result, hide_index=True)

    def read_records_category(self):
        st.subheader("ProductCategory Table")
        with self.session as session:
            result = session.execute(select(ProductCategory.prod_cat,
                                            ProductCategory.cat_name,
                                            ProductCategory.line_id)
                                     )
            st.dataframe(result, hide_index=True)

    def read_records_product(self):
        st.subheader("ProductInventory Table")
        with self.session as session:
            result = session.execute(select(ProductInventory.prod_id,
                                            ProductInventory.prod_name,
                                            ProductInventory.prod_price,
                                            ProductInventory.prod_photo,
                                            ProductInventory.line_id,
                                            ProductInventory.prod_cat)
                                     )
            st.dataframe(result, hide_index=True)

