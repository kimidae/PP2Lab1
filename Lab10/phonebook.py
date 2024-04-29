import psycopg2
import csv


conn = psycopg2.connect(
    host='localhost',
    dbname='phonebook',
    user='postgres',
    password='040403'
)

cur = conn.cursor()

todo = input("What would you like to do? Add from csv, concole, delete or update? \n")
if todo == "console":
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook_table (
            name VARCHAR(255) PRIMARY KEY,
            phone_num VARCHAR(255)
        )
    ''')
    name = input("Name: ")
    number = input("Number: ")
    cur.execute("""
            INSERT INTO phonebook_table (name, phone_num) 
        VALUES (%s, %s)
    """, (name, number))

    conn.commit()

elif todo == "csv":
    another_path = input("Enter your path: \n")
    with open(another_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook_table (name, phone_num) 
                VALUES (%s, %s)
            """, row)

    conn.commit()

elif todo == "update":
    todo = input("What exactly do you want to update: name or number? \n")
    if todo == "number":
        name = input("Enter name \n")
        num = input("Enter new number \n")
        cur.execute("""
            UPDATE phonebook_table
            SET phone_num = %s
            WHERE name = %s
        """, (num, name))
    elif todo == "name":
        num = input("Enter number \n")
        name = input("Enter new name \n")
        cur.execute("""
            UPDATE phonebook_table
            SET name = %s
            WHERE phone_num = %s
        """, (name, num))
elif todo=="delete":
    inputhz = input("Enter name or number: \n")
    cur.execute("""
        DELETE FROM phonebook_table WHERE phone_num = %s OR name=%s
    """, (inputhz, inputhz))

cur.execute("SELECT * FROM phonebook_table")
rows = cur.fetchall()
csv_file_path = "phonebook_data.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "phone_num"])
    writer.writerows(rows)

conn.commit()
conn.close()
