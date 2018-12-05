# @Author Ruel Gordon
# @Date November 29, 2018

# For some reason this module will not install on my machine
# I am compiling this code in my head, I cannot test it

import mysql.connector
import showtablenames
# Execute:
# python3 retrieveAll.py or python retreiveAll.py
#

def select_manager():
    print("Do you want to print all from an entered table\n")
    answer = input("Y/N\n")
    if answer == "Y":
        showtablenames.show_table_names()
        select_all()
    elif answer == "N":
        print("Enter 0 to see a join of champions and item tables")
        print("Enter 1 to check champions with a higher than entered win rate")
        print("Enter 2 to see the max win rate")
        command = input("Enter value here: ")
        if command == "0":
            select_champion_items()
        elif command == "1":
            select_aggregate()
        elif command == "2":
            select_aggregate_real()
        else:
            print("Entered wrong entry")
    else:
        print("You made an incorrect entry")
        return


def select_all():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="league"
    )
    mycursor = mydb.cursor()
    # Accept table name from user
    table_name = input("\nEnter the table name: ")
    # Selects all the elements from a table
    command = "SELECT * FROM " + table_name
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    # Prints the results out
    for _ in myresult:
        print(_)
    return

def select_champion_items():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="league"
    )

    mycursor = mydb.cursor()
    # Selects all the elements from a table
    command = "SELECT * FROM champion INNER JOIN item ON champion.itemsFrequentlyUsed1 = item.itemName "

    mycursor.execute(command)
    myresult = mycursor.fetchall()

    # Prints the results out
    for _ in myresult:
        print(_)
    return

def select_aggregate():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="league"
    )
    win_rate = float(input("Enter win rate you would like to compare against: "))
    mycursor = mydb.cursor()
    # Selects all the elements from a table
    sql = "SELECT championName FROM champion WHERE winLossRatioChamp > %s "

    arg = (win_rate,)

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    # Prints the results out
    for _ in myresult:
        print(_)
    return

def select_aggregate_real():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="league"
    )

    mycursor = mydb.cursor()

    sql = "SELECT MAX(winLossRatioChamp) FROM champion "
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    # Prints the results out
    for _ in myresult:
        print(_)
    return


# If this is the main script being executed run the command
if __name__ == '__main__':
    select_all()
