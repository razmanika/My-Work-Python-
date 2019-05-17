class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return 'Account owner: {0}\nAccount balance: {1}$'.format(self.owner,self.balance)
    
        
    def deposit(self,depo):
        if depo <= self.balance:
            self.balance += depo
            return "Deposit Accepted \n{1} Your Balance is:{0}$".format(self.balance,self.owner)
        else:
            return 'Deposit Declined'
    def withdraw(self,with_drow):
        if with_drow <= self.balance:
            self.balance -= with_drow
            return "Withdrawal Accepted \n{1} Your Balance is:{0}$".format(self.balance,self.owner)
        else:
            return 'Funds Unavailable!'

acct1 = Account('Jose',100)
print(acct1)
print(acct1.deposit(50))
print(acct1.withdraw(80))
