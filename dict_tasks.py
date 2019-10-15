person = {"name": "Taras", 'tel': '1234579', 'email': 'frank@gmail.com'}

# print(person.get('email'))
# print("\n")
# print(person.setdefault("addr", "Kyiv"))
# print(person)
for key, value in person.items():
    print(key, value)

print(person.keys())
team = {"team_name": "Adidas", "team_location": "NSC"}
person.update(team, name="Dima", city="Kyiv", country="Ukraine")
print(person)

dict_area = {"a": "а", "d": "д", "i": "і", "m": "м", "y": "и", "t": "т", "r": "р"}

def trans_lit(name):
    m_name = ""
    for i in name:
        m_name += dict_area.get(i)

    print(m_name.title())


try:
    trans_lit(input("Enter your name: ").lower())
except Exception:
    raise TypeError("Correct the dicionaty!!!")