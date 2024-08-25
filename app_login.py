# import streamlit as st
# from pages.seller_page import seller_operations
# from pages.buyer_page import buyer_operations
# # from pages.log_in_page import login
# import os
# from PIL import Image

folder_path = r"C:\Users\jchri\PycharmProjects\streamlit_tynan_retail\product_photos"


def app_login_func():
    pass
    # if "logged_in" not in st.session_state:
    #     st.session_state.logged_in = False
    #
    # def login():
    #     with st.container():
    #         col1, col2, col3 = st.columns((1, 4, 1))
    #         with col2:
    #             st.markdown("""<h6 style='text-align: center'>
    #             Bringing Buyers and Sellers together.
    #             </h6>""", unsafe_allow_html=True)
    #     col1, col2, col3 = st.columns((3, 1, 3))
    #     with col2:
    #         st.write("")
    #         if st.button("Log in", ):
    #             st.session_state.logged_in = True
    #             st.rerun()
    #
    # def logout():
    #     with st.container():
    #         col1, col2, col3 = st.columns((1, 4, 1))
    #         with col2:
    #             st.markdown("""<h6 style='text-align: center'>
    #                 If you are finished shopping you may log out.
    #                 </h6>""", unsafe_allow_html=True)
    #             st.markdown("""<h6 style='text-align: center'>
    #                 Thank you for shopping!!
    #                 </h6>""", unsafe_allow_html=True)
    #     col1, col2, col3 = st.columns((3, 1, 3))
    #     with col2:
    #         st.write("")
    #         if st.button("Log out"):
    #             st.session_state.logged_in = False
    #             st.rerun()
    #
    # login_page = st.Page(
    #     login,
    #     title="Log In Page"
    # )
    # logout_page = st.Page(
    #     logout,
    #     title="Log Out Page",
    #     icon=":material/logout:"
    # )
    # seller_page = st.Page(
    #     seller_operations,
    #     title="Seller Main Page",
    #     default=True
    # )
    # buyer_page = st.Page(
    #     buyer_operations,
    #     title="Buyer Main Page"
    # )
    #
    # if st.session_state.logged_in:
    #     pg = st.navigation(
    #         {
    #             "Account": [logout_page],
    #             "Seller": [seller_page],
    #             "Buyer": [buyer_page]
    #         }
    #     )
    # else:
    #     pg = st.navigation([login_page])
    #
    # pg.run()

#
#
# import streamlit as st
# import os
# from PIL import Image
#
# folder_path = r"C:\Users\jchri\PycharmProjects\streamlit_tynan_retail\product_photos"
#
# title_of_page = st.markdown("<h2 style='text-align: center'>Tynan Retail Store</h2", unsafe_allow_html=True)
#
# def app_login_func():
#
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#
#     def login():
#         with st.container():
#             title_of_page
#             col1, col2, col3 = st.columns((1, 4, 1))
#             with col2:
#                 st.markdown("""<h6 style='text-align: center'>
#                 Bringing together buyers and sellers of personal property.
#                 </h6>""", unsafe_allow_html=True)
#
#         col1, col2, col3 = st.columns((3, 1, 3))
#         with col2:
#             st.write("")
#             if st.button("Log in",):
#                 st.session_state.logged_in = True
#                 st.rerun()
#
#     def logout():
#         with st.container():
#             title_of_page
#             col1, col2, col3 = st.columns((1, 4, 1))
#             with col2:
#                 st.markdown("""<h6 style='text-align: center'>
#                 Thank you for visiting the store.
#                 </h6>""", unsafe_allow_html=True)
#
#         col1, col2, col3 = st.columns((3, 1, 3))
#         with col2:
#             if st.button("Log out"):
#                 st.session_state.logged_in = False
#                 st.rerun()
#
#     login_page = st.Page(login, title="Log in")
#     logout_page = st.Page(logout, title="Log Out Page", icon=":material/logout:")
#
#     seller_page = st.Page(
#         "pages/seller_page.py",
#         title="Seller Main Page",
#         default=True
#     )
#     buyer_page = st.Page(
#         "pages/buyer_page.py",
#         title="Buyer Main Page"
#     )
#
#     if st.session_state.logged_in:
#         pg = st.navigation(
#             {
#                 "Account": [logout_page],
#                 "Seller": [seller_page],
#                 "Buyer": [buyer_page]
#             }
#         )
#     else:
#         pg = st.navigation([login_page])
#
#     pg.run()
