"""
_______________________________
Author: Patrick Carlson
-------------------------------

License: MIT License
"""
# Developer defined modules
from src import menu
from utilities import log_helper, menu_strings


def main():
    log_helper.start_logger()
    print(menu_strings.welcome_string)
    menu.main_menu()


if __name__ == '__main__':
    main()
