content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
for key in content_ratings:
    proportion = content_ratings[key] / total_number_of_apps
    c_ratings_proportions[key] = proportion

c_ratings_percentages = {}
for key in c_ratings_proportions:
    percentage = c_ratings_proportions[key] * 100
    c_ratings_percentages[key] = percentage
