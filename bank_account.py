class BankAccount:
    def __init__ (self,name,initial_balance = 0 ):
        self.BankAccount = name
        self.__balance = initial_balance

    def deposit (self,amount):
        if amount > 0:
            self.__balance += amount
            print(f'The total Balance of your account is: ${self.__balance:}')

    def withdraw (self,amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f'The remained amount in your accont is: ${self.__balance:}')

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Holder: {self.BankAccount}, Balance: {self.__balance:}"

def main():
    name= input(" Enter the account holder's name: ")
    accont = BankAccount(name)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input('\nchoose an option(1-4): ')

        if choice == "1":
            amount = float(input('Enter amount to deposit: '))
            accont.deposit(amount)

        elif choice == "2":
            amount = float(input('Enter amount to Withdraw: '))
            accont.withdraw(amount)

        elif choice == "3":
            print(f'Current Balance: {accont.get_balance():}')

        elif choice == "4":
            print("Exiting.....")
            break

        else:
            print('Invalid choice, Please try again.')

if __name__ == '__main__':
    main()

