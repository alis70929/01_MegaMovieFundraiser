
def string_checker(choice, options):
    for var_list in options:

        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
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


while check_snack == "invalid choice":
    want_snack = input("Do you want to buy a snack")
    check_snack = string_checker(want_snack, yes_no_list)

for item in range(0, 6):
    desired_snack = input("Snack: ").lower()
    snack_chosen = string_checker(desired_snack, valid_snacks)
    print("Snack Chosen: {}".format(snack_chosen))


