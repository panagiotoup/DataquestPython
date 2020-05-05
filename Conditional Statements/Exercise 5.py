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
free_games_ratings = []

#list for non_gaming

for row in apps_data:
    rating = float(row[7])
    price = float(row[4])
    genre = (row[11])

    if price == 0.0 and genre == "Games":
        free_games_ratings.append(rating)
print(price == 0 and genre == "Games")

print(sum(free_games_ratings))
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)
print(avg_rating_free_games)
