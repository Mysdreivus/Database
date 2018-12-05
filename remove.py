# @Author Ruel Gordon
# @Date November 29, 2018

# For some reason this module will not install on my machine
# I am compiling this code in my head, I cannot test it

import mysql.connector

def remove_from_gameplay():

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="league"
    )
    mycursor = mydb.cursor()
    # Accept table name from user
    gameplay_type = input("\nEnter the gameplay type you want to remove: ")
    # Selects all the elements from a table
    sql = "DELETE FROM gameplay WHERE gameplayType=%s"

    arg = (gameplay_type,)
    mycursor.execute(sql, arg)
    mydb.commit()
