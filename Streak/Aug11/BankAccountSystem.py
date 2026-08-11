#print("Learning OOPs concepts in Python")

class Account:
    print("Learning OOPs concepts in Python")

    def __init__(self,name,balance): #removed lineofcredit from base class
        self.name = name
        self._balance = balance
        #self.lineofcredit = lineofcredit

    @property
    def balance(self):
        """2. Read-only getter: allows reading balance, but prevents overwriting directly."""
        return self._balance

    def showInformation(self):
        print(f"{self.name} has a balance of {self._balance}")


    def amountcredit(self, credit):
        #print("This is a method to calculate the amount of credit available.")
        #assert credit > 0, "credit amount should be greater than 0" assert error is crashing the program so implementing valueerror instead
        #value error also interrupting the program just like assert error.
        #trying implementing try ..except method.

        # if credit <=0:
        #     raise ValueError("credit amount should be greater than 0")

        # Validate input: print error and exit method if invalid
        if credit <= 0:
            print(f"Error for {self.name}: Credit amount must be greater than 0.")
            return
        
        
        print(f"amount credited: {credit}")
        self._balance = self._balance + credit
        print(f"available balance: {self._balance}")

    def amountdebit(self, debit):
        #print("This is a method to calculate the amount of debit available.")
        #assert debit >= 0 and debit < self._balance, "debit amount should be greater than or equal to 0 and less than {self._balance}"
       
        # if debit <=0 or debit > self._balance:
        #     raise ValueError("debit amount should be greater than or equal to 0 and less than {self._balance}")

        print(f"amount debited: {debit}")
        self._balance = self._balance - debit
        print(f"available balance: {self._balance}")
class Saving_account(Account):
    def __init__(self,name, balance,interest_rate):
        super().__init__(name,balance) # super() calls the parent class constructor to set name and balance.
        self.interest_rate = interest_rate

    def add_interest(self):
        self._balance = self._balance + (self._balance * self.interest_rate)
        print(f"new updated balance is: {self._balance}") 

    
saving_Acc1 = Saving_account("Erik", 2000, 0.05)
print(saving_Acc1.balance)
saving_Acc1.showInformation()
saving_Acc1.add_interest()
#saving_Acc1.balance = 999999 #will not update the value because of  self._balance and this is called Encapsulation.

saving_Acc1.showInformation()


Account1 = Account("JOhn Doe", 1000)
# Account1.name = "John Doe"
# Account1.balance = 1000
# Account1.lineofcredit = 5000 
# print(f"{Account1.name} has a balance of {Account1.balance} and a line of credit of {Account1.lineofcredit}.")
Account1.showInformation()
Account1.amountcredit(-200)
Account1.amountdebit(50)
# Account2 = Accounts()
# Account2.name = "Jane Smith"
# Account2.balance = 1500
# Account2.lineofcredit = 7500
# print(f"{Account2.name} has a balance of {Account2.balance} and a line of credit of {Account2.lineofcredit}.")  

Account2 = Account("Marry", 4500)
Account2.showInformation()
Account2.amountdebit(4000)