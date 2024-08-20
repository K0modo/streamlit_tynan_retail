import streamlit as st


def app_login_func():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    def login():
        if st.button("Log in",):
            st.session_state.logged_in = True
            st.rerun()

    def logout():
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.rerun()

    login_page = st.Page(login, title="Log in")
    logout_page = st.Page(logout, title="Log out")

    seller_page = st.Page(
        "pages/seller_page.py",
        title="Seller Main Page",
        # default=True
    )
    buyer_page = st.Page(
        "pages/buyer_page.py",
        title="Buyer Main Page"
    )

    if st.session_state.logged_in:
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Seller": [seller_page],
                "Buyer": [buyer_page]
            }
        )
    else:
        pg = st.navigation([login_page])

    pg.run()