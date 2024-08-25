from app_container import main_container_title
from .crud_tables import crud_table_radio
from .crud_actions import crud_actions_selectbox
from .create_table import create_model_tables
from .crud_class import CRUDops


def crud_operations_func():
    main_container_title()

    action = crud_actions_selectbox()

    if action == "Create Records":
        table_choice = crud_table_radio()
        operation = CRUDops(table_choice)
        operation.create_records()
    elif action == "Read Records":
        table_choice = crud_table_radio()
        operation = CRUDops(table_choice)
        operation.read_records()
    elif action == "Update Records":
        table_choice = crud_table_radio()
        operation = CRUDops(table_choice)
        operation.update_records()
    elif action == "Delete Records":
        table_choice = crud_table_radio()
        operation = CRUDops(table_choice)
        operation.delete_records()
    elif action == "Create Tables":
        create_model_tables()
