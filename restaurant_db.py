import sqlite3
from Users import *
from Employee import *
from Beverages import *
from Appetizers import *
from Main_Course import *
from Dessert import *
from Billing_Information import *

conn = sqlite3.connect('C:\sqlite\gui\Restaurant_Database.db')
c = conn.cursor()


def insert_beverages(beverage):
    with conn:
        c.execute("INSERT INTO Beverages VALUES(:item_id, :item_name, :alcoholic, :price, :quantity)",
                  {'item_id': beverage.item_id, 'item_name': beverage.item_name, 'alcoholic': beverage.alcoholic,
                   'price': beverage.price, 'quantity': beverage.quantity})

def insert_appetizer(appetizer):
    with conn:
        c.execute("INSERT INTO Appetizers VALUES(:item_id, :item_name , :quantity, :price)",
                  {'item_id': appetizer.item_id, 'item_name': appetizer.item_name, 'quantity': appetizer.quantity,
                   'price': appetizer.price})

def insert_maincourse(maincourse):
    with conn:
        c.execute("INSERT INTO Main_Course VALUES(:item_id, :item_name , :quantity, :price)",
                  {'item_id': maincourse.item_id, 'item_name': maincourse.item_name, 'quantity': maincourse.quantity,
                   'price': maincourse.price})

def insert_dessert(dessert):
    with conn:
        c.execute("INSERT INTO Dessert VALUES(:item_id, :item_name , :quantity, :price)",
                  {'item_id': dessert.item_id, 'item_name': dessert.item_name, 'quantity': dessert.quantity,
                   'price': dessert.price})

def insert_billing_info(billing_info):
    with conn:
        c.execute("INSERT INTO Billing_Information VALUES(:first_name, :last_name, :address, :phone, :zip_code, :email)",
                  {'first_name': billing_info.first_name, 'last_name': billing_info.last_name, 'address': billing_info.address,
                   'phone': billing_info.phone, 'zip_code': billing_info.zip_code, 'email': billing_info.email})


#This function will insert data from the application to the database
def insert_user(user):
    with conn:
        c.execute("INSERT INTO Users VALUES(:unique_id, :first_name, :last_name, :username, :password, :employee)",
                  {'unique_id': user.unique_id, 'first_name': user.first_name, 'last_name': user.last_name,
                   'username': user.username, 'password': user.password, 'employee': user.employee})

#This function will select a user from the database and show it to the screen based on last name
def get_user_by_name(lname):
    c.execute("SELECT * FROM Users WHERE last_name=:last_name", {'last_name':lname})
    return c.fetchall()


conn.commit()
conn.close()

