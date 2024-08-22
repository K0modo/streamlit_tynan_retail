import pandas as pd
import csv

def inventory_category_summary(data):
    df = pd.DataFrame(data)
    with open('query_data3.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        header = ['prod_id', 'prod_name', 'prod_price', 'line_id', 'prod_cat', 'cat_name']
        writer.writerow(header)
        for row in df:
            writer.writerow(row)
    # df = df.groupby(['prod_cat'], as_index=True).agg(InventoryCount=("prod_price", 'count'),
    #                                                     InventoryValue=("prod_price", 'sum'))
