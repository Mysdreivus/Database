#!usr/bin/local/python
# @Author Ruel Gordon
# @Date November 29, 2018


# Run with python3 main.py or python main.py

# For some reason this module will not install on my machine
# I am compiling this code in my head, I cannot test it
import mysql.connector

import retrieveAll # Import the script that has the retreive function
import showtablenames # Import the script that shows the tables
import insert # Import the script that inserts into tables
import update # Import the script to update values
import remove # Import the script that deletes

import sys
# Import name to know the type of operating system
from os import system, name

# Clear function found from geeksforgeeks
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_hello():
    sys.stdout.write("Welcome to Ruel's and Anthony's Database User Interface\n")
    sys.stdout.flush()
    return

def print_menu():
    # UI For terminal will be done here
    print("Enter 0 for Seeing all table names")
    print("Enter 1 for Select")
    print("Enter 2 for Insert")
    print("Enter 3 for Update")
    print("Enter 4 for Remove")
    print("Enter 5 for Exit")
    return

def print_insert_menu():
    # UI For terminal will be done here
    print("Enter 0 for inserting into champion table")
    print("Enter 1 for inserting into gameplay table")
    print("Enter 2 for inserting into item table")
    print("Enter 3 for inserting into player table")
    return

def print_update_menu():
    # UI For terminal will be done here
    print("Enter 0 for updating champion table")
    print("Enter 1 for updating gameplay table")
    return

def exit_interface():
    clear()
    sys.stdout.write("Sorry to see you go\n")
    sys.stdout.flush()
    exit()
    return

# This will be a driving force in the entire function
def handle_action(usr_command):
    # This is the Select Command
    if usr_command == 0:
        print("\nCurrently showing all tables")
        showtablenames.show_table_names()
        print("\n")

    elif usr_command == 1:
        retrieveAll.select_manager()
        print("\n")

    elif usr_command == 2:
        print_insert_menu()
        command = int(input("Enter value here: "))
        insert.handle_insert_command(command)

    elif usr_command == 3:
        print_update_menu()
        command = int(input("Enter value here: "))
        update.handle_update_command(command)

    elif usr_command == 4:
        print("Now removing a gameplay type from the database")
        remove.remove_from_gameplay()

    elif usr_command == 5:
        exit_interface()

    else:
        # Rejects entered key clears the screen and returns to print_menu
        clear()
        return

# Main driver program
if __name__ == '__main__':
    # Possible command names
    commands = {'0', '1', '2', '3', '4', '5'}
    clear()
    print_hello()
    while(True):
        print_menu()
        action = input("Enter value here: ")
        if action == "clear":
            clear()
        elif action not in commands:
            sys.stdout.write("Entered wrong entry")
            sys.stdout.flush()
        else:
            action = int(action)
            handle_action(action) # Handles the requested command
