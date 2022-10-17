#Bank Example
        
class bank():
    __balance=0.00
    __usercount=0
    def __init__(self):
        self.name=input('Enter Name :')
        self.gender=input('Enter Gender :')
        self.salary=int(input('Enter Salary :'))
        bank.__usercount+=1

    def showdetails(self):
        print (f"Name  =  {self.name}")
        print (f"Gender  =  {self.gender}")
        print (f"Salary  =  {self.salary}")
        print (f"Account no.  =  Ivbnk2200{bank.__usercount}")

    def deposite(self):
        self.amount=int(input("Enter the amount :"))
        self.__balance+=self.amount
        print("Amount added successfully")
        print(f"Opening Balance = {self.__balance}")

    def withdraw(self):
        self.amount=int(input("Enter the amount :"))
        if(self.amount>self.__balance):
            print("Insufficient balance")
            print(f"Opening Balance = {self.__balance}")

        elif((self.amount>100) and (self.amount<=self.__balance)):
            self.__balance=self.__balance-self.amount
            print(f"Opening Balance = {self.__balance}")
            print("Thank you for visisting")

        elif(self.amount<100):
            print("You can not withdraw amount less than 100.")
            print("Thank you for visisting")
            print(f"Opening Balance = {self.__balance}")

    def viewbalance(self):
        self.showdetails()
        print(f"Opening Balance = {self.__balance}")

    def transfer(self):
        self.amount=int(input("Enter amount :"))
        if(self.amount>self.__balance):
            print("Insufficient balance")
            print(f"Opening Balance = {self.__balance}")

        elif((self.amount>1) and (self.amount<=self.__balance)):
            user2.__balance+=self.amount
            self.__balance-=self.amount
            print("Amount transferred successfully")
            print(f"Opening Balance = {self.__balance}")
            print("Thank you for visisting")
        
        else:
            print("Transfer failed")
            print("Thank you for visisting")
            print(f"Opening Balance = {self.__balance}")
        

print("Welcome to ITvedant Bank Ltd., Please Enter your details")
user1=bank()
abc=True
while(abc):    
    print("""To Check Account Details, Press '1'
             To Check Account Balance, Press '2'
             For Transactions, Press '3'
             To Logout, press '0'""")
    z=int(input("Enter your choice :"))
    if (z==1):
        user1.showdetails()
    elif(z==2):
        user1.viewbalance()
    elif(z==3):
        print("""
                 1. Cash Withdrawal
                 2. Deposite
                 3. Fund Transfer
                 0. Exit""")
        
        x=int(input("Enter your choice :"))
        if(x==1):
            user1.withdraw()
        elif(x==2):
            user1.deposite()
        elif(x==3):
            print("Add benificiary")
            user2=bank()
            user1.transfer()
        elif(x==0):
            break
        else:
            print("Invalid Choice")
    elif(z==0):
        abc=False
    else:
        print("Invalid Choice")
