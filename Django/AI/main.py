import random
import re
import time
from threading import Thread

from jsonlines import jsonlines


class System_control:
    def __init__(self):
        self.year = 60
        pass

    def get_married(self):
        pass

        # time.time() + random.randint(1000,9999)


class The_human_brain:
    def __init__(self, id_human, name, time_birth, gender, married, time_married):
        system = System_control()
        self.id = id_human
        self.name = name
        self.age = (round(time.time()) - round(float(time_birth))) / system.year
        self.time_birth = time_birth
        self.gender = gender
        self.married = married
        self.time_married = time_married


def life(human):
    print(human)
    age = The_human_brain(human["id_human"], human["name"], human["time_birth"],
                          human["gender"], human["married"], human["time_married"], )
    while True:
        print(f'Возраст:{age.name}={round(age.age)}')
        time.sleep(3)


with jsonlines.open('humans.jsonlines') as data:
    for human in data:
        human_life = Thread(target=life, args=(human,))
        human_life.start()
