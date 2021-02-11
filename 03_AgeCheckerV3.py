def intcheck(question):
    valid = False
    # Error messages

    error = "please enter a whole number greater than 0"

    while not valid:
        try:
            # Gets user input
            response = int(input(question))
            # Checks number is not below zero
            if response <= 0:
                print(error)
                print()
            else:
                return response



        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()




name = ""
count = 0
max_tickets = 5

while count < max_tickets:
    if(max_tickets - count ) == 1:
        print("")
        print("!!! There is only 1 ticket left !!!")
        print("")
    else:
        print("You have {} tickets left".format(max_tickets - count))

    name = input("Name:")
    if name == "xxx":
        break

    age = intcheck("Age: ")
    if age < 12:
        print("Error: You are too young to see this movie")
        continue
    elif age > 130:
        print("Error: The age entered is too high")
        continue

    count += 1

if count < max_tickets:
    print("You have sold {}".format(count))
    print("There are {} tickets left".format(max_tickets-count))
else:
    print("All tickets have been sold")

