content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for rating in content_ratings:
    content_ratings[rating] /= total_number_of_apps
    content_ratings[rating] *= 100

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['9+'] + content_ratings['12+']

print(percentage_17_plus,'%'' of the apps are 17+ ')
print(percentage_15_allowed,'%' ' of the apps can be downloaded by 15 year olds')
