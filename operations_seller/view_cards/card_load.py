import streamlit as st
from sqlalchemy import select
from db_models import ProductInventory
import os

from PIL import Image

folder_path = r"./product_photos"


@st.cache_data
def card_template(_connection):
    with _connection as session:
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
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center'>{r[0]}</h5", unsafe_allow_html=True)
                col1, col2, col3 = st.columns((1, 3, 1))
                filename = r[3]
                if filename:
                    img_path = os.path.join(folder_path, filename)
                    img = Image.open(img_path)  # .resize((180, 150))
                    with col2:
                        st.image(img, use_column_width=True)
                st.markdown(f"<h5 style='text-align: center'>Price : $ {r[2]}</h5", unsafe_allow_html=True)
                col1, col2 = st.columns((5, 3))
                with col1:
                    st.markdown(f"<h6 style=''>Description: {r[1]}</h6", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<h6 style='padding: 0% 0% 2% 0%'>Product Dimensions</h6", unsafe_allow_html=True)
                    st.markdown(f"<h6 style='padding: 0'>Width: {r[4]}</h6", unsafe_allow_html=True)
                    st.markdown(f"<h6 style='padding: 0'>Height: {r[5]}</h6", unsafe_allow_html=True)
                    st.markdown(f"<h6 style='padding: 0% 0% 2% 0%'>Depth: {r[6]}</h6", unsafe_allow_html=True)


def count_images_folder():
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('jpg')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            images.append(img)
    st.write(f"Loaded {len(images)} images. ")
