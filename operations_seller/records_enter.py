import streamlit as st
from db_models import BusinessLine, ProductCategory, ProductInventory
from sqlalchemy import select


# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# img = Image.open(current_dir / "product_photos" / "prod_001" / "IMG_3672_drafttable.jpg")


def enter_records_to_table(st_conn):
    table_data = st.radio("Select table to add data:",
                          options=["Business Line",
                                   "Product Category",
                                   "Product Inventory",]
                          )
    if table_data == "Business Line":
        with st.form("Add Business Line", clear_on_submit=True):
            line_id_input = st.text_input("line_id code : ")
            line_name_input = st.text_input("line_name : ")
            add_record = BusinessLine(line_id=line_id_input,
                                      line_name=line_name_input)
            if st.form_submit_button("Submit"):
                if line_id_input == "":
                    return
                else:
                    with st_conn.session as session:
                        session.add(add_record)
                        session.commit()
    elif table_data == "Product Category":
        with st.form("Add Category Data", clear_on_submit=True):
            prod_cat_input = st.text_input("prod_cat code : ")
            cat_name_input = st.text_input("cat_name : ")
            line_id_input = st.text_input("line_id:")
            add_record = ProductCategory(prod_cat=prod_cat_input,
                                         cat_name=cat_name_input,
                                         line_id=line_id_input)
            input_record = add_record
            if st.form_submit_button("Submit"):
                if prod_cat_input == "" or cat_name_input == "":
                    return
                else:
                    with st_conn.session as session:
                        session.add(add_record)
                        session.commit()
                        st.write(input_record)
                    with st_conn.session as session:
                        result = session.execute(select(ProductCategory.prod_cat,
                                                        ProductCategory.cat_name,
                                                        ProductCategory.line_id)
                                                 )
                        st.dataframe(result, hide_index=True)
    elif table_data == "Product Inventory":
        with st.form("Add Product to Inventory", clear_on_submit=True):
            prod_name_input = st.text_input("prod_name: ")
            prod_desc_input = st.text_input("prod_desc: ")
            prod_price_input = st.text_input("prod_price: ")
            prod_photo_input = st.text_input("prod_photo: ")
            line_id_input = st.text_input("line_id: ")
            add_record = ProductInventory(
                prod_name=prod_name_input,
                prod_desc=prod_desc_input,
                prod_price=prod_price_input,
                prod_photo=prod_photo_input,
                line_id=line_id_input
            )
            input_record = add_record
            if st.form_submit_button("Submit"):
                if prod_name_input == "" :
                    return
                else:
                    with st_conn.session as session:
                        session.add(add_record)
                        session.commit()
                        st.write(input_record)
                    with st_conn.session as session:
                        result = session.execute(select(ProductCategory.prod_cat,
                                                        ProductCategory.cat_name,
                                                        ProductCategory.line_id)
                                                 )
                        st.dataframe(result, hide_index=True)

