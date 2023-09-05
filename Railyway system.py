#Owner:SIDDHARTH KALYAN


import mysql.connector
import os
import platform

mydb = mysql.connector.connect(host="localhost", user="root", passwd="232004")
mycursor = mydb.cursor()

def dataBase():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Railway_System")
    mycursor.execute("USE Railway_System")
    railresmenu()

def Tables():
    print("Creating Train detail table")
    sql = "CREATE TABLE IF NOT EXISTS traindetail (" \
          "tname VARCHAR(30)," \
          "tnum INT," \
          "ac1 INT," \
          "ac2 INT," \
          "ac3 INT," \
          "slp INT);"
    mycursor.execute(sql)
    print("Traindetail Table created")

    print("Creating Passengers table")
    sql = "CREATE TABLE IF NOT EXISTS Passengers (" \
          "pname CHAR(25)," \
          "age CHAR(3)," \
          "trainno CHAR(15) NOT NULL," \
          "noofpas INT(3)," \
          "cls CHAR(5)," \
          "amt INT," \
          "status VARCHAR(10)," \
          "pnrno INT);"
    mycursor.execute(sql)
    print("Passengers table created")
    railresmenu()

def railresmenu():
    print("1. Access Database")
    print("2. Create Tables if not Exist")
    print("---------Railway Reservation------------")
    print("3. Train Detail")
    print("4. Reservation of Ticket")
    print("5. Cancellation of Ticket")
    print("6. Display PNR status")
    print("7. Quit")
    n = int(input("Enter your choice: "))
    if n == 1:
        dataBase()
    elif n == 2:
        Tables()
    elif n == 3:
        traindetail()
    elif n == 4:
        reservation()
    elif n == 5:
        cancel()
    elif n == 6:
        displayPNR()
    elif n == 7:
        exit(0)
    else:
        print("Wrong choice")

def reservation():
    global pnr
    l1 = []
    pname = input("Enter passenger name: ")
    l1.append(pname)
    age = input("Enter age of passenger: ")
    l1.append(age)
    trainno = input("Enter train number: ")
    l1.append(trainno)
    np = int(input("Enter number of passengers: "))
    l1.append(np)

    print("Select a class you would like to travel in")
    print("1. AC FIRST CLASS")
    print("2. AC SECOND CLASS")
    print("3. AC THIRD CLASS")
    print("4. SLEEPER CLASS")
    cp = int(input("Enter your choice: "))
    if cp == 1:
        amount = np * 1000
        cls = 'ac1'
    elif cp == 2:
        amount = np * 800
        cls = 'ac2'
    elif cp == 3:
        amount = np * 500
        cls = 'ac3'
    else:
        amount = np * 350
        cls = 'slp'

    l1.append(cls)
    print("Total amount to be paid:", amount)
    l1.append(amount)
    pnr = pnr + 1
    print("PNR Number:", pnr)
    print("Status: confirmed")
    sts = 'conf'
    l1.append(sts)
    l1.append(pnr)
    train1 = tuple(l1)

    sql = "INSERT INTO passengers(pname, age, trainno, noofpas, cls, amt, status, pnrno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, train1)
    mydb.commit()
    print("Insertion completed")
    print("Go back to menu")
    print('\n' * 10)
    print("===================================================================")
    railresmenu()

# Define pnr outside any function
pnr = 0

def traindetail():
    print("Train Details")
    ch = 'y'
    while ch == 'y':
        l = []
        name = input("Enter train name: ")
        l.append(name)
        tnum = int(input("Enter train number: "))
        l.append(tnum)
        ac1 = int(input("Enter number of AC 1 class seats: "))
        l.append(ac1)
        ac2 = int(input("Enter number of AC 2 class seats: "))
        l.append(ac2)
        ac3 = int(input("Enter number of AC 3 class seats: "))
        l.append(ac3)
        slp = int(input("Enter number of sleeper class seats: "))
        l.append(slp)
        train = tuple(l)

        sql = "INSERT INTO traindetail(tname, tnum, ac1, ac2, ac3, slp) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, train)
        mydb.commit()
        print("Insertion completed")
        ch = input("Do you want to insert more train details? (yes/no): ")
        print('\n' * 3)
        print("===================================================================")
    railresmenu()

def cancel():
    print("Ticket cancel window")
    pnr_input = input("Enter PNR for cancellation of Ticket: ")
    pn = (pnr_input,)
    sql = "UPDATE passengers SET status = 'deleted' WHERE pnrno = %s"
    mycursor.execute(sql, pn)
    mydb.commit()
    print("Deletion completed")
    print("Go back to menu")
    print('\n' * 10)
    print("===================================================================")
    railresmenu()

def displayPNR():
    print("PNR STATUS window")
    pnr_input = input("Enter PNR NUMBER: ")
    pn = (pnr_input,)
    sql = "SELECT * FROM passengers WHERE pnrno = %s"
    mycursor.execute(sql, pn)
    res = mycursor.fetchall()
    print("PNR STATUS are as follows: ")
    print("(pname, age, trainno, noofpas, cls, amt, status, pnrno)")
    for x in res:
        print(x)
    print("Go back to menu")
    print('\n' * 3)
    print("===================================================================")
    railresmenu()

railresmenu()
