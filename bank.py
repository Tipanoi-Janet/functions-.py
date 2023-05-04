class Account:
  # Class attribute
  num_accounts = 0
  def __init__(self, account_number, balance, owner):
    # Instance variables
    self.account_number = account_number
    self.balance = balance
    self.owner = owner
    # Increment the number of accounts
    Account.num_accounts += 1
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient funds.")
  def get_account_number(self):
    return self.account_number
  def get_balance(self):
    return self.balance
  def get_owner(self):
    return self.get_owner