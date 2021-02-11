
name = ""
count = 0
max_tickets = 5

while count < max_tickets:
    if(max_tickets - count ) == 1:
        print("")
        print("!!! There is only 1 ticket left !!!")
        print("")
    else:
        print("You have {} tickets left".format(max_tickets - count))

    name = input("Name:")
    if name == "xxx":
        break
    count += 1

if count < max_tickets:
    print("You have sold {}".format((count)))
    print("There are {} tickets left".format(max_tickets-count))
else:
    print("All tickets have been sold")