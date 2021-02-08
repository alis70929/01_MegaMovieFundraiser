
def not_blank(question,error_message):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print(error_message)


name = not_blank("Name: ",
                 "sorry - This cannot be left blank, "
                 "Please enter a name")

