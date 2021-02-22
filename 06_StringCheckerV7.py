# Imports
import re


# Functions
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




# Main Routine
yes_no_list = [
        ["yes", "y"],
        ["no", "n"]
    ]


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


