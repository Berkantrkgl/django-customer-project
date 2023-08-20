import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'admin',
    passwd = 'password'
)

# prepare a cursor object
cursortObject = dataBase.cursor()

cursortObject.execute("CREATE DATABASE elderco")
print('ALL DONE!')
