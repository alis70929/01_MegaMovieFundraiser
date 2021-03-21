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
    show_help = input("Do you want to read the instructions: ")
    show_help = string_checker(show_help,options)

    if show_help == "Yes":
      print("****** Instructions ******* ")
      print("To use this program you must - ")
      print(" - put in a customers name")
      print(" - put in a customers age")
      print(" - while entering snacks type in xxx or n to finish inputting snacks ")
      print(" - put number of snacks wanted infront of of that snack \n E.g 2 pita chips")
      print(" - then enter whether the user is paying with cash or credit")
      print(" when finished inputting customers type in xxx to finish \n the program will show you a short summary and put all inputted customer data in a .csv file")
      print()
      input("press enter to continue")

  
yes_no_list = [["yes", "y"], ["no", "n"]]

instructions(yes_no_list)