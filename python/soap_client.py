from zeep import Client

Client = Client("https://localhost:8000")
result = Client.service.Saludar("Nicolas")
print(result)
