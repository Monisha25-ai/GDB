    
    while True:
        banking_service = BankingService()
        print("\nWelcome to the Global Digital Bank!")
        print("\n------- Main Menu -----------\n")
        print("1. Account Management")
        print("2. Transactions")
        print("3. Search & Reports")
        print("4. Lend Loan")
        print("5. Fixed Deposit")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n--- Account Management ---")
            print("1. Create a new account")
            print("2. Close an account")
            print("3. Activate account")
            print("4. Unlock account")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                account_type = input("Enter your account type: ")
                initial_deposit = float(input("Enter your initial deposit: "))
                choice_pin = input("do you want to set a pin? (y/n): ")
                
                while True:
                    if choice_pin.lower() == "y":
                        pin = input("enter your pin: ")
                        break
                    elif choice_pin.lower() == "n":
                        print("pin not set,so random pin is generated")
                        pin = random.randint(1000, 9999)
                        break
                    else:
                        print("Invalid choice\n please enter y or n")
                        choice_pin = input("do you want to set a pin? (y/n): ")
                        
                acc, msg = banking_service.create_account(name, age, account_type, initial_deposit, pin)
                print(msg)
                if acc:
                    print(acc)
                again()

            elif sub_choice == "2":
                acc_no = int(input("Enter your account number: "))
                ok, msg = banking_service.close_account(acc_no)
                print(msg)
                again()

            elif sub_choice == "3":
                acc_no = int(input("Enter your account number: "))
                # Check if account exists and is already active before asking for PIN
                acc, msg = banking_service.balance_inquiry(acc_no)
                if not acc:
                    print(msg)
                    again()
                    continue
                if acc.status == "Active":
                    print("Account is already active")
                    again()
                    continue
                pin = int(input("Enter your pin to activate: "))
                ok, msg = banking_service.activate(acc_no, pin)
                print(msg)
                again()

            elif sub_choice == "4":
                acc_no = int(input("Enter your account number: "))
                pin = int(input("Enter your pin: "))
                ok, msg = banking_service.unlock_account(acc_no, pin)
                print(msg)
                again()
            else:
                print("Invalid choice.")
                again()

        elif choice == "2":
            print("\n--- Transactions ---")
            print("1. Deposit money")
            print("2. Withdraw money")
            print("3. Money Transfer")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                acc_no = int(input("Enter your account number: "))
                amount = float(input("Enter the amount to deposit: "))
                pin = int(input("Enter your pin: "))
                ok, msg = banking_service.deposit(acc_no, amount, pin)
                print(msg)
                again()

            elif sub_choice == "2":
                acc_no = int(input("Enter your account number: "))
                amount = float(input("Enter the amount to withdraw: "))
                pin = int(input("Enter your pin: "))
                ok, msg = banking_service.withdraw(acc_no, amount, pin)
                print(msg)
                again()

            elif sub_choice == "3":
                from_acc_no = int(input("Enter your account number: "))
                to_acc_no = int(input("Enter the recipient's account number: "))
                amount = float(input("Enter the amount to transfer: "))
                pin = int(input("Enter your pin: "))
                ok, msg = banking_service.transfer(from_acc_no, to_acc_no, pin, amount)
                print(msg)
                again()
            else:
                print("Invalid choice.")
                again()

        elif choice == "4":
            acc_no = int(input("Enter your account number: "))
            ok, msg = banking_service.lend_loan(acc_no)
            print(msg)
            again()

        elif choice == "5":
            print("Interest rate is 5% per annum.\n"
              "Maturity amount will be calculated using simple interest formula.")
            acc = int(input("Enter your account number: "))
            print(msg)
            again()

        elif choice == "3":
            print("\n--- Search & Reports ---")
            print("1. Check balance (Search by account number)")
            print("2. Get account statement")
            print("3. View transactions for an account")
            print("4. Admin: Search by name")
            print("5. Admin: List all active accounts")
            print("6. Admin: List all inactive accounts")
            print("7. Admin: List all locked accounts")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                acc_no = int(input("Enter your account number: "))
                acc, msg = banking_service.balance_inquiry(acc_no)
                print(msg)
                if acc:
                    print(acc)
                again()
            elif sub_choice == "2":
                acc_no = int(input("Enter the account number: "))
                pin = int(input("Enter the pin: "))
                acc, msg = banking_service.get_account_statement(acc_no, pin)
                print(msg)
                if acc:
                    print(acc)
                again()
            elif sub_choice == "3":
                account_number = int(input("Enter the account number: "))
                transactions = banking_service.get_transactions(account_number)
                if transactions:
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transactions found.")
                again()
            elif sub_choice in ["4", "5", "6", "7"]:
                admin_pass = input("Enter admin password: ")
                if admin_pass != "admin123":
                    print("Incorrect password.")
                    again()
                    continue

                if sub_choice == "4":
                    name = input("Enter account holder's name: ")
                    acc = banking_service.get_account_by_name(name)
                    if acc:
                        print(acc)
                    else:
                        print("Account not found.")
                    again()
                elif sub_choice == "5":
                    active_accounts = banking_service.get_active_accounts()
                    if active_accounts:
                        for account in active_accounts:
                            print(account)
                    else:
                        print("No active accounts found.")
                    again()
                elif sub_choice == "6":
                    inactive_accounts = banking_service.get_inactive_accounts()
                    if inactive_accounts:
                        for account in inactive_accounts:
                            print(account)
                    else:
                        print("No inactive accounts found.")
                    again()
                elif sub_choice == "7":
                    locked_accounts = banking_service.get_locked_accounts()
                    if locked_accounts:
                        for account in locked_accounts:
                            print(account)
                    else:
                        print("No locked accounts found.")
                    again()
            else:
                print("Invalid choice.")
                again()

        elif choice == "6":
            print("Thank you for using Global Digital Bank. Goodbye!")
            sys.exit()

        # This block is now part of the sub-menus, but kept here as a reference for admin password logic
        elif choice == "11": # This choice is no longer in the main menu, but we can handle it just in case
            while True:
                admin_pass = input("Enter admin password: ")
                if admin_pass == "admin123":
                    print("Admin features have been moved to 'Search & Reports'.")
                    break
                else:
                    print("Incorrect password. Try again.")
            again()
            
        else:
            print("Invalid choice")



                accounts.append(acc)         
        return accounts
    
    def get_locked_accounts(self):
        accounts = []
        print("Locked Accounts:")
        for acc in self.accounts.values():
            if acc.is_locked():
                accounts.append(acc)
        return accounts

    def fixed_deposit(self,account_number,amount,tenure,pin):
        acc = self.get_account(account_number)
        print(f"Account Balance: {acc.balance}")

