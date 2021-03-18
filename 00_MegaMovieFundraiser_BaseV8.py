# Imports
import re, pandas

# Functions


# checks if string is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print(error_message)


# checks if value is an integer
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


# checks who many tickets are left
def check_tickets(tickets_sold, ticket_limit):
    # special message if only one ticket is left
    if (ticket_limit - tickets_sold) == 1:
        print("")
        print("!!! There is only 1 ticket left !!!")
        print("")
    else:
        print("You have {} tickets left".format(ticket_limit - tickets_sold))


# compares given string to valid options, Returns items in Title case
def string_checker(choice, options):

    # checks if the choice is in one of the options lists, returns the first item in that list in title case
    for var_list in options:

        if choice.lower() in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"
    # if choice was valid return item form above or tell users invalid choice
    if is_valid == "yes":
        return chosen
    else:
        print("Error: Please enter a valid choice")
        return "invalid choice"


# Snacks Component, asks user for snacks and amount
def get_snacks():

    # regular expression for finding numbers 1-9 inclusive
    number_regex = "^[1-9]"

    # list of valid snacks
    valid_snacks = [["popcorn", "p", "corn", "a"],
                    ["M&Ms", "m&ms", "mms", "m", "b"],
                    ["pita chips", "chips", "pc", "pita", "c"],
                    ["water", "w", "d"], ["orange juice", "oj", "e"]]

    # initialize chosen snack master list
    chosen_snacks = []

    # setup loop variable
    desired_snack = ""
    # loop til user enters exit code or n
    while desired_snack != "xxx" or desired_snack != "n":

        # initialize list for one type of snack
        snack_row = []
        # ask user for their choice of snack
        desired_snack = input("Snack: ").lower()

        # if exit code is entered break out of loop
        if desired_snack == "xxx" or desired_snack == "n":
            return chosen_snacks

        # if the users choice has a number at the front
        if re.match(number_regex, desired_snack):

            #seperate that number form the rest of the string and put them in variables
            amount = int(desired_snack[0])  # number
            desired_snack = desired_snack[1:]  # rest of string

        # if no number at front assume the user wants one
        else:
            amount = 1

        # strip blank spaces
        desired_snack = desired_snack.strip()

        # check if the chsoen snack is a valid snack from the list of valid snacks
        snack_chosen = string_checker(desired_snack, valid_snacks)

        # limit users to only be able to order 4 of a snack
        if amount >= 5:
            print("Sorry we have a four snack maximum")
            snack_chosen = "invalid choice"
        # if chosen thing
        if snack_chosen != "invalid choice":
            print("Snack Chosen:{} {}".format(amount, snack_chosen))

        snack_row.append(amount)
        snack_row.append(snack_chosen)

        if snack_chosen != "xxx" and snack_chosen != "invalid choice":
            chosen_snacks.append(snack_row)


# get age of customer and check the ticket price
def get_ticket_price():
    age = intcheck("Age: ")
    # Check if age is within range
    if age < 12:
        print("Error: You are too young to see this movie")
        return "invalid ticket price"
    elif age > 130:
        print("Error: The age entered is too high")
        return "invalid ticket price"

    # set ticket price according to age
    if age < 16:
        price = 7.50
    elif age > 64:
        price = 6.50
    else:
        price = 10.50

    return price


# currency formatting
def currency(x):
    return '${:.2f}'.format(x)


# Main

# initialize loop values
name = ""
ticket_count = 0
max_tickets = 150  # set maximum tickets

# initialize lists for movie data dictionary
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

surcharge_mult_list = []

# set headings for summary data
summary_headings = [
    'Popcorn', 'M&Ms', 'Pita Chips', 'Water', 'Orange Juice', 'Snack Profit',
    'Ticket Profit', 'Total Profit'
]
# setup list for summary data
summary_data = []

# set up dictionaries
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge Multiplier': surcharge_mult_list
}

summary_data_dict = {'Item': summary_headings, 'Amount': summary_data}

price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# initialize string checker lists
yes_no_list = [["yes", "y"], ["no", "n"]]

pay_method = [['cash', 'ca'], ['credit', 'cr']]

# counts how much money is made from tickets
total_sale = 0

