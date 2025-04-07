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


# Test cases
import unittest

class BankAccountTestDeposit(unittest.TestCase):
    # Tests for deposit method
    def test_deposit(self):
        account1 = BankAccount()
        ret = account1.deposit(1000)
        self.assertEqual(ret, 1000)

    def test_deposit_multiple(self):
        account1 = BankAccount()
        account1.deposit(1000)
        ret = account1.deposit(2000)
        self.assertEqual(ret, 3000)

    def test_deposit_negative(self):
        account1 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.deposit(-1000)
        self.assertEqual(str(context.exception), "Invalid amount")

    def test_deposit_zero(self):
        account1 = BankAccount()
        ret = account1.deposit(0)
        self.assertEqual(ret, 0)

class BankAccountTestWithdraw(unittest.TestCase):
    # Tests for withdraw method
    def test_withdraw(self):
        account1 = BankAccount(1000)
        ret = account1.withdraw(200)
        self.assertEqual(ret, 800)

    def test_withdraw_insufficient(self):
        account1 = BankAccount(500)
        with self.assertRaises(ValueError) as context:
            account1.withdraw(1000)
        self.assertEqual(str(context.exception), "Insufficient balance.")

    def test_withdraw_negative(self):
        account1 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.withdraw(-1000)
        self.assertEqual(str(context.exception), "Invalid amount")

class BankAccountTestViewBalance(unittest.TestCase):
    # Tests for view_balance method
    def test_view_balance(self):
        account1 = BankAccount()
        self.assertEqual(account1.view_balance(), 0)

    def test_view_balance_with_balance(self):
        account1 = BankAccount(1000)
        self.assertEqual(account1.view_balance(), 1000)

class BankAccountTestTransfer(unittest.TestCase):
    # Tests for transfer method
    def test_transfer(self):
        account1 = BankAccount(800)
        account2 = BankAccount(1000)
        account1.transfer(account2, 300)
        self.assertEqual(account1.view_balance(), 500)
        self.assertEqual(account2.view_balance(), 1300)

    def test_transfer_insufficient(self):
        account1 = BankAccount(500)
        account2 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.transfer(account2, 600)
        self.assertEqual(str(context.exception), "Insufficient balance.")

    def test_transfer_negative(self):
        account1 = BankAccount(500)
        account2 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.transfer(account2, -600)
        self.assertEqual(str(context.exception), "Invalid amount")

class BankAccountTest(unittest.TestCase):
    # Tests for a sequence of operations
    def test_sequence_operations(self):
        account1 = BankAccount()
        account2 = BankAccount()
        account1.deposit(1000)
        account1.withdraw(200)
        account1.transfer(account2, 300)
        self.assertEqual(account1.view_balance(), 500)
        self.assertEqual(account2.view_balance(), 300)

if __name__ == "__main__":
    unittest.main()