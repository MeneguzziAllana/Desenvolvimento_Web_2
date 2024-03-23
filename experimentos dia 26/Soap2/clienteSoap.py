from zeep import Client

url = 'http://localhost:8000/?wsdl'
cliente = Client(url)

x = int(input("Digite a largura da imagem: "))
y = int(input("Digite a altura da imagem: "))

mdc = cliente.service.calcular_mdc(x, y)
aspect_ratio_x = x // mdc
aspect_ratio_y = y // mdc

print(f"MDC da imagem: {mdc}")
print(f"Aspect Ratio da imagem: {aspect_ratio_x}:{aspect_ratio_y}")
