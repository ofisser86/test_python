import requests
import json
from collections import OrderedDict

client_id = 'f40a3fcdbbb14c071eda'
client_secret = '75e407ad11e899ad2f839c64f6d0f649'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

headers = {"X-Xapp-Token" : token}
art = {}
# инициируем запрос с заголовком
with open('artsit.txt', 'r', encoding='UTF-8') as f:
    artist = f.read().splitlines()

    for i in artist:
        r = requests.get("https://api.artsy.net/api/artists/{}".format(i), headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.content.decode('utf-8'))
        art[j['sortable_name']] = j['birthday']

ordered_art = OrderedDict(sorted(art.items(), key=lambda t: t[1]))
for i in ordered_art:
    print(i)

print(ordered_art)
#print(art)