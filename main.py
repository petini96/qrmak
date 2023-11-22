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


def generateQr(userId):
  img = qrcode.make(userId)
  type(img)
  img.save("qr-user-" + str(userId) + ".png")
  print("Hello from a function")

def getCredits(userId):
    cursor.execute("SELECT total_value FROM users WHERE id = " + str(userId))
    userTotalValue = cursor.fetchone()
    print(str(userTotalValue))

def getAllUsers():
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
        print(user[1])

def setCredits(userId, value):
    cursor.execute("UPDATE users SET total_value = "+str(value)+" WHERE id = " + str(userId))

setCredits(3, 10.0)
getCredits(3)
cursor.close()
conn.close()


# consultar o banco de dados
# cadastrar novo usuario no banco de dados
# usuario coringa

