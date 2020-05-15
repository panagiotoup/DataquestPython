opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
header = apps_data[0]
apps_data = apps_data[1:]

#Establish index for cont_rating index
genre_index = header.index('prime_genre')

#Create dictionary
genre_counting = {}

for row in apps_data:
    genre = row[(genre_index)]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
print(genre_counting)
