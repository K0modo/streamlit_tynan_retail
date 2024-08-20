import streamlit as st
import pandas as pd
from pandas import DataFrame

# import st_connection_load as st_conn
from sqlalchemy import select
from sqlalchemy.sql import func
from db_models import ProductInventory

available_reports = ["Category"]


def create_summary_report(st_conn):
    table = st.radio("Select Report", available_reports)
    if table == "Category":
        st.subheader("Inventory by Category")
        with st_conn.session as session:
            result = (session.execute(select(ProductInventory.prod_id,
                                             ProductInventory.prod_name,
                                             ProductInventory.prod_price,
                                             ProductInventory.line_id,
                                             ProductInventory.prod_cat)
                                    )
                      )
            df = DataFrame(result.fetchall())
            # df.columns = result.keys()
            df = df.groupby('prod_cat')[['prod_price']].sum()
            st.dataframe(df)

