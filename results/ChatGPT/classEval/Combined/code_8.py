class BankAccount:
    """
    A class representing a bank account that supports deposit, withdrawal, balance viewing, and money transfers.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with a given balance (default is 0).
        :param balance: Initial account balance (default is 0)
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        
        :param amount: Amount to deposit (must be non-negative)
        :return: Current account balance after deposit
        :raises ValueError: If amount is negative
        """
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.
        
        :param amount: Amount to withdraw (must be non-negative and not exceed balance)
        :return: Current account balance after withdrawal
        :raises ValueError: If amount is negative or exceeds available balance
        """
        self._validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        """
        Returns the current account balance.
        
        :return: Current balance
        """
        return self.balance

    def transfer(self, other_account, amount):
        """
        Transfers a specified amount to another bank account.
        
        :param other_account: The target BankAccount to transfer to
        :param amount: Amount to transfer (must be non-negative and not exceed balance)
        :raises ValueError: If amount is negative or exceeds available balance
        """
        self.withdraw(amount)
        other_account.deposit(amount)

    @staticmethod
    def _validate_amount(amount):
        """
        Validates that the amount is non-negative.
        
        :param amount: Amount to validate
        :raises ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Invalid amount")