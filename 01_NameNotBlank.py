
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("sorry - This cannot be left blank")


name = not_blank("Name: ")
