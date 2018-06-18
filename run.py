# System modules




# Developer defined modules
import manager
from utilities import menu_strings

# Logging
import logging

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(levelname)s | %(asctime)s | %(name)s | %(funcName)s | %(message)s")

# Build file logger handler
fh = logging.FileHandler(filename="./logs/game-container.log",)
fh.setLevel(logging.DEBUG)
fh.setFormatter(log_format)
logger.addHandler(fh)


def main():
    logger.info("Test Message")
    logger.debug("Debug Message")
    print(menu_strings.welcome_string)
    exit = False
    while(exit is False):
        print(menu_strings.main_menu)
        option = input("> ")
        print("----------------------------------------------")
        if option.isdigit():
            option = int(option)
            print(f"You selected {option}")
            if option == 0:
                exit = True
        else:
            print(menu_strings.invalid_input)

if __name__ == '__main__':
    main()