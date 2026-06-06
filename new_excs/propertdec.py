class BankAccount:
    def __init__(self, acctno, holname, balance):
        self._acctno = acctno
        self._holname = holname
        # Triggers the setter method below to enforce validation during initialization
        self.balance = balance
    
    @property 
    def balance(self):
        """Getter for balance."""
        return self._balance

    @balance.setter 
    def balance(self, balance):
        """Setter for balance with validation."""
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        # Uses a protected internal attribute (_balance) to prevent infinite 
        # recursion, as assigning to self.balance would call this setter again.
        self._balance = balance 
        
    @property 
    def holname(self):
        """Getter for holname that returns the name in uppercase."""
        return self._holname.upper()    
    
    @property
    def acctno(self):
        """Read-only getter for acctno."""
        return self._acctno

# --- Example Usage ---
ob = BankAccount("12345563", "seShu", 2000)
print(ob.acctno, ob.balance, ob.holname)

ob.balance = 80000
# ob.acctno="123789" There will be an error if this executed because a getter method 
# is executed without setter which means you cannot update existing value 
print(ob.acctno, ob.balance, ob.holname)