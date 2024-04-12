import pika
import json

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print("Pedido enviado para envio/logística:", pedido)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedidos_processados')
channel.basic_consume(queue='pedidos_processados', on_message_callback=callback, auto_ack=True)

print('Aguardando pedidos processados...')
channel.start_consuming()
