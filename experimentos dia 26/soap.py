from zeep import Client

url = 'http://www.dneonline.com/calculator.asmx?WSDL'
cliente = Client(url)

adicao = cliente.service.Add(13, 11)
subtracao = cliente.service.Subtract(72, 24)
multiplicacao = cliente.service.Multiply(3, 8)
divisao = cliente.service.Divide(36, 6)

print("Resultados:")
print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
