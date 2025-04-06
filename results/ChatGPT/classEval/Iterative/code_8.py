class BankAccount:
    """
    A class representing a bank account system, supporting deposit, withdrawal, balance viewing, and money transfer.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with a specified balance (default is 0).
        :param balance: int
        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance.
        Returns the current account balance.
        Raises ValueError for negative amounts.
        :param amount: int
        """
        if amount < 0:
            raise ValueError("Invalid amount. Must be non-negative.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance.
        Returns the current account balance.
        Raises ValueError for negative amounts or insufficient balance.
        :param amount: int
        """
        if amount < 0:
            raise ValueError("Invalid amount. Must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        """
        Returns the current account balance.
        """
        return self.balance

    def transfer(self, other_account, amount):
        """
        Transfers a specified amount from the current account to another account.
        Raises ValueError for invalid transfer amounts.
        :param other_account: BankAccount
        :param amount: int
        """
        if not isinstance(other_account, BankAccount):
            raise ValueError("The recipient must be a BankAccount instance.")
        if amount < 0:
            raise ValueError("Invalid amount. Must be non-negative.")
        self.withdraw(amount)
        other_account.deposit(amount)