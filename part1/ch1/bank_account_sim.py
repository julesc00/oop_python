

class Banking:
    def __init__(self):
        self.ACCOUNT_NAME = "Julito"
        self.ACCOUNT_BALANCE = 100
        self.ACCOUNT_PASSWORD = "soup"
        self.tries_history = []

    def main(self):
        sesame = self.login()
        if sesame.get("sesame"):
            self.show_operations()
        else:
            print("Sorry, your information does not match our data. Account is blocked.")
            return

        action = input("What do you want to do? ").lower()[0]
        print()

        if action == "b":
            print(self.check_balance())
        elif action == "d":
            print(self.deposit())

    def create_account(self, account_name: str, account_bal: int, password: str):
        pass

    def login(self) -> dict:
        print("Welcome to Untrusty Bank")

        login_tries, sesame = 3, False
        while login_tries:
            acc_name = input(f"Please enter Account Name: ")
            acc_pass = input(f"Please enter your password: ")

            if acc_name != self.ACCOUNT_NAME and acc_pass != self.ACCOUNT_PASSWORD:
                print("Wrong account name or password, please try again")
                login_tries -= 1
                self.tries_history.append(login_tries) if login_tries < 2 else None
            else:
                print(f"Welcome {self.ACCOUNT_NAME.title()}")
                sesame = True
                return {
                    "sesame": sesame,
                    "login_tries": login_tries
                }
        return {
            "sesame": sesame,
            "login_tries": login_tries
        }

    @staticmethod
    def show_operations():
        print("""
            Press b to get the balance
            Press d to make a deposit
            Press w to make a withdrawal
            Press s to show the account
            Press q to quit
        """)

    def deposit(self) -> str:
        print("Deposit")
        deposited_amount = int(input("Please enter amount to deposit: "))
        balance = self.ACCOUNT_BALANCE + deposited_amount
        return f"Your balance is: ${balance}"

    def withdraw(self, account_name: str, account_bal: int, password: str):
        pass

    def check_balance(self) -> int:
        print(f"Your balance is: ${self.ACCOUNT_BALANCE:2}")
        return self.ACCOUNT_BALANCE


if __name__ == "__main__":
    julito = Banking()
    julito.main()
