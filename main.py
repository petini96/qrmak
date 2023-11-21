from types import NoneType
import qrcode

import psycopg2

conn = psycopg2.connect(
    dbname="qrmak",
    user="postgres",
    password="mister",
    host="localhost"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

users = cursor.fetchall()
for user in users:
    if type(user[4]) == NoneType:
        img = qrcode.make("Olá! " + user[1]+ " faça uma recarga.")
        type(img)
        img.save(user[1] + ".png")
    else:
        img = qrcode.make("Olá! " + user[1]+ ", você tem " + str(user[4]))
        type(img)
        img.save(user[1] + ".png")
    
    
    print(users)

cursor.close()
conn.close()


# consultar o banco de dados
# cadastrar novo usuario no banco de dados
# usuario coringa

