# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price != 0.0:
        non_free_apps_ratings.append(rating)

avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)
print(avg_rating_non_free)
