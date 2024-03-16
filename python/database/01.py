import mysql.connector

ydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vp062004"
)

print(ydb)
