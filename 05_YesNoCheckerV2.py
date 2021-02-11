#Functions
def yes_no(question,valid_answers):

    error = "Please enter Yes or No"

    valid = False
    while not valid:
        response = input(question).lower()

        if response in valid_answers:
            return response
        else:
            for item in valid_answers:
                if response == item[0]:
                    return item

        print("please enter Yes or No")


for item in range(0,6):
    yes_no("Do you want to buy snacks: ",["yes","no"])