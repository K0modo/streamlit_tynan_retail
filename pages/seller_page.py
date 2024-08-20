import streamlit as st
from st_connection_load import _st_conn
from operations_seller.create_table import create_model_tables
from operations_seller.records_enter import enter_records_to_table
from operations_seller.records_update import update_records_table
from operations_seller.records_delete import delete_records_from_table
from operations_seller.view_tables import view_tables
from operations_seller.view_reports import create_summary_report
from operations_seller.view_cards import card_template




sidebar_actions = ["View Cards",
                   "View Tables",
                   "View Reports",
                   "Enter Data",
                   "Update Record",
                   "Delete Record",
                   "Create Table"]

action = (st.sidebar.selectbox("Select Seller Operations", sidebar_actions))

if action == "View Cards":
    card_template(_st_conn)
elif action == "View Tables":
    view_tables(_st_conn)
elif action == "View Reports":
    st.write("Reports")
    create_summary_report(_st_conn)
elif action == "Enter Data":
    enter_records_to_table(_st_conn)
elif action == "Update Record":
    update_records_table(_st_conn)
elif action == "Delete Record":
    delete_records_from_table(_st_conn)
elif action == "Create Table":
    create_model_tables(_st_conn)



