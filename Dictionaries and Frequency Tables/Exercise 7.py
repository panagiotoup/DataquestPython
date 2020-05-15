opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
header = apps_data[0]
apps_data = apps_data[1:]
print(header)

#Establish index for cont_rating index
cont_rating_index = header.index('cont_rating')

#Create dictionary
content_ratings = {'4+':0, '9+':0, '12+':0, '17+':0}

for row in apps_data:
    c_rating = row[(cont_rating_index)]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)
