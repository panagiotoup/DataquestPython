opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

all_ratings = []

for row in apps_data:
    rating = float(row[7])
    all_ratings.append(rating)
#print('This are all the ratings ->',all_ratings)
print('The sum of the ratings ->',sum(all_ratings))

avg_rating = sum(all_ratings)/len(apps_data)
print(avg_rating)
