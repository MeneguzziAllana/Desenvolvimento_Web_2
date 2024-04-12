import pika
import json

#conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedidos_loja_online')

#envio de pedidos
pedidos = [
    {"cliente": "Cliente A", "produto": "Produto X"},
    {"cliente": "Cliente B", "produto": "Produto Y"},
    {"cliente": "Cliente C", "produto": "Produto Z"}
]

#envia cada pedido para a fila
for pedido in pedidos:
    channel.basic_publish(exchange='',
                          routing_key='pedidos_loja_online',
                          body=json.dumps(pedido))
    print("Pedido enviado:", pedido)

connection.close()
