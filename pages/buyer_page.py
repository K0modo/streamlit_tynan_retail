import streamlit as st
from st_connection_load import _st_conn
from operations_seller import view_cards
from operations_buyer.buyer_operations_options import select_category_line


sidebar_actions = ["View All Items",
                   "View by Category",
]


def buyer_operations():

    action = (st.sidebar.selectbox("Select Buyer Operations", sidebar_actions))

    if action == "View All Items":
        st.write("View All Items")
        view_cards.card_template(_st_conn)
    elif action == "View by Category":
        st.write("View by Category")
        select_category_line(_st_conn)

