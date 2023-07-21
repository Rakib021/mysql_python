import mysql.connector

mydb = mysql.connector.connect(
    
    host ="localhost",
    user ="root",
    passwd ="password",
    database ="myDatabase"
)

mycursor = mydb.cursor()

sql_command ="""
                    INSERT INTO Student(roll,first_name,last_name)
                    VALUES(2,"RAKIB","ISLAM");

                    """
mycursor.execute(sql_command)
mydb.commit()