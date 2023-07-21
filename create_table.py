import mysql.connector

mydb =mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="password",
    database ="myDatabase"
)

mycursor =mydb.cursor()

sql_command ="""
              CREATE TABLE Student(
                  
                  roll INT,
                  first_name VARCHAR(30),
                  last_name VARCHAR(30)
                  
                  ); 

             """
mycursor.execute(sql_command)