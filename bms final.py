import pickle
import random


def ac_storer():
    log = {}
    acc_list = []
    try:
        f = open("users.dat", "ab")
        while True:
            log = pickle.load(f)
            for i in log:
                acc_list.append(log[i]['acc_no'])

    except Exception:
        f.close()
    return acc_list    # openAccount me use kar rahe hai


def openAccount():
    repeat = ac_storer()
    user_log = {}
    fin = open('users.dat', 'ab')
    condi = 'y'
    while condi == 'y':
        name = str(input("\nEnter the account holder name : "))
        bal = int(input("Enter The Initial deposit amount(>=500)  : "))
        acd = {}
        accNo = random.randint(1001, 9999)
        for i in repeat:
            if i == accNo:
                accNo = random.randint(1001, 9999)
            else:
                pass
        user_log[accNo] = acd
        acd["name"] = name
        acd["acc_no"] = accNo
        acd["bal"] = bal
        pickle.dump(user_log, fin)
        user_log.clear()
        print("\nAccount Created!!!")
        print("Your Account Number is ", accNo, " remember it.")

        condi = input("\nWant to add more users (y\\n):")

    fin.close()


def ac_list():
    log = {}
    f = open("users.dat", "rb")
    print("*"*78)
    print("Data stored in bank database....")
    try:
        while True:
            log = pickle.load(f)
            for i in log:
                print("Name:", log[i]['name'])
                print("Acc No.:", log[i]['acc_no'])
                print("Balance: ₹", log[i]['bal'])
                print("."*75)

    except EOFError:
        print("*"*78, "\n")
        f.close()


def bal_enq(num=0):
    log = {}
    f = open("users.dat", "rb")
    print("*"*78)
    tmp = 0
    try:
        while True:
            log = pickle.load(f)
            for j in log.values():
                if j["acc_no"] == num:
                    print("Your balence left for acc no. ",
                          num, " is : ₹", j.get("bal"))

                    return j.get("bal")   # fnd_tnf me use ho raha hai

                    tmp = 1

    except Exception:
        f.close()
        if tmp == 0:
            print("Record not found...")
    else:
        pass
    print("*"*78)


def deposit(num1=0, depo=0):
    data = {}
    found = False
    fin = open("users.dat", "rb+")

    try:
        while True:
            rpos = fin.tell()
            data = pickle.load(fin)

            if num1 in data.keys():
                data[num1]["bal"] += depo
                fin.seek(rpos)
                print(data)
                pickle.dump(data, fin)
                found = True
    except EOFError:
        if found == False:
            print("No record found!!")
        else:
            print("Record updated")
            fin.close()


def withdraw(num1=0, wd=0):
    data = {}
    found = False
    fin = open("users.dat", "rb+")

    try:
        while True:
            rpos = fin.tell()
            data = pickle.load(fin)

            if num1 in data.keys():
                if wd <= data[num1]["bal"]:
                    data[num1]["bal"] -= wd
                    fin.seek(rpos)
                    print(data)
                    pickle.dump(data, fin)
                else:
                    print("U Cannot WITHDRAW greater amounnt than ur balance")
                found = True
    except EOFError:
        if found == False:
            print("No record found!!")
        else:
            print("Record updated")
            fin.close()


def fund_trf(my=0, amt=0, his=0):
    if amt >= bal_enq(my):
        print("U Cannot TRANSFER greater amounnt than ur balance")
    else:
        withdraw(my, amt)
        deposit(his, amt)
        print("\nMoney Transfer sucessful for ₹", amt)


def edit_acc(num, new_nm):
    data = {}
    found = False
    fin = open("users.dat", "rb+")

    try:
        while True:
            rpos = fin.tell()
            data = pickle.load(fin)

            if num in data.keys():
                data[num]["name"] = new_nm
                fin.seek(rpos)
                print(data)
                pickle.dump(data, fin)
                found = True
    except EOFError:
        if found == False:
            print("No record found!!")
        else:
            print("Record updated")
            fin.close()


def intro():
    print("\t\t\t\t⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳")
    print("\t\t\t\t\t⋘◁◀ BANK MANAGEMENT SYSTEM ▶▷⋙")
    print("\t\t\t\t⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳")
    input()


# main body
command = ''
num = 0
intro()

while command != 8:
    print("\n\t\t <<< MAIN MENU >>>")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. FUND TRANSFER (RTGS|NET BANKING|UPI)")
    print("\t5. BALANCE ENQUIRY")
    print("\t6. ALL ACCOUNT HOLDER LIST")
    print("\t7. EDIT AN ACCOUNT DETAILS")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    command = input()

    if command == '1':
        openAccount()
    elif command == '2':
        num = int(
            input("\tEnter The account No. to\n\twhich money is to be deposit : "))
        num1 = int(input("Enter amount to deposit: ₹"))

        deposit(num, num1)
    elif command == '3':
        num = int(
            input("\tEnter The account No. to\n\twhich money is to be withrawn : "))
        num1 = int(input("Enter amount to withdraw: ₹"))

        withdraw(num, num1)

    elif command == '4':
        num = int(input("\tEnter 'Your' account No. : "))
        num2 = int(input("\tEnter 'Beneficiary' account No. : "))
        num1 = int(input("Enter amount to transfer(send): ₹"))
        fund_trf(num, num1, num2)

    elif command == '5':
        num = int(input("\tEnter The account No. : "))
        bal_enq(num)

    elif command == '6':
        ac_list()

    elif command == '7':
        num = int(input("\tEnter The account No. : "))
        num3 = str(input("\tEnter the new Name to change : "))
        edit_acc(num, num3)

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
