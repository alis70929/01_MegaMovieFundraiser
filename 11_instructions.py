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

def instructions(options):


  show_help = 'invalid choice'
  while show_help == 'invalid choice':
    show_help = input("Do you want to read the instructions")
    show_help = string_checker(show_help,options)

    if show_help == "Yes":
      print("Instructions")
      input("press enter to continue")

  
yes_no_list = [["yes", "y"], ["no", "n"]]

instructions(yes_no_list)