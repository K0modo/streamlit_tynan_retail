from app_container import main_container_title

from .card_load import card_template
from st_connection_load import st_conn

def load_cards():
    main_container_title()
    card_template(st_conn.session)
