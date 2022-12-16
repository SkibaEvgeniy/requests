import requests

import json

from pprint import pprint 

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


class YaUploader:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type' : 'application/json',
            'Authorization' : f'OAuth {self.token}'
        }

    def upload(self, file_path):
        """Метод загружает файлы по списку на яндекс диск"""
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        # print(response.status_code)
        # pprint(response.json())
        upload_url = response.json()['href']
        # pprint(upload_url)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка произошла успешно!')
      
      
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    uploader.upload(path_to_file)