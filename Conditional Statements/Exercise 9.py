opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

#Header
price_index = apps_data[0].index('price')

for row in apps_data[1:]:
    price = float(row[(price_index)])
    if price == 0.0:
        row.append('free')
    else:
        row.append('non-free')

apps_data[0].append('free_or_not')
print(apps_data[:6])
