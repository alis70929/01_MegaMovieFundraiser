# Functions
def not_blank(question,error_message):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print(error_message)


def intcheck(question):
    valid = False
    # Error message

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



# Main
name = ""

ticket_count = 0
max_tickets = 5

total_sale = 0
while ticket_count < max_tickets:

    if(max_tickets - ticket_count ) == 1:
        print("")
        print("!!! There is only 1 ticket left !!!")
        print("")
    else:
        print("You have {} tickets left".format(max_tickets - ticket_count))

    name = not_blank("Name: ",
                     "sorry - This cannot be left blank, "
                     "Please enter a name")

    if name == "xxx":
        break

    age = intcheck("Age: ")
    # Check if age is within range
    if age < 12:
        print("Error: You are too young to see this movie")
        continue
    elif age > 130:
        print("Error: The age entered is too high")
        continue

    price = 0
    if age < 16:
        price = 7.50
    elif age > 64:
        price = 6.50
    else:
        price = 10.50

    total_sale += price
    ticket_count += 1

    print("{}:${:.2f}".format(name,price))


if ticket_count < max_tickets:
    print("You have sold {}".format(ticket_count))
    print("There are {} tickets left".format(max_tickets-ticket_count))
else:
    print("All tickets have been sold")

profit = total_sale - (5*ticket_count)
print("You have made ${:.2f} profit".format(profit))

