
import streamlit as st
from st_connection_load import _st_conn
from operations_seller.create_table import create_model_tables
from operations_seller.records_enter import enter_records_to_table
from operations_seller.records_update import update_records_table
from operations_seller.records_delete import delete_records_from_table
from operations_seller.view_tables import view_tables
from operations_seller.view_reports import create_summary_report
from operations_seller.view_cards import card_template
from operations_seller.view_reports_calcultions import inventory_category_summary


sidebar_actions = ["View Cards",
                   "View Tables",
                   "View Reports",
                   "Enter Data",
                   "Update Record",
                   "Delete Record",
                   "Create Table",
                   "DataFrame"]


def seller_operations():

    action = (st.sidebar.selectbox("Select Seller Operations", sidebar_actions))

    with _st_conn.session as session:

        if action == "View Cards":
            # pass
            card_template(session)
        elif action == "View Tables":
            view_tables(session)
        elif action == "View Reports":
            st.write("Reports")
            data = create_summary_report(session)
            # df = inventory_category_summary(data)
            st.dataframe(data)
        elif action == "Enter Data":
            enter_records_to_table(session)
        elif action == "Update Record":
            update_records_table(session)
        elif action == "Delete Record":
            delete_records_from_table(session)
        elif action == "Create Table":
            create_model_tables(_st_conn)
        # elif action == "DataFrame":




