from bank_account import Account   # import your class file (whatever you named it)

def main():
    print("=== Welcome to Python Bank ===")
    acc = Account()                 # create a new account object
    if not acc.login_in():          # login or create account
        return

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Transfer money")
        print("4. Show interest forecast")
        print("5. Account summary")
        print("6. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            acc.deposit()
        elif choice == "2":
            acc.withdrawal()
        elif choice == "3":
            acc.transfer()
        elif choice == "4":
            acc.interest_forecast()
        elif choice == "5":
            acc.account_summary()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
