

# Functions
# Warning: Response is returned in title case
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


# main

pay_method = [
    ['cash', 'ca'],
    ['credit', 'cr']

]

name = ""
while name != "xxx":
    name = input('Name: ')
    if name == "xxx":
        break

    how_pay = "invalid choice"
    while how_pay == 'invalid choice':
        how_pay = input("please choose a payment method (cash or credit)")
        how_pay = string_checker(how_pay,pay_method)

    subtotal = float(input("Sub total?"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | Total Payable: ${:.2f} "
          .format(name,subtotal,surcharge,total))



