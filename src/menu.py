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
            sys.exit()
        elif option == 1:
            deploy_menu()
        elif option == 2:
            manager.list_containers()
        else:
            print(f"You selected {option} which is not yet implemented")


def deploy_menu():
    fencepost = True
    while(fencepost):
        print(menu_strings.game_types)
        game_type = verify_input(input("> "), deploy_menu)
        if game_type == 0:
            main_menu()
        if get_games(game_type) is "invalid":
            print(f"Invalid Game or not yet implemented, please select again")
        else:
            # import pdb; pdb.set_trace()
            manager.deploy_container(game_type)
            fencepost = False


def verify_input(input, menu):
    if input.isdigit():
        return int(input)
    else:
        print(menu_strings.invalid_input)
        menu()


def get_games(game_type):
    if game_type == 1:
        return "terraria"
    else:
        return "invalid"
