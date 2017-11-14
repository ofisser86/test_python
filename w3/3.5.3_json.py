import json
 
student = {
    'first_name': "Dima",
    'last_name': "K",
    'cert': True,
    'mark':[84, 84, 100]
  }

data = [student]
#print(json.dumps(data, indent=4, sort_keys=True))
# with open('dump.json', 'w') as f:
#     json.dump(data, f, indent=4, sort_keys=True)

data_json = json.dumps(data, indent=4, sort_keys=True)
# loads - получить обьект язьіка Python соответствующий строковому представлению формата json
data_again = json.loads(data_json)
print(sum(data_again[0]['mark']))