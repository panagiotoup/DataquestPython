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
    elif price > 0 and price < 20:
        row.append('affordable')
    elif price >= 20 and price < 50:
        row.append('expensive')
    elif price > 50:
        row.append('very expensive')

apps_data[0].append('price_label')
print(apps_data[:6])
