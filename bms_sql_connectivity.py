# BANK MANAGEMENT SYSTEM (Python + Mysql connectivity)

from prettytable import PrettyTable # MUST INSTALL , pip install prettytable
import random
import mysql.connector 

mydatabase = mysql.connector.connect(host="localhost", user="root", password="c)de")

# CREATING DATABASE & TABLE

mycursor = mydatabase.cursor()
mycursor.execute("create database if not exists bank_management_system")
mycursor.execute("use bank_management_system")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS signup(username varchar(30) primary key, password varchar(30))")

# SIGNUP function

def signup():
    username = (input("USERNAME: "))
    password = input("PASSWORD: ")
    mycursor.execute(f"insert into signup values('{username}','{password}')")
    mydatabase.commit()
    print("\t\t\t***********<<<<<<<SIGNUP SUCCESSFULLY>>>>>>>*************")
    print('Login to continue')
    login()

usr_name=""
# LOGIN function
def login():
    username = input("USERNAME: ")
    global usr_name
    usr_name=username 
    password = input("PASSWORD: ")
    mycursor = mydatabase.cursor()
    mycursor.execute("select username from signup")
    user1 = mycursor.fetchall()  
    mydatabase.commit()
    user2 = []
    for i in range(len(user1)):
        user2.append(user1[i][0])

    mycursor = mydatabase.cursor()
    mycursor.execute('select password from signup')
    pwd1 = mycursor.fetchall()
    pwd2 = []
    for i in range(len(pwd1)):
        pwd2.append(pwd1[i][0])

    if (username not in user2) or (password not in pwd2):
        print("WRONG USERNAME OR PASSWORD !!")
        t = 1
        while True:
            t = int(input("Press 1 for Try again or, \n Press 2 for exit : "))
            if t == 1:
                login()
            else:
                exit()
    else:
        mycursor = mydatabase.cursor()
        mycursor.execute(
            f'select username from signup where username="{username}"')
        user = mycursor.fetchone()
        mycursor.execute(
            f'select password from signup where password="{password}"')
        pwd = mycursor.fetchone()
        print("\t\t\t***********<<<<<<<LOGIN SUCCESSFULLY>>>>>>>*************")

        mydatabase.commit()
        while True:
            print("\n\t\t <<< MAIN MENU >>>")
            print("Press 1 to open new account")
            print("Press 2 to deposit amount")
            print("Press 3 to withdraw amount")
            print("Press 4 for FUND TRANSFER (RTGS|NET BANKING|UPI)")
            print("Press 5 for balance enquiry")
            print("Press 6 for ALL ACCOUNT HOLDER LIST")
            print(" Press 7 to delete account")
            print("Press 8 to EXIT")
            print("Press 9 to logout")
            command = (input("enter your choice: "))

            if command == '1':
                openAccount()
            elif command == '2':
                num = input(
                    "\tEnter The account No. to\n\twhich money is to be deposit : ")
                num1 = int(input("Enter amount to deposit: ₹"))

                deposit(num, num1)
            elif command == '3':
                num = int(
                    input("\tEnter The account No. to\n\twhich money is to be withrawn : "))
                num1 = int(input("Enter amount to withdraw: ₹"))

                withdraw(num, num1)

            elif command == '4':
                num = int(input("\tEnter 'Your' account No. : "))
                num1 = int(input("\tEnter 'Beneficiary' account No. : "))
                num2 = int(input("Enter amount to transfer(send): ₹"))
                fund_trf(num, num1, num2)

            elif command == '5':
                num = int(input("\tEnter The account No. : "))
                bal_enq(num)

            elif command == '6':
                ac_list()

            elif command == '7':
                close()            
            elif command == '9':
                print("\n\t<< Login again >>\n")

                login()

            elif command == '8':
                print("\tThanks for using Bank Managemnt System")
                print('''\n\tCOMPUTER SCIENCE PROJECT
                            Created by ROHIT BURMAN
                            NARAYANA SCHOOL 
                            class XII
                        
                ''')
                break
            else:
                print("Invalid choice")
            print("")
            input()


