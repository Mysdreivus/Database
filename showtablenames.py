# @Author Ruel Gordon
# @Date November 29, 2018

# For some reason this module will not install on my machine
# I am compiling this code in my head, I cannot test it

import mysql.connector

# Execute:
# python3 retrieveAll.py or python retreiveAll.py
#

def show_table_names():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="league"
    )
    mycursor = mydb.cursor()
    # Shows all tables
    mycursor.execute("SHOW tables")
    myresult = mycursor.fetchall()
    # Prints the results out
    for _ in myresult:
        print(_)
    return

# If this is the main script being executed run the command
if __name__ == '__main__':
    select_all()
