import pandas as pd
import csv


class InventoryReports:
    def __init__(self, table):
        self.table = table

    def inventory_category_summary(self):
        df_table = (self.table.groupby('prod_cat', as_index=True)
                    .agg(InventoryCount=('prod_price', 'count'), InventoryValue=('prod_price', 'sum'))
                    )
        return df_table

    def select_category(self):
        df_table = self.table
        return df_table