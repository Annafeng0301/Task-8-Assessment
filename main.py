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
    sql = "SELECT * FROM shoes;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("brand          model               size    colour")
    for shoe in results:
        print(f"{shoe[1]:<15}{shoe[2]:<20}{shoe[3]:<8}{shoe[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_brand():
    '''print shoes sorted by brand nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM shoes ORDER BY brand ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("brand          model               size    colour")
    for shoe in results:
        print(f"{shoe[1]:<15}{shoe[2]:<20}{shoe[3]:<8}{shoe[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_model():
    '''print shoes sorted by model nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM shoes ORDER BY model ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("brand          model               size    colour")
    for shoe in results:
        print(f"{shoe[1]:<15}{shoe[2]:<20}{shoe[3]:<8}{shoe[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_size():
    '''print shoes sorted by size nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM shoes ORDER BY size ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("brand          model               size    colour")
    for shoe in results:
        print(f"{shoe[1]:<15}{shoe[2]:<20}{shoe[3]:<8}{shoe[4]:<10}")
    # loop finished here
    db.close()


def print_all_shoes_by_colour():
    '''print shoes sorted by colour nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM shoes ORDER BY colour ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("brand          model               size    colour")
    for shoe in results:
        print(f"{shoe[1]:<15}{shoe[2]:<20}{shoe[3]:<8}{shoe[4]:<10}")
    # loop finished here
    db.close()


def search_shoes_by_brand(brand):
    '''search shoes by brand'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM shoes WHERE brand = ?;"
    cursor.execute(sql, (brand,))
    results = cursor.fetchall()
    # loop through all the results
    print("brand          model               size    colour")
    if len(results) == 0:
        print("No shoes found")
    else:
        for shoe in results:
            print(f"{shoe[1]:<15}{shoe[2]:<20}{shoe[3]:<8}{shoe[4]:<10}")
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
6. Search shoes by brand
7. Exit

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
        brand = input("Enter the brand to search for: ")
        search_shoes_by_brand(brand)
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")
