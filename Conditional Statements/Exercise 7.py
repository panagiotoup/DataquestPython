opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
print(header)
apps_data = apps_data[1:]


#See index for elements
rating_index = header.index('user_rating')
print('Index # of rating', rating_index)
genre_index = header.index('prime_genre')
print('Index # of genre', genre_index)
price_index = header.index('price')
print('Index # of price', price_index)

# Create ratings variable

nf_rating_sn_games = []

for row in apps_data:
    price = float(row[4])
    rating = float(row[7])
    genre = row[11]

    if (genre == 'Social Networking' or genre == 'Games') and price > 0.0:
        nf_rating_sn_games.append(rating)

print(sum(nf_rating_sn_games))
avg_non_free = sum(nf_rating_sn_games) / len(nf_rating_sn_games)
print(avg_non_free)
