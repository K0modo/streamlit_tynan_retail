import streamlit as st

from data_import_files.table_list_dict import product_category_id

available_reports = ["Category",
                     "Select",
                    ]


class ReportData:
    def __init__(self, _st_conn):
        self.conn = _st_conn
        self.table = self.load_report_data()

    def load_report_data(self):
        db_query = "SELECT *  FROM product_inventory"
        result = self.conn.query(db_query)
        return result

    def inventory_category_summary(self):
        df_table = (self.table.groupby('prod_cat', as_index=True)
                .agg(InventoryCount=('prod_price', 'count'), InventoryValue=('prod_price', 'sum'))
                )
        return df_table

    def select_category(self):
        pass

    def select_reports(self):
        table = st.radio("Select Report", available_reports)
        if table == "Category":
            st.subheader("Inventory by Category")
            df_table = self.inventory_category_summary()
            st.dataframe(df_table)
        elif table == "Select":
            st.subheader("Select Inventory Category")
            choice = st.selectbox('Select Category', product_category_id)
            df_table = self.table[self.table['prod_cat'] == choice]
            df_table = df_table.loc[:, ['prod_id', 'prod_name', 'prod_desc','prod_price']]
            st.dataframe(df_table, hide_index=True)










