# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]
print(header)

# Creating length of free apps
free_apps_length = []

for row in apps_data:
    price = float(row[4])

    if price == 0.0:
        free_apps_length.append(1)
free_apps_length = sum(free_apps_length)
print(free_apps_length)

# Creating the ratings of free apps
free_apps_ratings = []

for row in apps_data:
    rating = float(row[7])
    price = float(row[4])

    if price == 0.0:
        free_apps_ratings.append(rating)
free_apps_ratings = sum(free_apps_ratings)
print(free_apps_ratings)

avg_rating_free = free_apps_ratings / free_apps_length
print(avg_rating_free)
