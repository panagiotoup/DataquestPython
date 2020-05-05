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

# Create free games ratings
games_social_ratings = []

# list for sn and games
for row in apps_data:
    rating = float(row[7])
    genre = row[11]

    if genre == "Social Networking" or genre == "Games":
        games_social_ratings.append(rating)
print(sum(games_social_ratings))

avg_games_social = sum(games_social_ratings) / len(games_social_ratings)
print(avg_games_social)
