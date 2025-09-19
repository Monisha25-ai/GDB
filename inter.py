name = "malayalam"
print("true" if name == name[::-1] else "false")

a ,b = 1,2
a,b = b , a 
print(a,b)


MIN_BALANCE = {"Savings": 500, "Current": 1000}
if self.account_type not in Account.MIN_BALANCE:#how it works means it checks if the account type is in the dictionary or not (including keys)
            raise ValueError(f"Invalid account type: {self.account_type}")#if not then raise value error

def deposit(self, amount):
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        '''here we can use tuple to catch multiple exceptions ."
        "however , we can also use multiple except blocks,"
        "but here we are using tuple if any one of the exception occurs it will be caught'''
        return False, "Invalid Amount"
        '''u can think how it returns false and string together 
        The answer is it works like a tuple that is (False,"Invalid Amount")'''

    def to_dict(self):#this method converts the object to a dictionary(not a built in method)
        return {
            "account_number": self.account_number,
            "name": self.name,
            "age": self.age,
            "balance": self.balance,
            "account_type": self.account_type,
            "status": self.status,
            "pin": self.pin if self.pin else "", #here if pin is None it will return empty string if not it will return pin
        }
    def __str__(self):
        '''this is a built in method it returns string representation of the object(object means instance of the class)
        if this method is not defined it will return the memory address of the object'''
        return f"[{self.account_number}] {self.name} ({self.account_type}) - Balance: {self.balance} - {self.status}"
    

import os, sys, csv
'''how each import works
import os : this module provides a way of using operating system dependent functionality like reading or writing to
files, creating directories, etc.
import sys : this module provides access to some variables used or maintained by the interpreter and to functions
that interact strongly with the interpreter. It is always available.
import csv : this module implements classes to read and write tabular data in CSV format.'''
# Minimal import fix: add the project src/ folder to sys.path so
# "from models..." works when running this file directly.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))#this line adds the parent directory of the current file to the sys.path in simple words it adds the src folder to the sys.path
from models.account import Account
from datetime import datetime#this module supplies classes for manipulating dates and times.
#datetime is a class in the datetime module used to work with date and time objects.
#example: datetime.now() returns the current date and time.and datetime.strptime() is used to convert string to date object
#example: datetime.strptime("2023-10-01", "%Y-%m-%d") returns a date object representing October 1, 2023.


def load_accounts():
    accounts = {}#this creates an empty dictionary to store accounts
    try:
        with open(ACCOUNT_FILE, "r") as f:#this opens the file in read mode 
            reader = csv.DictReader(f)
            '''this reads the file as a dictionary
            for example if the csv file has columns name,age,balance
            then the dictionary will be like {"name": "value", "age": "value", "balance": "value"}'''
            for row in reader:
                '''this iterates through each row of the csv file
                 and row is a dictionary representing each row
                 for example if the csv file has columns name,age,balance
                 then row will be like {"name": "value", "age": "value", "balance": "value"}
                 so we can access the values using row["name"], row["age"], row["balance"]'''
                acc = Account(
                    account_number=row["account_number"],
                    name=row["name"],
                    age=row["age"],
                    account_type=row["account_type"],
                    balance=row["balance"],
                    status=row["status"],
                    pin=row["pin"] if row["pin"] else None,
                )#example is if account_number is 1001,name is vikas,age is 21,account_type is Savings,balance is 5000,status is Active,pin is 1234
                #this creates an object of Account class using the values from the row dictionary
                accounts[acc.account_number] = acc 
                '''for the above example it will be like accounts["1001"] = acc where acc is the object of Account class that we created above and contains all the details of the account like name,age,account_type,balance,status,pin
                so it will '''
    except FileNotFoundError:
        pass #pass means do nothing if the file is not found
    return accounts #this returns the dictionary of accounts where key is account_number and value is the object of Account class

def save_accounts(accounts):
    with open(ACCOUNT_FILE, "w", newline="") as f:#this opens the file in write mode and
        writer = csv.writer(f)
        writer.writerow(["account_number", "name", "age", "balance", "account_type", "status", "pin", "failed_attempts"])
        for acc in accounts.values():
            d = acc.to_dict()
            writer.writerow(
                [
                    d["account_number"],
                    d["name"],
                    d["age"],
                    d["balance"],
                    d["account_type"],
                    d["status"],
                    d["pin"],
                    d["failed_attempts"]
                    ])


 while True:
                admin_pass = input("Enter admin password: ")
                if admin_pass == "admin123":
                    inactive_accounts = banking_service.get_inactive_accounts()
                    if inactive_accounts:
                        for account in inactive_accounts:
                            print(account)
                        break
                    else:
                        print("No inactive accounts found.")
                        break
                else:
                    print("Incorrect password. Try again.")

        elif choice == "12":
            while True:
                admin_pass = input("Enter admin password: ")
                if admin_pass == "admin123":
                    active_accounts = banking_service.get_active_accounts()
                    if active_accounts:
                        for account in active_accounts:
                            print(account)
                        break
                    else:
                        print("No active accounts found.")
                        break
                else:
                    print("Incorrect password. Try again.")

                elif choice == "14":
            name = input("Enter account holder's name: ")
            acc = banking_service.get_account_by_name(name)
            if acc:
                print(acc)
            again()


        
           

        elif choice == "13":
            acc_no = int(input("Enter your account number: "))
            pin = int(input("Enter your pin: "))
            acc, msg = banking_service.get_account_statement(acc_no,pin)
            print(msg)
            if acc:
                print(acc)
            again()

        elif choice == "15":
            account_number = int(input("Enter the account number: "))
            transactions = banking_service.get_transactions(account_number)
            if transactions:
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found.")
            again()