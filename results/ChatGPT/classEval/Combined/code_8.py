class BankAccount:
    """
    A class representing a bank account system, which supports depositing money, withdrawing money, viewing balance, and transferring money.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance. Default value is 0.
        :param balance: Initial balance of the account.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance.
        :param amount: Amount to deposit (must be non-negative).
        :return: Current account balance after deposit.
        :raises ValueError: If amount is negative.
        """
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance.
        :param amount: Amount to withdraw (must be non-negative and not greater than balance).
        :return: Current account balance after withdrawal.
        :raises ValueError: If amount is negative or exceeds the current balance.
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
        Transfers a certain amount from the current account to another account.
        :param other_account: BankAccount instance to transfer money to.
        :param amount: Amount to transfer (must be non-negative and not greater than balance).
        :raises ValueError: If amount is negative or exceeds the current balance.
        """
        self.withdraw(amount)
        other_account.deposit(amount)

    def _validate_amount(self, amount):
        """
        Validates the amount for deposit and withdrawal.
        :param amount: Amount to validate.
        :raises ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Invalid amount")