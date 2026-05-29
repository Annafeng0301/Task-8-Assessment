# docstring- Anna Feng - shoes database application
# imports
import sqlite3

# constants and variables
DATABASE = "shoes.db"


# function
def print_all_shoes():
    # Display all shoe records in a formatted manner
    '''print all the shoes nicely'''
    # Connect to the SQLite database specified by DATABASE
    db = sqlite3.connect(DATABASE)
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    # SQL query to select all records from the 'shoes' table
    sql = "SELECT * FROM shoes;"
    # Execute the SQL query using the cursor object
    cursor.execute(sql)
    # Fetch all results from the executed query and store them in the 'results' variable
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


def add_shoes():
    '''add a new shoe'''

    brand = input("Enter brand: ")
    model = input("Enter model: ")
    size = input("Enter shoe size: ")
    colour = input("Enter colour: ")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "INSERT INTO shoes (brand, model, size, colour) VALUES (?, ?, ?, ?);"

    cursor.execute(sql, (brand, model, size, colour))

    db.commit()

    if cursor.rowcount == 0:
        print("Shoe not added")
    else:
        print("Shoe added successfully")

    db.close()


def update_shoes_colour():
    '''update shoe colour'''

    shoes_id = input("Enter shoe ID to update: ")
    new_colour = input("Enter new colour: ")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "UPDATE shoes SET colour = ? WHERE id = ?;"

    cursor.execute(sql, (new_colour, shoes_id))

    db.commit()

    if cursor.rowcount == 0:
        print("No shoe found")
    else:
        print("Shoe updated successfully")

    db.close()


# main code
while True:
    user_input = input("\nWhat would you like to do.\n1. Print all shoes\n2. Print all shoes sorted by brand\n3. Print all shoes sorted by model\n4. Print all shoes sorted by size\n5. Print all shoes sorted by colour\n6. Search shoes by brand\n7. Add shoe\n8. Update shoe colour\n9. Exit\n")
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
        add_shoes()
    elif user_input == "8":
        update_shoes_colour()
    elif user_input == "9":
        break
    else:
        print("That was not an option\n")
