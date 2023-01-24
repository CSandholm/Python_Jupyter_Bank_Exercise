import re
import customer_mod
from collections import deque

class Bank:
    def __init__(self):
        self.customers = []
        self.logged_in = None
        self.admin_user = {"admin": "adminPassword123"}
        
    def get_customers(self):
        return self.customers
    def get_customer(self, userName):
        for customer in self.customers:
            if customer.userName == userName:
                return customer
    def add_customer(self, userName, password):
        self.customers.append(customer_mod.Customer(userName, password))
        return True
    def remove_customer(self, userName):
        for customer in self.customers:
            if customer.userName == userName:
                print(f"Removed {userName}")
                self.customers.remove(customer)
                return True
        return False
    def change_customer_password(self, userName, new_password):
        for customer in self.customers:
            if customer.userName == userName:
                customer.password = new_password
                print(f"Password for {userName} changed.")
                return True
        return False

    def add_account_loggedIn(self, number, balance):
        if self.logged_in != None or "admin":
            self.logged_in.add_account(number, balance)
            return True
        return False
    def remove_account_loggedIn(self, number):
        if self.logged_in != None or "admin":
            self.logged_in.remove_account(number)
            return True
        return False
    def get_account_loggedIn(self, number):
        if self.logged_in != None or "admin":
            return self.logged_in.get_account(number)
    def get_accounts_loggedIn(self):
        if self.logged_in != None or "admin":
            return self.logged_in.get_accounts()
    def deposit_to_loggedIn(self, number, amount):
        if self.logged_in != None or "admin":
            self.logged_in.deposit(number, amount)
            return True
        return False
    def withdraw_to_loggedIn(self, number, amount):
        if self.logged_in != None or "admin":
            self.logged_in.withdraw(number, amount)
            return True
        return False

    def login(self, inputName, inputPassword):
        #login through inputName and inputPassword
        if inputName == "admin":
            if inputPassword != self.admin_user['admin']:
                self.login_error()
            else: 
                self.login_success(inputName)
        else:
            for customer in self.customers:
                if customer.userName == inputName and customer.password == inputPassword:
                    self.login_success(inputName)
                    self.logged_in = customer
                    return True
            else: 
                self.login_error()
                return False 
    def login_error(self):
        print(f"Error: username or password was incorrect. Try again.")
    def login_success(self, name):
        print(f"Logged in as: {name}")
    def logout(self):
        if self.logged_in != None:
            self.logged_in = None
            print("Logged out")
            return True
        else: return False
    
    def get_accounts(self):
        #Return all available accounts based on logged in user. admin get all accounts
        if self.logged_in == None:
            print("You have to log in first.")
        elif self.logged_in == "admin":
            all_accounts = []
            for customer in self.customers:
                for account in customer.accounts:
                    all_accounts.append(account)
            print("Admin get all customers accounts.")
            return all_accounts
        else:
            for customer in self.customers:
                if self.logged_in == customer:
                    accounts = []
                    for account in customer.accounts:
                        accounts.append(account)
                    print(f"{customer.userName} got accounts.")
                    return accounts       
    
    
    def load_input(self):
        #open and handle data from txt-file. 
        #fill customers list and accounts
        
        self.input_list = []
        
        with open('input.txt') as f:
            lines = f.readlines()  

        for line in lines:
            #Split on certain characters and create a new input_list_string
            input_list_string = re.split('/|@|\n|#', line)
            
            if len(input_list_string) % 2 != 0:
                #input_list_string will have an even numbers indexes, but most include one unwanted index: ''. Remove it.
                input_list_string.pop()
            self.input_list.append(input_list_string)
            
        for lists in self.input_list:
            #Create Customer
            customer = customer_mod.Customer(lists[0], lists[1])
            #Delete the first two indexes so that list only include accounts. Ugly, "bad", but works for now.
            del lists[0] 
            del lists[0] 
            
            counter = 0
            while counter < len(lists):
                #Add accounts
                customer.add_account(lists[counter], int(lists[counter+1]))
                counter += 2
            #Add customer to customers list
            self.customers.append(customer)
            
    def save(self):
        #save changes to txt-file
        
        output_list = []
        
        for customer in self.customers:
            customer_string = f"{customer.userName}/{customer.password}#"
            for account in customer.accounts:
                customer_string += f"{account.number}/{account.balance}@"
            
            output_list.append(customer_string[:-1])
            
        with open("output.txt", 'w') as f:
            for output_string in output_list:
                f.write("%s\n" % output_string)
        print('Output saved to output.txt')