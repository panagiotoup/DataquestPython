opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

#Size_bytes index
header = apps_data[0]
size_bytes_index = header.index('size_bytes')

data_sizes = []

for row in apps_data[1:]:
    size = float(row[size_bytes_index])
    data_sizes.append(size)

min_size = min(data_sizes)
max_size = max(data_sizes)
