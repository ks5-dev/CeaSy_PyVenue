'''
Đây là một chương trình mô phỏng chức năng của 1 tài khoản ngân hàng, ứng dụng lập trình hướng đối tượng
'''
class Bank_Account:
    def __init__(self, default_balance = 0):
        self.balance= default_balance
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Tạo 1 vật thể
#s = Bank_Account()
  
# Calling functions with that class object
'''
s.deposit()
s.withdraw()
s.display()


print(s.balance)
'''

class Premium_Account(Bank_Account):
    def __init__(self):
        super().__init__(10)
        rate = float(input("Your rate, input in float: "))
        tenure = int(input("Your tenure: "))
        self.simple_interest(rate, tenure)
    def simple_interest(self, rate = 0.01, tenure = 12):
        self.gain = self.balance * rate * tenure
        self.balance += self.gain
    def display(self):
        print("Current balance after gaining interest:", self.balance)

x = Premium_Account()
x.display()
x.deposit()