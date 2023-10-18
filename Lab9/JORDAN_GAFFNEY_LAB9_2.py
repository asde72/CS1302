import sqlite3
conn = sqlite3.connect('store_inventory.db')
cursor = conn.cursor()
command = '''CREATE TABLE IF NOT
EXISTS GROCERY (\
ProductID INTEGER PRIMARY KEY,\
ProductName TEXT,\
UnitPrice FLOAT,\
Quantity FLOAT\
)'''

cursor.execute(command)
command= "INSERT INTO GROCERY VALUES (001,'Egg','2.0','23')"
cursor.execute(command)
command= "INSERT INTO GROCERY VALUES (002,'Milk','4.0','30')"
cursor.execute(command)
command= "INSERT INTO GROCERY VALUES (003,'Rice','19.99','10')"
cursor.execute(command)
# command = "INSERT INTO STUDENTS VALUES (0001, 'A B',
# 'ab1@student.gsu.edu')" 
# Execute a SELECT query to retrieve the data from the 'GROCERY' table
command = ("SELECT * FROM GROCERY")
cursor.execute(command)

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Print the table header
print("ProductID | ProductName | UnitPrice | Quantity")
print("-" * 45)

# Iterate through the rows and print each record
for row in rows:
    product_id, product_name, unit_price, quantity = row
    print(f"{product_id:9} | {product_name:11} | {unit_price:9.2f} | {quantity:7.2f}")

command = '''SELECT ProductName FROM GROCERY WHERE UnitPrice
BETWEEN 1.0 and 5.0'''
cursor.execute(command)
product_names = cursor.fetchall()
for product_name in product_names:
    print(product_name[0])



command = '''SELECT SUM(UnitPrice*Quantity) from GROCERY'''
cursor.execute(command)
sum_of_all = cursor.fetchall()
for sum in sum_of_all:
    print(sum_of_all[0])

