
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

valid_snacks = [

    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],

]

yes_no_list = [
        ["yes", "y"],
        ["no", "n"]
    ]

snack_ok = ""
snack = ""

chosen_snacks = []
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to buy a snack")
    check_snack = string_checker(want_snack, yes_no_list)


if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        snack_chosen = string_checker(desired_snack, valid_snacks)
        if snack_chosen != "invalid choice":
            print("Snack Chosen: {}".format(snack_chosen))

        if snack_chosen != "xxx" and snack_chosen != "invalid choice":
            chosen_snacks.append(snack_chosen)

print()
if len(chosen_snacks) == 0:
    print("Snacks Ordered: None")
else:
    print("Snacks Ordered: ")

    for item in chosen_snacks:
        print(item)


