import streamlit as st
from st_connection_load import st_conn
from .create_records import CreateRecords as CR
from .read_records import ReadRecords as RR
from .update_records import UpdateRecords as UR
from .delete_records import DeleteRecords as DR


def form_request():
    return st.write("Please complete form for selected table.")


class CRUDops:
    def __init__(self, table_choice):
        self.table_choice = table_choice

    def create_records(self):
        col = st.columns((5, 3))
        with col[0]:
            st.write("")
            form_request()
            if self.table_choice == "BusinessLine":
                choice = CR(st_conn.session)
                choice.create_records_table_line()
            elif self.table_choice == "ProductCategory":
                choice = CR(st_conn.session)
                choice.create_records_table_category()
            elif self.table_choice == "ProductInventory":
                choice = CR(st_conn.session)
                choice.create_records_table_product()

    def read_records(self):
        if self.table_choice == "BusinessLine":
            choice = RR(st_conn.session)
            choice.read_records_line()
        elif self.table_choice == "ProductCategory":
            choice = RR(st_conn.session)
            choice.read_records_category()
        elif self.table_choice == "ProductInventory":
            choice = RR(st_conn.session)
            choice.read_records_product()

    def update_records(self):
        col = st.columns((5, 3))
        with col[0]:
            st.write("")
            form_request()
            if self.table_choice == "BusinessLine":
                choice = UR(st_conn.session)
                choice.update_records_line()
            elif self.table_choice == "ProductCategory":
                choice = UR(st_conn.session)
                choice.update_records_category()
            elif self.table_choice == "ProductInventory":
                choice = UR(st_conn.session)
                choice.update_records_product()

    def delete_records(self):
        col = st.columns((5, 3))
        with col[0]:
            st.write("")
            form_request()
            if self.table_choice == "BusinessLine":
                choice = DR(st_conn.session)
                choice.delete_records_line()
            elif self.table_choice == "ProductCategory":
                choice = DR(st_conn.session)
                choice.delete_records_category()
            elif self.table_choice == "ProductInventory":
                choice = DR(st_conn.session)
                choice.delete_records_product()
