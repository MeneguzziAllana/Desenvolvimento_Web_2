import pika
import json
import sqlite3

conn = sqlite3.connect('loja.db')
c = conn.cursor()

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    c.execute("INSERT INTO pedidos (cliente, produto) VALUES (?, ?)", (pedido['cliente'], pedido['produto']))
    conn.commit()
    print("Pedido registrado:", pedido)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedidos_loja_online')
channel.basic_consume(queue='pedidos_loja_online', on_message_callback=callback, auto_ack=True)

print('Aguardando pedidos...')
channel.start_consuming()
