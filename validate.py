# validating user inputs for integers

def validate_input(user_input):
    while True:
        try:
            user_input = int(input(user_input))
        except ValueError:
            print("Enter a whole number. Try again!")
            continue
        else:
            return user_input
            break