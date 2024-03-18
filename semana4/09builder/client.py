import requests

url = "http://localhost:8000/pizza"
headers = {"Content-type": "application/json"}

mi_pizza = {
    "tamaño": "Grande",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso"],
}
segunda_pizza = {
    "tamaño": "Mediana",
    "masa": "Gruesa",
    "toppings": ["Pepperoni", "Champiñones"],
}
response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())
