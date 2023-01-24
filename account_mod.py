#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Account:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
    def __str__(self):
        return f"Account: {self.number} Balance: {self.balance}"
        
    def get_balance(self, number):
        return self.balance
    def get_number(self):
        return self.number
    def change_balance(self, change_in_balance):
        balance += change_in_balance

