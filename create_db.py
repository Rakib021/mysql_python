import mysql.connector
# connect database
mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="password",
)

# create a database

mycursor = mydb.cursor()
db_name ="myDatabase"
sql_command ="create database " +db_name
mycursor.execute(sql_command)

