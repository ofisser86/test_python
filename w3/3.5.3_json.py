import json
 
student = {
    'first_name': "Dima",
    'last_name': "K",
    'cert': True,
    'mark':[84, 84, 100]
  }

data = [student]
print(json.dumps(data, indent=4, sort_keys=True))