def openAccount():
    mycursor.execute(
        "create table if not exists acc(acc_no int primary key,name varchar(30),address varchar(30),total_balance int(8))")
    mycursor.execute(
        "create table if not exists amount (acc_no int primary key,name varchar(30),total_balance int(8))")
    mydatabase.commit()

    name = input('enter name of accountholder: ')
    acc_no = 0
    mycursor.execute("select acc_no from acc")
    user1 = mycursor.fetchall()  
    mydatabase.commit()
    acc_check = []
    for i in range(len(user1)):
        acc_check.append(user1[i][0])
    if acc_no not in acc_check:
        acc_no = random.randint(1001, 9999)
    else:
        acc_no = random.randint(1001, 9999)

    address = input('enter your permanent address : ')
    total_balance = int(input("Enter amount to deposit: ₹"))
    data1 = (acc_no, name, address, total_balance)
    data2 = (acc_no, name, total_balance)

    sql1 = "insert into acc values(%s,%s,%s,%s)"
    sql2 = "insert into amount values(%s,%s,%s)"
    c = mydatabase.cursor()
    mycursor.execute(sql1, data1)
    mycursor.execute(sql2, data2)
    mydatabase.commit()
    print("\nAccount Created!!!")
    print("Your Account Number is ", acc_no, " remember it.")


def deposit(acc_no, dep_amt):
    c = mydatabase.cursor()
    mycursor.execute(f"update acc set total_balance=total_balance+{dep_amt} where acc_no= {acc_no}")
    mydatabase.commit()
    mycursor.execute("select total_balance from acc where acc_no="+str(acc_no)+';')
    myresult = mycursor.fetchall()
    t = PrettyTable(['total_balance'])
    for total_balance in myresult:
        t.add_row([total_balance])
    print(t)


def withdraw(acc_no, wd_amt):
    if bal_enq(acc_no) <= wd_amt:
        print("U Cannot TRANSFER greater amounnt than ur balance")
    else:
        c = mydatabase.cursor()
        mycursor.execute(f"update acc set total_balance=total_balance-{wd_amt} where acc_no= {acc_no}")
        mydatabase.commit()
        mycursor.execute("select total_balance from acc where acc_no="+str(acc_no)+';')
        myresult = mycursor.fetchall()

        t = PrettyTable(['total_balance'])
        for total_balance in myresult:
            t.add_row([total_balance])
        print(t)


def bal_enq(acc_no):
    c = mydatabase.cursor()
    mycursor.execute(f'select total_balance from acc where acc_no={acc_no}')
    myresult = mycursor.fetchall()
    print("\n\t Your balance for account is ")
    t = PrettyTable(['total_balance'])
    for total_balance in myresult:
        t.add_row([total_balance])
        print(t)
        return(total_balance[0])     # fnd_tnf me use ho raha hai

    #print(t)


def ac_list():
    c = mydatabase.cursor()
    mycursor.execute('select * from acc')
    myresult = mycursor.fetchall()
    t = PrettyTable(['acc_no', 'name', 'address', 'total_balance'])
    for name, acc_no, address, total_balance in myresult:
        t.add_row([name, acc_no, address, total_balance])
    print("\t\t\t**** Customers Details ***")
    print(t)


def fund_trf(my_acc_no, bf_acc_no, amt=0):
    if amt >= bal_enq(my_acc_no):
        print("U Cannot TRANSFER greater amounnt than ur balance")
    else:
        withdraw(my_acc_no, amt)
        deposit(bf_acc_no, amt)
        print("\nMoney Transfer sucessful for ₹", amt)
        


def close():
    acc_no = int(input('enter  account number : '))
    c = mydatabase.cursor()
    mycursor.execute(f'delete from signup where username="{usr_name}"')
    mycursor.execute(f'delete from amount where acc_no={acc_no}')
    mycursor.execute(f'delete from acc where acc_no={acc_no}')
    mydatabase.commit()
    print("\t\t\t******** Account Deleted Succcesfully ********* ")


# main
print("\t\t\t\t⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳")
print("\t\t\t\t\t⋘◁◀ BANK MANAGEMENT SYSTEM ▶▷⋙")
print("\t\t\t\t⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳")
choice = int(input("\n\t\tPress 1 for SIGNUP\n\t\tPress 2 for LOGIN :  "))
if choice == 1:
    signup()
if choice == 2:
    login()
else:
    print("Invalid Choice")
