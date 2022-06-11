from player import create_character, load_character


def main_menu():
    menu1 = input(
        "Please enter the number of the option you would like to choose:\n1. Create a Character.\n2. Load an Existing Character.\n3. Cancel.\n"
    )

    print(f'\n{menu1}')
    if int(menu1) == 1:
        input_name = input(
            'What would you like your character name to be?\n> ')
        try:
            player = create_character(f'{input_name}')

            print(f'{input_name} has been created and added to the database')

            return player

        except Exception as e:
            print(e)
            print('There was an issue creating your character.')
            return None

    if int(menu1) == 2:
        input_name = input(
            'What is the name of the character that we are loading?\n> ')

        try:
            player = load_character(f"{input_name}")
            print(f'{input_name} has been successfully loaded.')
            return player

        except Exception as e:
            print(e)
            print(
                f'There was an issue that occured when trying to load {input_name}'
            )
            return None






	