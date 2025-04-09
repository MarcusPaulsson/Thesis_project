class BankAccount:
    """
    This class implements a bank account system, which supports depositing money,
    withdrawing money, viewing balance, and transferring money.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance. Default value is 0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance.
        Returns the current account balance.
        Raises ValueError for negative amounts.
        :param amount: float
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance.
        Returns the current account balance.
        Raises ValueError for negative amounts or insufficient balance.
        :param amount: float
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        """
        Returns the account balance.
        """
        return self.balance

    def transfer(self, other_account, amount):
        """
        Transfers a certain amount from the current account to another account.
        Raises ValueError for negative amounts or insufficient balance.
        :param other_account: BankAccount
        :param amount: float
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.withdraw(amount)
        other_account.deposit(amount)

