#print("Learning OOPs concepts in Python")

class Accounts:
    print("Learning OOPs concepts in Python")

    def __init__(self,name,balance,lineofcredit):
        self.name = name
        self.balance = balance
        self.lineofcredit = lineofcredit

    def showInformation(self):
        print(f"{self.name} has a balance of {self.balance} and a line of credit of {self.lineofcredit}.")


    def amountcredit(self, credit):
        #print("This is a method to calculate the amount of credit available.")
        print(f"amount credited: {credit}")
        self.balance = self.balance + credit
        print(f"available balance: {self.balance}")

    def amountdebit(self, debit):
        #print("This is a method to calculate the amount of debit available.")
        print(f"amount debited: {debit}")
        self.balance = self.balance - debit
        print(f"available balance: {self.balance}")

    



Account1 = Accounts("JOhn Doe", 1000, 5000)
# Account1.name = "John Doe"
# Account1.balance = 1000
# Account1.lineofcredit = 5000 
# print(f"{Account1.name} has a balance of {Account1.balance} and a line of credit of {Account1.lineofcredit}.")
Account1.showInformation()
Account1.amountcredit(100)
Account1.amountdebit(50)
# Account2 = Accounts()
# Account2.name = "Jane Smith"
# Account2.balance = 1500
# Account2.lineofcredit = 7500
# print(f"{Account2.name} has a balance of {Account2.balance} and a line of credit of {Account2.lineofcredit}.")  

Account2 = Accounts("Marry", 4500, 12000)
Account2.showInformation()
Account2.amountdebit(1200)