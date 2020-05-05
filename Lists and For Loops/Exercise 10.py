opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]
length = len(apps_data[7])

print('Length is', length)
print('Header is',header[7])

rating_sum = 0

for row in apps_data:
    rating = float(row[7])
    rating_sum = rating_sum + rating
print('Rating sum is', rating_sum)

avg_rating = rating_sum/7197

print('Average is', avg_rating)
