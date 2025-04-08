import psycopg2
import csv

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                try:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
                except Exception as e:
                    print(f"Error inserting {row}: {e}")
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Entry added.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

def update_data():
    field = input("Update (1) Name or (2) Phone? Enter 1 or 2: ")
    identifier = input("Search by phone or name: ")
    new_value = input("Enter new value: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        if field == "1":
            cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s OR first_name = %s", (new_value, identifier, identifier))
        elif field == "2":
            cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s OR first_name = %s", (new_value, identifier, identifier))
        conn.commit()
        print("Update successful.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

def query_data():
    field = input("Filter by (1) Name or (2) Phone? Enter 1 or 2: ")
    value = input("Enter filter value: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        if field == "1":
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{value}%",))
        elif field == "2":
            cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", (f"%{value}%",))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

def delete_data():
    value = input("Enter name or phone to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", (value, value))
        conn.commit()
        print("Deleted.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# Create table on run
if __name__ == '__main__':
    create_table()
    print("PhoneBook Ready.")

query_data()