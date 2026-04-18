class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"  +{amount:,} so'm -> Balans: {self.balance:,} so'm")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  Xato: Yetarli mablag' yo'q! (Balans: {self.balance:,})")
        else:
            self.balance -= amount
            print(f"  -{amount:,} so'm -> Balans: {self.balance:,} so'm")


if __name__ == "__main__":
    acc = BankAccount("Ali Valiyev", 50000)
    print(f"Hisob egasi: {acc.owner}\n")
    acc.deposit(20000)
    acc.withdraw(100000)
    acc.withdraw(15000)
