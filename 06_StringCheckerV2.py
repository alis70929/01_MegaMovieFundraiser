

valid_snacks = [

    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],

]

snack_ok = ""
snack = ""
for item in range(0,6):

    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        if desired_snack in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        else:
            snack_ok = "no"

    if snack_ok == "yes":
        print("snack Choice: ", snack)
    else:
        print("invalid choice")
