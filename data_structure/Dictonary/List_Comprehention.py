import random

city_name = ['Paris','Londom','Rona','Berlin','Madrin']

new_dict = {city:random.randint(20,30) for city in city_name}
print(new_dict)