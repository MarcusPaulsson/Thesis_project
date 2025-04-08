class BankAccount:
    """
    A class representing a bank account.

    Supports deposit, withdraw, balance view, and transfer functionalities.
    """

    def __init__(self, balance=0):
        """
        Initializes a BankAccount object.

        Args:
            balance (int, optional): Initial balance of the account. Defaults to 0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount (int): The amount to deposit.

        Returns:
            int: The updated balance after the deposit.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.

        Args:
            amount (int): The amount to withdraw.

        Returns:
            int: The updated balance after the withdrawal.

        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            int: The current balance.
        """
        return self.balance

    def transfer(self, other_account, amount):
        """
        Transfers money from this account to another account.

        Args:
            other_account (BankAccount): The account to transfer money to.
            amount (int): The amount to transfer.

        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.withdraw(amount)
        other_account.deposit(amount)