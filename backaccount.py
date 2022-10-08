class BankAccount:
    # define constructor with attributes 
    def __init__(self, accountnumber , name, balance):
        self.number = accountnumber
        self.name = name
        self.balance = balance
        
    # Create method
    def Deposit(self,d):
        print("Your current balance is" ,self.balance)
        print("You deposit" ,d)
        self.balance = self.balance + d
        print("Your current balance is" ,self.balance)
        return self.balance
    
    # Create method
    def Withdraw(self,w):
        if w > self.balance:
            print (" Your account hasn't enough money to get withdraw action")
        else:
            print("Your current balance is" ,self.balance)
            print("You withdraw:" ,w)
            self.balance = self.balance - w
            print("Your current balance is" ,self.balance)
               
        return self.balance   
    # Create method
    def Bankfee(self):
        print ("Your account fee will be count as 5% of your account")
        self.balance = self.balance*95/100
    
    # create display method
    def display(self):
        print("The owner of this bank account is: ", self.name)
        print("The accountnumber is: ", self.number)
        print("The balance of this account is: ", self.balance)
        #print("The area of rectangle is: ", self.Area())


a1 = BankAccount("123456","John", 4000)
print("----------------------------------")
a1.Deposit(1000)
print("----------------------------------")
a1.Withdraw(3000)
print("----------------------------------")
a1.display()
