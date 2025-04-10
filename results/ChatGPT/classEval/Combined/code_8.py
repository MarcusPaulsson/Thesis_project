class BankAccount:
    """
    A class representing a bank account system that supports deposit, withdrawal, balance viewing, and money transfer.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with a specified balance.
        :param balance: Initial balance of the account (default is 0).
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        :param amount: Amount to deposit (must be non-negative).
        :raises ValueError: If the amount is negative.
        :return: Current account balance after deposit.
        """
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.
        :param amount: Amount to withdraw (must be non-negative and not exceed balance).
        :raises ValueError: If the amount is negative or exceeds the balance.
        :return: Current account balance after withdrawal.
        """
        self._validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        """
        Returns the current account balance.
        :return: Current account balance.
        """
        return self.balance

    def transfer(self, other_account, amount):
        """
        Transfers a specified amount to another bank account.
        :param other_account: BankAccount object to transfer money to.
        :param amount: Amount to transfer (must be non-negative and not exceed balance).
        :raises ValueError: If the amount is negative or exceeds the balance.
        """
        self.withdraw(amount)
        other_account.deposit(amount)

    def _validate_amount(self, amount):
        """
        Validates that the amount is non-negative.
        :param amount: Amount to validate.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Invalid amount")