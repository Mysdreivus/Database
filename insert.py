import mysql.connector

# Execute:
# python3 insert.py
#

def handle_insert_command(command):
    if command == 0:
        insert_into_champion()
    elif command == 1:
        insert_into_gameplay()
    elif command == 2:
        insert_into_item()
    elif command == 3:
        insert_into_player()
    else:
        print("You entered an incorrect value")
        return

def insert_into_champion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="league"
    )
    # Accept all needed entries for the table
    champion_name = input("Enter the unique Champion name: ")
    num_of_wins = int(input("Enter number of champion wins: "))
    num_of_losses = int(input("Enter number of champion losses: "))
    win_loss_ratio = float(float(num_of_wins)/float(num_of_losses))
    time_played = int(input("Enter time played so far: "))
    most_frequent_role = input("Enter most frequent role: ")
    learning_difficulty = input("Enter learning difficulty: ")
    items_one = input("Enter item one: ")
    items_two = input("Enter item two: ")
    items_three = input("Enter item three: ")
    gameplay_type = input("Enter gameplay type: ")


    mycursor = mydb.cursor()
    sql = "INSERT INTO champion (championName, numOfWinsChamp, numOfLossChamp, winLossRatioChamp, timePlayedCumulative, mostFrequentRole, learningDifficulty, itemsFrequentlyUsed1, itemsFrequentlyUsed2, itemsFrequentlyUsed3, gameplayType) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    arg = (champion_name, num_of_wins, num_of_losses, win_loss_ratio, time_played, most_frequent_role, learning_difficulty, items_one, items_two, items_three, gameplay_type,)

    mycursor.execute(sql, arg)
    mydb.commit()

def insert_into_gameplay():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="league"
    )

    gameplay_type = input("Enter the unique gameplay type: ")
    description = input("Describe the play style: ")
    team_based = input("Team based?: ")
    champ_optimal_strat = input("What champion synergizes with this gameplay best: ")

    mycursor = mydb.cursor()
    sql = "INSERT INTO gameplay (gameplayType, descriptionPlayStyle, teamBased, champOptimalSynergy) " \
          "VALUES(%s, %s, %s, %s)"

    arg = (gameplay_type, description, team_based, champ_optimal_strat,)
    mycursor.execute(sql, arg)
    mydb.commit()

def insert_into_item():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="league"
    )

    item_name = input("Enter the unique item name: ")
    description = input("Enter the description of the item: ")
    item_cost = int(input("Enter the item's cost: "))
    item_type = input("Enter the type of item: ")

    mycursor = mydb.cursor()
    sql = "INSERT INTO item (itemName, descriptionItem, costOfItem, typeOfItem) " \
          "VALUES(%s, %s, %s, %s)"

    arg = (item_name, description, item_cost, item_type,)

    mycursor.execute(sql, arg)

    mydb.commit()


def insert_into_player():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="league"
    )

    player_name = input("Enter unique player name: ")
    most_played_champion = input("Enter most played champion name: ")
    champ_most_wins = input("Enter champion the player has most wins with: ")
    time_played = int(input("Enter time played by a player: "))
    num_wins = int(input("Enter number of wins: "))
    num_loss = int(input("Enter the number of losses: "))
    win_loss_ratio = float(num_wins)/float(num_loss)
    top_champ_one = input("Enter the number one champion for the player: ")
    top_champ_two = input("Enter the number two champion for the player: ")
    top_champ_three = input("Enter the number three champion for the player: ")

    mycursor = mydb.cursor()
    sql = "INSERT INTO player (playerName, mostPlayedChamp, champMostWins, timePlayed, numOfWinsPlayer, numOfLossesPlayer, winLossRatioPlayer, topChamp1, topChamp2, topChamp3) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    arg = (player_name, most_played_champion, champ_most_wins, time_played, num_wins, num_loss, win_loss_ratio, top_champ_one, top_champ_two, top_champ_three,)
    mycursor.execute(sql, arg)
    mydb.commit()

if __name__ == "__main__":
    insert_into_item()
