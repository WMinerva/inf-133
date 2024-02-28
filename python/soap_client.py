from zeep import Client

client = Client("http://localhost:8000")
result = client.service.Saludar(nombre="Nicolas")
sumar = client.service.Sumar(a=5, b=3)
palindromo = client.service.CadenaPalindromo(cadena="Oruro")
print(result)
print(sumar)
print(palindromo)
