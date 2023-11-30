import tennis_rankings
import head_2_head


def verify_input(user_input):
    """
    Validates user input for ATP Rankings menu options.

    Args:
        user_input (str): The user-provided input for the menu option.

    Returns:
        str: The valid input for the ATP Rankings menu.
    """
    while True:
        if user_input not in ['head2head', 'ranking', '-h']:
            user_input = input("Invalid input: Please type either 'head2head' or 'ranking' or type '-h' for help. ")
        elif user_input == '-h':
            print("head2head: type the name of 2 players and see their stats side by side!\n"
                  "ranking: displays a list of top players and stats")
            user_input = input("Type either 'head2head' or 'ranking' or type '-h' for help. ")
        else:
            return user_input


def main():
    user = verify_input(input("Type one of two options: 'head2head' or 'ranking': "))
    if user == 'head2head':
        head_2_head.main()
    if user == 'ranking':
        tennis_rankings.main()


if __name__ == "__main__":
    main()
