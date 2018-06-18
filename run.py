from utilities import menu_strings


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
