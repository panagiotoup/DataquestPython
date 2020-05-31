opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
df = list(read_file)

def freq_table(index, df):
    frequency_table = {}

    for row in df[1:]:
        value = row[index]

        if value in frequency_table:
            frequency_table[value] += 1

        else:
            frequency_table[value] = 1

    return frequency_table

ratings_ft = freq_table(7, df)
print(rating_ft)
