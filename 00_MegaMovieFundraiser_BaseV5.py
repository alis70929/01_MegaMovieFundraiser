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


def string_checker(choice, options):
    for var_list in options:

        if choice.lower() in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        print("Error: Please enter a valid choice")
        return "invalid choice"


def get_snacks():
    number_regex = "^[1-9]"

    valid_snacks = [

        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj"]

    ]

    chosen_snacks = []

    desired_snack = ""
    while desired_snack != "xxx":
        snack_row = []
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return chosen_snacks

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1

        desired_snack = desired_snack.strip()

        snack_chosen = string_checker(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry we have a four snack maximum")
            snack_chosen = "invalid choice"

        if snack_chosen != "invalid choice":
            print("Snack Chosen:{} {}".format(amount, snack_chosen))

        snack_row.append(amount)
        snack_row.append(snack_chosen)

        if snack_chosen != "xxx" and snack_chosen != "invalid choice":
            chosen_snacks.append(snack_row)


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

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice

}

# initialize string checker lists
yes_no_list = [
        ["yes", "y"],
        ["no", "n"]
    ]

pay_method = [
    ['cash', 'ca'],
    ['credit', 'cr']

]


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

    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to buy a snack")
        check_snack = string_checker(want_snack, yes_no_list)

    if check_snack == "Yes":
        get_order = get_snacks()
    else:
        get_order = []

    print()
    if len(get_order) == 0:
        print("Snacks Ordered: None")
    else:
        print("Snacks Ordered: ")

        for item in get_order:
            print(item)

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

