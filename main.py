# docstring- Anna Feng- airb=plane database applicantion
# imports
import sqlite3

# constants and variables
DATABASE = "shoes.db"


# function
def print_all_shoes():
    '''print all the shoes nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          brand   model size colour")
    for shoes in results:
        print(f"{shoes[1]:<15}{shoes[2]:<20}{shoes[3]:<8}{shoes[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_brand():
    '''print all the shoes nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          brand   model size colour")
    for shoes in results:
        print(f"{shoes[1]:<15}{shoes[2]:<20}{shoes[3]:<8}{shoes[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_model():
    '''print all the shoes nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          brand   model size colour")
    for shoes in results:
        print(f"{shoes[1]:<15}{shoes[2]:<20}{shoes[3]:<8}{shoes[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_size():
    '''print all the shoes nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          brand   model size colour")
    for shoes in results:
        print(f"{shoes[1]:<15}{shoes[2]:<20}{shoes[3]:<8}{shoes[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_colour():
    '''print all the shoes nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          brand   model size colour")
    for shoes in results:
        print(f"{shoes[1]:<15}{shoes[2]:<20}{shoes[3]:<8}{shoes[4]:<10}")
    # loop finished here
    db.close()


# main code
while True:
    user_input = input(
"""
What would you like to do.
1. Print all shoes
2. Print all shoes sorted by brand
3. Print all shoes sorted by model
4. Print all shoes sorted by size
5. Print all shoes sorted by colour
6. Exit
""")
    if user_input == "1":
        print_all_shoes()
    elif user_input == "2":
        print_all_shoes_by_brand()
    elif user_input == "3":
        print_all_shoes_by_model()
    elif user_input == "4":
        print_all_shoes_by_size()
    elif user_input == "5":
        print_all_shoes_by_colour()
    elif user_input == "6":
        break
    else:
        print("That was not an option\n")
