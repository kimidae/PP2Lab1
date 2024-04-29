import psycopg2
import csv


conn = psycopg2.connect(
    host='localhost',
    dbname='phonebook',
    user='postgres',
    password='040403'
)

cur = conn.cursor()

todo = input("What would you like to do? Add from csv, concole, delete or update? Or find contact? \n")
if todo == "console":
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook_table (
            name VARCHAR(255),
            surname VARCHAR(255),
            phone_num VARCHAR(255) PRIMARY KEY
        )
    ''')
    name = input("Name: ")
    surname = input("Surname: ")
    number = input("Number: ")
    cur.execute("""
            INSERT INTO phonebook_table (name, surname, phone_num) 
        VALUES (%s, %s, %s)
    """, (name, surname, number))

    conn.commit()

elif todo == "csv":
    another_path = input("Enter your path: \n")
    with open(another_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook_table (name, surname, phone_num) 
                VALUES (%s, %s, %s)
            """, row)

    conn.commit()

elif todo == "update":
    todo = input("What exactly do you want to update: name, surname or number? \n")
    if todo == "number":
        name = input("Enter name: \n")
        surname = input("Enter surname: \n")
        num = input("Enter new number: \n")
        cur.execute("""
            UPDATE phonebook_table
            SET phone_num = %s
            WHERE name = %s AND surname=%s
        """, (num, name, surname))
    elif todo == "name":
        num = input("Enter number: \n")
        name = input("Enter new name: \n")
        cur.execute("""
            UPDATE phonebook_table
            SET name = %s
            WHERE phone_num = %s
        """, (name, num))
    elif todo == "surname":
        num = input("Enter number: \n")
        name = input("Enter new name: \n")
        cur.execute("""
            UPDATE phonebook_table
            SET name = %s
            WHERE phone_num = %s
        """, (name, num))
elif todo=="delete":
    inputhz = input("Enter name and surname or number: \n")
    cur.execute("""
        DELETE FROM phonebook_table WHERE phone_num = %s OR CONCAT(name, ' ', surname) = %s
    """, (inputhz, inputhz))

elif todo == "find" or todo=="find contact":
    pattern=input("What do you want to find? \n")
    cur.execute("""
        SELECT * FROM phonebook_table 
        WHERE LOWER(name) LIKE %s 
        OR LOWER(surname) LIKE %s 
        OR LOWER(phone_num) LIKE %s
    """, ('%' + pattern.lower() + '%', '%' + pattern.lower() + '%', '%' + pattern.lower() + '%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)


cur.execute("SELECT * FROM phonebook_table")
rows = cur.fetchall()
csv_file_path = "phonebook_data.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "surname", "phone_num"])
    writer.writerows(rows)

conn.commit()
conn.close()
