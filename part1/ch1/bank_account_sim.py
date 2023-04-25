

class Banking:
    def __init__(self):
        self.ACCOUNT_NAME = "Julito"
        self.ACCOUNT_BALANCE = 100
        self.ACCOUNT_PASSWORD = "soup"

    def main(self):
        sesame = self.login()
        if sesame:
            print("""
                Press b to get the balance
                Press d to make a deposit
                Press w to make a withdrawal
                Press s to show the account
                Press q to quit
            """)
        else:
            print("Sorry, your information does not match our data. Account is blocked.")
            return

        action = input("What do you want to do? ").lower()[0]
        print()

        if action == "b":
            print(self.check_balance())

    def create_account(self, account_name: str, account_bal: int, password: str):
        pass

    def login(self):
        print("Welcome to Untrusty Bank")

        login_tries, sesame = 3, False
        while login_tries:
            acc_name = input(f"Please enter Account Name: ")
            acc_pass = input(f"Please enter your password: ")
            if acc_pass != self.ACCOUNT_PASSWORD:
                print("Wrong account name or password, please try again")
                login_tries -= 1
            else:
                print(f"Welcome {self.ACCOUNT_NAME.title()}")
                sesame = True
                return sesame

    def deposit(self):
        print("Deposit")

    def withdraw(self, account_name: str, account_bal: int, password: str):
        pass

    def check_balance(self):
        print("Get balance:")
        return f"Your balance is: ${self.ACCOUNT_BALANCE:2}"


if __name__ == "__main__":
    julito = Banking()
    julito.main()
