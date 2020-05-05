opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
print(header)
apps_data = apps_data[1:]


#See index for elements
rating_index = header.index('user_rating')
print(rating_index)
genre_index = header.index('prime_genre')
print(genre_index)

# Create non games ratings
non_games_ratings = []

#list for non_gaming

for row in apps_data:
    rating = float(row[7])
    genre = (row[11])

    if genre != 'Games':
        non_games_ratings.append(rating)
print(sum(non_games_ratings))

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)
print('This is the avg rating of NON gaming apps',avg_rating_non_games)

#create gaming ratings
gaming_ratings = []

# list for gaming
for row in apps_data:
    rating = float(row[7])
    genre = row[11]

    if genre == "Games":
        gaming_ratings.append(rating)
print(sum(gaming_ratings))

avg_rating_games = sum(gaming_ratings) / len(gaming_ratings)
print('This is the avg rating for Gaming apps', avg_rating_games)

rating_diff = avg_rating_non_games - avg_rating_games
print(rating_diff)
