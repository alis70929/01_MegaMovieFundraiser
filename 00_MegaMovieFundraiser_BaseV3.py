# Imports
import re, pandas


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


def check_tickets(tickets_sold,ticket_limit):
    if (ticket_limit - tickets_sold) == 1:
        print("")
        print("!!! There is only 1 ticket left !!!")
        print("")
    else:
        print("You have {} tickets left".format(ticket_limit - tickets_sold))


def get_ticket_price():
    age = intcheck("Age: ")
    # Check if age is within range
    if age < 12:
        print("Error: You are too young to see this movie")
        return "invalid ticket price"
    elif age > 130:
        print("Error: The age entered is too high")
        return "invalid ticket price"


    if age < 16:
        price = 7.50
    elif age > 64:
        price = 6.50
    else:
        price = 10.50

    return price


# Main

name = ""
ticket_count = 0
max_tickets = 5

all_names = []
all_tickets = []

movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets

}

total_sale = 0
while ticket_count < max_tickets:

    check_tickets(ticket_count, max_tickets)

    name = not_blank("Name: ",
                     "sorry - This cannot be left blank, "
                     "Please enter a name")

    if name == "xxx":
        break

    ticket_price = get_ticket_price()
    if ticket_price == "invalid ticket price":
        continue

    total_sale += ticket_price
    ticket_count += 1

    all_names.append(name)
    all_tickets.append(ticket_price)

    print("{}:${:.2f}".format(name,ticket_price))


movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

profit = total_sale - (5*ticket_count)
print("You have made ${:.2f} profit".format(profit))

if ticket_count < max_tickets:
    print("You have sold {}".format(ticket_count))
    print("There are {} tickets left".format(max_tickets-ticket_count))
else:
    print("All tickets have been sold")

