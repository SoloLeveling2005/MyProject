import json
import random
import time

import jsonlines as jsonlines

# data = {
#    "id_human": f"{time.time()}{random.randint(1000,9999)}",
#     "name": "Mansur",
#     "time_birth": f"{time.time()}",
#     "gender": "man",
#     "married": False,
#     "time_married": "",
# }

data = {
    "id_human": f"{time.time()}{random.randint(1000,9999)}",
    "name": "Nastya",
    "time_birth": f"{time.time()}",
    "gender": "woman",
    "married": False,
    "time_married": "",
}

with open('humans.jsonlines', 'a', encoding='utf-8') as file:
    json.dump(data, file)
    file.write('\n')

with jsonlines.open('humans.jsonlines') as reader:
    for obj in reader:
        print(obj)