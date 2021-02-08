
name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:
    name = input("Name:")
    count += 1

if count < max_tickets:
    print("There are {} tickets left".format(max_tickets-count))
else:
    print("All tickets have been sold")