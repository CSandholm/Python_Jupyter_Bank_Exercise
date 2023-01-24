import account_mod

class Customer:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.accounts = []
    def __str__(self):
        return f"Username: {self.userName} Password: {self.password}"
        
    def add_account(self, number, balance):
        self.accounts.append(account_mod.Account(number, balance))
    def get_account(self, number):
        for account in self.accounts:
            if account.number == number:
                return account
    def get_accounts(self):
        return self.accounts
    def remove_account(self, number):
        for account in self.accounts:
            if account.number == number:
                print(f"Deleted account {account.number}")
                self.accounts.remove(account)
                
    def deposit(self, number, amount):
        for account in self.accounts:
            if account.number == number:
                print(f"Added funds to: {number}")
                account.balance += amount
    def withdraw(self, number, amount):
        for account in self.accounts:
            if account.number == number:
                print(f"Withdrew funds from: {number}")
                account.balance -= amount
        
    def login_check(self, userName, password):
        if userName == self.userName and self.password == password:
            return True
        else: return False