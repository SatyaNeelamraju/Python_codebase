class BankAccount:
    total_bank_reserves = 0.0
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    @classmethod
    def bank_reserves(cls,amount):
        cls.total_bank_reserves=cls.total_bank_reserves+amount
        return cls.total_bank_reserves

holder1=BankAccount("Sai",10000)
balance=holder1.deposit(500)
reserves=holder1.bank_reserves(500)
print(f"Balance after 1st transaction: {balance}")
balance2=holder1.deposit(1500)
reserves=holder1.bank_reserves(500)
print(f"Balance after 2nd transaction: {balance2}")

