#Import data
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

#Header separation
header = apps_data[0]
apps_data = apps_data[1:]

print(header)

#Find index
price_index = header.index('price')
print('Index # for price = ', price_index)
rating_index = header.index('user_rating')
print('Index # for rating = ', rating_index)

#Create save variable
more9_rating = []
n_apps_more_9 = 0
n_apps_less_9 = 0
# Loops
for row in apps_data:
    rating = float(row[(rating_index)])
    price = float(row[(price_index)])

    if price >= 9.0:
        more9_rating.append(rating)
        n_apps_more_9 = n_apps_more_9 + 1

    if price <= 9.0:
        n_apps_less_9 = n_apps_less_9 + 1

avg_rating = sum(more9_rating) / len(more9_rating)
print(avg_rating)
