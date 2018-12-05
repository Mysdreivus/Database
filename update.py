

import mysql.connector

def handle_update_command(command):
    if command == 0:
        update_champion()
    elif command == 1:
        update_gameplay()
    elif command == 2:
        update_item()
    elif command == 3:
        update_player()
    else:
        print("You entered an incorrect value")
        return

def update_champion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="league"
    )
    print("You can update the number of wins and losses of this champion")
    champ_name = input("Enter the champion name: ")
    num_wins = int(input("Enter the number of wins: "))
    num_losses = int(input("Enter the number of losses: "))
    win_loss_ratio = float(num_wins) / float(num_losses)

    mycursor = mydb.cursor()
    sql = "UPDATE champion SET numOfWinsChamp = %s, numOfLossChamp = %s, winLossRatioChamp = %s "\
          "WHERE championName = %s"

    arg = (num_wins, num_losses, win_loss_ratio, champ_name,)
    mycursor.execute(sql, arg)
    mydb.commit()

def update_gameplay():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="league"
    )
    print("You can update the champion optimal with this strategy")
    gameplay_type = input("Enter the gameplay type: ")
    champion = input("Enter the champion name: ")

    mycursor = mydb.cursor()
    sql = "UPDATE gameplay SET champOptimalSynergy = %s "\
          "WHERE gameplayType = %s"

    arg = (champion, gameplay_type)
    mycursor.execute(sql, arg)
    mydb.commit()
