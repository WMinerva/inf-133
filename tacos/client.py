import requests

url = "http://localhost:8000/"
headers = {"Content-type": "application/json"}

# GET /tacos
response = requests.get(url)
print(response.json())

# POST /tacos
mi_taco = {
    "base": "Mediano",
    "guiso": "Si",
    "salsa": "picante",
    "toppings": ["chorizo", "gallo"],
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())

# PUT /tacos/1
edit_taco = {
    "base": "Mediano",
    "guiso": "No",
    "salsa": "miel",
    "toppings": ["palta", "queso"],
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())

# DELETE /tacos/1

response = requests.delete(url + "/1")
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())
