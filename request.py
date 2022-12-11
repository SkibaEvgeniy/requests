import requests

import json

from pprint import pprint 

import pandas as pd


url = 'https://akabab.github.io/superhero-api/api/all.json'
heroes_data = requests.get(url).json()
# pprint(heroes_data)

def get_smart_heroes(list_heroes):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    heroes = {}
    heroes_data = requests.get(url).json()
    for hero in heroes_data:
        if hero['name'] in list_heroes:
            heroes[hero['name']] = hero['powerstats']['intelligence']
    print(max(heroes, key=heroes.get))
get_smart_heroes(['Hulk', 'Captain America', 'Thanos'])
