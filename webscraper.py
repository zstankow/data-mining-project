import tennis_rankings
import head_2_head


def verify_input(user_input):
    while True:
        if user_input not in ['head2head', 'ranking', '-h']:
            user_input = input("Invalid input: Please type either 'head2head' or 'ranking' or type '-h' for help. ")
        elif user_input == '-h':
            print("head2head: type the name of 2 players and see which player is more likely to win!\n"
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
