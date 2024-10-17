#elso
import json
with open('data.json', 'r') as file:
    data = json.load(file)

for nev in data:
    print(f"Név: {data['name']}, Életkor: {data['age']}")

#masodik
cars = [
    {"brand": "Toyota", "model": "Corolla", "year": 2018},
    {"brand": "Honda", "model": "Civic", "year": 2020},
    {"brand": "Ford", "model": "Mustang", "year": 2021}
]


with open('newdata.json', 'w') as file:
    data = json.dumps(cars)
    file.write(data)
    file.close()
    
#haromadikk

api_response = {
    "weather": "sunny",
    "temperature": 25,
    "city": "Budapest"
}

print(f"Város: {api_response['city']}")
print(f"Időjárás: {api_response['weather']}")
print(f"Hőmérséklet: {api_response['temperature']} °C")

