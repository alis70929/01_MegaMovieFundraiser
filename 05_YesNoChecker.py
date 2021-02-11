#Functions
def yes_no(question):

    error = "Please enter Yes or No"

    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "y"
        elif response == "no" or response == "n":
            return "n"
        else:
            print(error)


for item in range(0,6):
    yes_no("Do you want to buy snacks: ")