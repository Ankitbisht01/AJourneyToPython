class Account:
    """Base class representing a standard bank account."""

    def __init__(self, name: str, balance: float):
        self.name = name
        self._balance = balance  # Protected attribute (Encapsulation)

    @property
    def balance(self) -> float:
        """Read-only property to view account balance safely."""
        return self._balance

    def show_information(self) -> None:
        """Prints summary details for the account."""
        print(f"Account Holder: {self.name} | Current Balance: ${self._balance:,.2f}")

    def credit(self, amount: float) -> None:
        """Deposits funds into the account after input validation."""
        if amount <= 0:
            print(f"Transaction Error ({self.name}): Credit amount must be greater than $0.")
            return

        self._balance += amount
        print(f"[{self.name}] Credited: ${amount:,.2f} | Available Balance: ${self._balance:,.2f}")

    def debit(self, amount: float) -> None:
        """Withdraws funds from the account if sufficient balance exists."""
        if amount <= 0:
            print(f"Transaction Error ({self.name}): Debit amount must be greater than $0.")
            return

        if amount > self._balance:
            print(f"Transaction Error ({self.name}): Insufficient funds. Available: ${self._balance:,.2f}")
            return

        self._balance -= amount
        print(f"[{self.name}] Debited: ${amount:,.2f} | Available Balance: ${self._balance:,.2f}")


class SavingAccount(Account):
    """Child class representing a interest-bearing savings account."""

    def __init__(self, name: str, balance: float, interest_rate: float):
        super().__init__(name, balance)
        self.interest_rate = interest_rate  # e.g., 0.05 for 5%

    def add_interest(self) -> None:
        """Calculates and credits earned interest to the account balance."""
        earned_interest = self._balance * self.interest_rate
        self._balance += earned_interest
        print(f"[{self.name}] Interest Earned: ${earned_interest:,.2f} ({self.interest_rate * 100}%) | Updated Balance: ${self._balance:,.2f}")


# ==========================================
# DRIVER CODE / DEMONSTRATION
# ==========================================

if __name__ == "__main__":
    # --- Savings Account Demonstration ---
    print("--- Savings Account Operations ---")
    saving_acc = SavingAccount("Erik", 2000, 0.05)
    saving_acc.show_information()
    saving_acc.add_interest()
    saving_acc.show_information()

    # --- Standard Account Operations ---
    print("\n--- Standard Account Operations ---")
    acc1 = Account("John Doe", 1000)
    acc1.show_information()
    
    # Testing invalid credit input
    acc1.credit(-200)
    
    # Valid debit operation
    acc1.debit(50)

    print("\n--- Insufficient Funds Check ---")
    acc2 = Account("Mary", 4500)
    acc2.show_information()
    acc2.debit(5000)  # Exceeds available balance