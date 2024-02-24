import mysql.connector

# Conectando ao banco de dados MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="allana1234",
    database="monolito"
)

print("Conexão bem-sucedida!")