#loop till all tickets are sold or exit code is entered
while ticket_count < max_tickets:

    # says how many tickets are left, special message if only one is left
    check_tickets(ticket_count, max_tickets)

    # ask user for name and checks that the name is not blank
    name = not_blank(
        "Name: ", "sorry - This cannot be left blank, "
        "Please enter a name")

    # exit code is entered break out of loop
    if name == "xxx":
        break

    # ask/check users age, if below 12 years old or above 130 go back to beginning of loop
    ticket_price = get_ticket_price()
    if ticket_price == "invalid ticket price":
        continue

    # add this tickets price to the total sale
    total_sale += ticket_price
    # add 1 to how many tickets have been sold
    ticket_count += 1

    # add the users name and ticket price in the corresponding list for later proccessing
    all_names.append(name)
    all_tickets.append(ticket_price)

    # get how many snacks the user wants
    snack_order = get_snacks()

    # add zeros onto the end of the snack lists as place
    for item in snack_lists:
        item.append(0)

    # loops for every type of snack order by the User
    for item in snack_order:

        if len(item) > 0:

            to_find = (item[1])  # gets the name of the snack
            amount = (item[0])  # gets the amount of the snack
            add_list = movie_data_dict[
                to_find]  # finds the list corresponding to the snack threough the dictionary
            add_list[
                -1] = amount  # replaces the placeholder at the end of the list with the amount of the snack

    # loop asking how the user wants to pay (cash or credit)
    how_pay = "invalid choice"
    while how_pay == 'invalid choice':
        how_pay = input("please choose a payment method (cash or credit)")
        how_pay = string_checker(how_pay, pay_method)

    # depending on abovea answer set the proper surcharge multiplier
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0
    # add the surcharge multiplier to the list so it can be used for summary and math later
    surcharge_mult_list.append(surcharge_multiplier)

# create data frame from the movie_data dictionary
movie_frame = pandas.DataFrame(movie_data_dict)
# Set the index to name
movie_frame = movie_frame.set_index('Name')

# Calculate the price of snacks
movie_frame['Snacks'] = \
    movie_frame["Popcorn"] * price_dict['Popcorn'] + \
    movie_frame["Water"] * price_dict['Water'] + \
    movie_frame["Pita Chips"] * price_dict['Pita Chips'] + \
    movie_frame["M&Ms"] * price_dict['M&Ms'] + \
    movie_frame["Orange Juice"] * price_dict['Orange Juice']

# calaculate sub total before surcharge
movie_frame['Sub Total'] = \
    movie_frame["Ticket"] + movie_frame['Snacks']

# calculate how much surcharge is made
movie_frame["Surcharge"] = \
  movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

# add surcharge and sub total together to get total
movie_frame["Total"] = \
  movie_frame["Sub Total"] + movie_frame['Surcharge']

# shorten long column names
movie_frame = movie_frame.rename(columns={
    'Orange Juice': 'OJ',
    'Pita Chips': 'Chips',
    'Surcharge Multiplier': "SM"
})

# add together how many of each snack is sold in total and pit it in summary data
for item in snack_lists:
    summary_data.append(sum(item))

# get the total amount of snack cost form across customers
snack_total = movie_frame['Snacks'].sum()
# calculate profit from snacks(20%)
snack_profit = snack_total * 0.2

# calculate ticket profit
ticket_profit = total_sale - (5 * ticket_count)

# add together ticket and snack profit for total profit
total_profit = snack_profit + ticket_profit

# format all of the profits above with dollar sign and two decimals
dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = currency(item)
    summary_data.append(item)

# make a data frame with the summary data
summary_frame = pandas.DataFrame(summary_data_dict)
# set the index as to the row names
summary_frame = summary_frame.set_index('Item')

# get rid of column limit
pandas.set_option('display.max_columns', None)

# create list of colums for the movie frame that we want to format to currency
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']

# format the selected columns above to $ and 2 decimals
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# send customer ticket data and overall summary data to .csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv('snack_summary.csv')

# show the user ticket info shorntened down
print()
print("*** Ticket/Snack Info ***")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

print()
# show summary table
print("*** Snack/Profit Summary ***")
print()
print(summary_frame)

# say how many tickets are left
if ticket_count < max_tickets:
    print("You have sold {}".format(ticket_count))
    print("There are {} tickets left".format(max_tickets - ticket_count))
else:
    print("All tickets have been sold")
