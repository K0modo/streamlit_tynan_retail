import streamlit as st
from st_connection_load import _st_conn
from db_models import ProductInventory, BusinessLine, ProductCategory
from data_import_files.table_list_dict import business_line_id, product_category_id
from sqlalchemy import select
import os
from PIL import Image

folder_path = r"C:\Users\jchri\PycharmProjects\home_retail\product_photos"

@st.cache_data
class BuyerActions:

    def __init__(self, st_conn):
        self.conn = st_conn

    def card_template(self):
        with open('actions_seller/style.css') as f:
            st.markdown(f"<style>{f.read()}<style", unsafe_allow_html=True)
        with self.conn.session as session:
            result = session.execute(select(
                                            ProductInventory.prod_name,
                                            ProductInventory.prod_desc,
                                            ProductInventory.prod_price,
                                            ProductInventory.prod_photo,
                                            ProductInventory.prod_width,
                                            ProductInventory.prod_height,
                                            ProductInventory.prod_depth,
                                            )
                                     )
            for r in result:
                with st.container(height=500, border=True):
                    st.markdown(f"<h5 style='text-align: center'>{r[0]}</h5", unsafe_allow_html=True)
                    col1, col2, col3 = st.columns((1,3,1))
                    filename = r[3]
                    if filename:
                        img_path = os.path.join(folder_path, filename)
                        img = Image.open(img_path)  #.resize((180, 150))
                        with col2:
                            st.image(img, use_column_width=True)
                    st.markdown(f"<h5 style='text-align: center'>Price : $ {r[2]}</h5", unsafe_allow_html=True)
                    col1, col2 = st.columns((5,3))
                    with col1:
                        st.markdown(f"<h6 style=''>Description: {r[1]}</h6", unsafe_allow_html=True)
                    with col2:
                        st.markdown(f"<h6 style='padding: 0% 0% 2% 0%'>Product Dimensions</h6", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='padding: 0'>Width: {r[4]}</h6", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='padding: 0'>Height: {r[5]}</h6", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='padding: 0'>Depth: {r[6]}</h6", unsafe_allow_html=True)


def select_category_line(_st_conn):

    with st.form("Select Options"):
        category_choice = st.selectbox("Select Product Category", product_category_id)
        st.form_submit_button("Submit")
        with _st_conn.session as session:
            result = session.execute(select(ProductInventory.prod_name,
                                            ProductInventory.prod_desc,
                                            ProductInventory.prod_price,
                                            ProductInventory.prod_photo,
                                            ProductInventory.prod_width,
                                            ProductInventory.prod_height,
                                            ProductInventory.prod_depth,)
                                     .where(ProductInventory.prod_cat == category_choice)
                                     )
            # for r in result:
            #     st.write(r)
            for r in result:
                with st.container(height=500, border=True):
                    st.markdown(f"<h5 style='text-align: center'>{r[0]}</h5", unsafe_allow_html=True)
                    col1, col2, col3 = st.columns((1,3,1))
                    filename = r[3]
                    if filename:
                        img_path = os.path.join(folder_path, filename)
                        img = Image.open(img_path)  #.resize((180, 150))
                        with col2:
                            st.image(img, use_column_width=True)
                    st.markdown(f"<h5 style='text-align: center'>Price : $ {r[2]}</h5", unsafe_allow_html=True)
                    col1, col2 = st.columns((5,3))
                    with col1:
                        st.markdown(f"<h6 style=''>Description: {r[1]}</h6", unsafe_allow_html=True)
                    with col2:
                        st.markdown(f"<h6 style='padding: 0% 0% 2% 0%'>Product Dimensions</h6", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='padding: 0'>Width: {r[4]}</h6", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='padding: 0'>Height: {r[5]}</h6", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='padding: 0'>Depth: {r[6]}</h6", unsafe_allow_html=True)





