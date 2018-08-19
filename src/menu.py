import sys
from utilities import log_helper, menu_strings
from src.manager import Manager
# Get Logger
log = log_helper.get_logger()

test = None

manager = Manager()


def main_menu():
    exit = False
    while(exit is False):
        print(menu_strings.main_menu)
        option = verify_input(input("> "), main_menu)
        if option == 0:
            print(f"Exiting program, thank you!")
            manager.stop_all_containers()
            sys.exit()
        elif option == 1:
            deploy_menu()
        elif option == 2:
            manager.list_containers()
        elif option == 4:
            get_server_info()
        else:
            print(f"You selected {option} which is not yet implemented")


def deploy_menu():
    invalid_types = [2, 3]
    fencepost = True
    while(fencepost):
        print(menu_strings.game_types)
        game_type = verify_input(input("> "), deploy_menu)
        if game_type == 0:
            main_menu()
        if game_type in invalid_types:
            print(f"Invalid Game or not yet implemented, please select again")
        else:
            manager.deploy_container(game_type)
            fencepost = False


def verify_input(input, menu):
    if input.isdigit():
        return int(input)
    else:
        print(menu_strings.invalid_input)
        menu()


def stop_server():
    pass


def get_server_info():
    container_list = manager.get_container_info()
    count = 1
    for container in container_list:
        print(f"{count}) {container.get('name')}")
    option = verify_input(input("\n> "), get_server_info)
    container = container_list[option - 1]
    obj = container.get('container_object')
    print(f"name {container.get('name')}")
    print(f"STATUS: {obj.status}")
    print(f"HOST PORT: {container.get('host_port')}")
    print(f"INTERNAL PORT: {container.get('internal_port')}")
    fencepost = True
    while(fencepost):
        logs = input("Would you like to view the logs? (y,n) > ")
        logs = logs.lower()
        if logs not in ["y", "n"]:
            fencepost = True
        else:
            fencepost = False
    if logs == "y":
        print(f"Logs Start -----------------\n")
        print(obj.logs(stdout=True))
        print(f"Logs End -------------------\n")


