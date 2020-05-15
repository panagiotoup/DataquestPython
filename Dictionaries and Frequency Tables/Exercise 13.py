opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
df = list(read_file)

#Dataframe formulation
header = df[0]
df = df[1:]

#Index
rating_count_index = header.index('rating_count_tot')

#rating_count_tot
rating_count_tot = []

for row in df:
    rating = float(row[(rating_count_index)])
    rating_count_tot.append(rating)

minimum = min(rating_count_tot)
maximum = max(rating_count_tot)

# Dictionary creation for total ratings
total_rating = {'0 to 500,000  ratings':0,
'500,000 to 1 million ratings':0, '1 million to 2.5 million ratings':0,
'2.5 million to 3 million ratings':0 }

for row in df:
    rating = float(row[(rating_count_index)])

    if rating <= 500000:
        total_rating['0 to 500,000  ratings'] += 1

    elif 500000 > rating <= 1000000:
        total_rating['500,000 to 1 million ratings'] += 1

    elif 1000000 > rating <= 2500000:
        total_rating['1 million to 2.5 million ratings'] += 1

    elif 2500000 > rating <= 3000000:
        total_rating['2.5 million to 3 million ratings'] += 1

print(total_rating)
