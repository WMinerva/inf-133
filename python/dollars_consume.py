from zeep import Client  # usamos zeep para consumir un WS SOAP

Client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result = Client.service.NumberToDollars(89)
print(result)
