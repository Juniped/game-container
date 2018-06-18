# System modules
import sys



# Developer defined modules
import manager
from utilities import menu_strings

# Logging
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(levelname)8s | %(asctime)s | %(name)12s | %(funcName)15s | %(message)s")

# Build File Handler
fh = logging.FileHandler(filename="./logs/game-container.log",)
fh.setLevel(logging.DEBUG)
fh.setFormatter(log_format)

# Add Handlers to Logger
logger.addHandler(fh)


def main():
    logger.info("Test Message")
    logger.debug("Debug Message")
    print(menu_strings.welcome_string)
    main_menu()


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
if __name__ == '__main__':
    main()