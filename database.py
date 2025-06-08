import sqlite3
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Used by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def remove_table():
    conn=sqlite3.connect(resource_path("flights.db"))
    cur=conn.cursor()
    cur.execute("DROP TABLE reservation")
    conn.commit()
    conn.close()
def table_init():
    conn=sqlite3.connect(resource_path("flights.db"))
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTs 
            reservation(fullName TEXT NOT NULL,
            flightNumber INTEGER ,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seatNumber INTEGER )""")
    flights=[
        ('Hazem Bakr',321,'Cairo','Sharqia','30/4/25',12),
        ('Bakr Ragab',343,'Paris','Makkah','30/3/25',12),
        ('Ahmed Samy',678,'Tokyo','Madrid','30/2/25',12),
        ('Mostafa Mahmoud',120,'Maldifs','Paris','30/1/25',12),
        ('Abdelrahman Mahmoud',192,'Austria','London','30/12/24',12),
        ('Mohamed Alaa',2392,'Makkah','Al Sharqia','30/11/24',12),
        ('Hazem Bakr',4321,'sharqia','Holly Wood','30/4/25',12),
        ('Hazem Bakr',3454,'Cairo','Austria','30/4/25',12),
    ]
    cur.executemany("INSERT INTO reservation VALUES(?,?,?,?,?,?)",flights)
    conn.commit()
    conn.close()
def EDIT_reservation(id, name, flight_num, departure, destination, date, seat_number):
    conn = sqlite3.connect(resource_path("flights.db"))
    cur = conn.cursor()
    cur.execute("""
        UPDATE reservation
        SET date = ?,
            fullName = ?,
            seatNumber = ?,
            destination = ?,
            departure = ?,
            flightNumber = ?
        WHERE rowid = ?
    """, (date, name, seat_number, destination, departure, flight_num, id))
    conn.commit()
    conn.close()

def remove_reservation(id):
    conn=sqlite3.connect(resource_path("flights.db"))
    cur=conn.cursor()
    cur.execute(f"DELETE FROM reservation WHERE rowid = {id} ")
    conn.commit()
    conn.close()
def insert_resrervation(name,flight_num,departure,destination,date,seat_number):
    return_stat=''
    def is_not_integer(value):
        try:
            int(value)
            return False  # It **is** an integer
        except ValueError:
            return True  # It is NOT an integer
    if name ==None:
        return_stat += 'Invalid Full Name\n'
    if is_not_integer(flight_num):
        return_stat += 'Invalid Flight Number\n'
    if departure ==None:
        return_stat += 'Invalid departure\n'
    if destination==None:
        return_stat+='Invalid destination\n'
    if date== None:
        return_stat+='Invalid data\n'
    if is_not_integer(seat_number):     
        return_stat+='Invalid Seat Number\n'
    if return_stat=='':
        conn=sqlite3.connect(resource_path("flights.db"))
        cur=conn.cursor()
        cur.execute(f"""INSERT INTO reservation  
                    VALUES('{name}',{flight_num},'{departure}','{destination}','{date}',{seat_number})""")
        conn.commit()
        conn.close()
        return "Successfully added"
    else:
        return return_stat
def display(displayfor):
    conn=sqlite3.connect(resource_path("flights.db"))
    cur=conn.cursor()
    def search(searchfor):
        cur.execute(f"""Select rowid,* from reservation 
                    WHERE 
                    destination LIKE '%{searchfor}%' OR
                    departure LIKE '%{searchfor}%' OR 
                    seatNumber LIKE '%{searchfor}%' OR 
                    fullName LIKE '%{searchfor}%' 
                    ORDER BY rowid """)
        return cur.fetchall()
    if displayfor == None:
        cur.execute("Select rowid,* from reservation ORDER BY rowid ")
        data=cur.fetchall()
    else:
        data=search(displayfor)
    conn.commit() 
    conn.close()
    return data

# remove_table()
# table_init()
data = display(None)
for i in data:
    print(i)