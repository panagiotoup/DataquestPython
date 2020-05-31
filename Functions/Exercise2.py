ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for item in ratings:
    if item in content_ratings:
        content_ratings[item] += 1

    else:
        content_ratings[item] = 1
