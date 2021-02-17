#Functions
def yes_no(question,valid_answers):

    error = "Sorry that is not a valid response"

    valid = False
    while not valid:
        response = input(question).lower()

        if response in valid_answers:
            return response
        else:
            for item in valid_answers:
                if response == item[0]:
                    return item

        print(error)


for item in range(0,6):
    yes_no("Do you want to buy snacks: ",["yes","no"])