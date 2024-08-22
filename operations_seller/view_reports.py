import streamlit as st
from sqlalchemy import select
from db_models import ProductInventory, ProductCategory


available_reports = ["Category", "Cat2"
                     ]


def create_summary_report(session):
    table = st.radio("Select Report", available_reports)
    if table == "Category":
        st.subheader("Inventory by Category")
        query = select(ProductInventory.prod_id,
                       ProductInventory.prod_name,
                       ProductInventory.prod_price,
                       ProductInventory.line_id,
                       ProductInventory.prod_cat,
                       )
        result = session.execute(query)

        return result

    elif table == "Cat2":
        st.subheader("Inventory by Category")
        query = select(ProductInventory.prod_id,
                       ProductInventory.prod_name,
                       ProductInventory.prod_price,
                       ProductInventory.line_id,
                       ProductInventory.prod_cat,
                       )
        result = session.execute(query)

        return result










        #     result = session.execute(query)
        #     df = pd.DataFrame(result.fetchall())
        #     df = df.groupby(['prod_cat'], as_index=True).agg(InventoryCount=("prod_cat", 'count'),
        #                                                     InventoryValue=("prod_price", 'sum'))
        #     st.dataframe(df)



