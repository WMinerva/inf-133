from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler


def Saludar(nombre):
    return "!Hola, {}!".format(nombre)


def Sumar(a, b):
    return a + b


def CadenaPalindromo(cadena):
    return cadena == cadena[::-1]


dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    Saludar,
    returns={"saludo": str},
    args={"nombre": str},
)

dispatcher.register_function(
    "Sumar",
    Sumar,
    returns={"resultado": int},
    args={"a": int, "b": int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"resultado": bool},
    args={"cadena": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
