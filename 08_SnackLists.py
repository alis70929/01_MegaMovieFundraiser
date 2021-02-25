
import pandas
all_names = ['Rangi', 'Manaia', 'Talia', 'Arihi', ' Retu']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'AA_Orange Juice': orange_juice
}

test_data = [
    [[2, 'Popcorn'],[1, 'Pita Chips'],[1, 'AA_Orange Juice']],
    [[]],
    [[1,'Water']],
    [[1,'Popcorn'], [1, 'AA_Orange Juice']],
    [[1, "M&Ms"], [1, 'Pita Chips'], [3, 'AA_Orange Juice']]

]

count = 0
for client_order in test_data:

    for item in snack_lists:
        item.append(0)

    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print("Popcorn: ",snack_lists[0])
print("Water: ", snack_lists[1])
print("Pita Chips",snack_lists[2])
print("M&Ms:",snack_lists[3])
print("Orange Juice:" ,snack_lists[4])

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)
