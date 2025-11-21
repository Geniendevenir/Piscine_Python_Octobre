class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		if not isinstance(new_account, Account):
			return False
		if self.fix_account(new_account) == False:
			return False
		if new_account in self.accounts:
			return False
		self.accounts.append(new_account)
		return True

	def transfer(self, origin, dest, amount):
		if not isinstance(origin, str) or not isinstance(dest, str):
			return False

		originAccount = None
		for account in self.account:
			if account.name == origin:
				originAccount = account

		destAccount = None
		for account in self.account:
			if account.name == dest:
				destAccount = account

		if originAccount is None or destAccount is None:
			return False

		if self.fix_account(origin) == False or self.fix_account(dest):
			return False

		if originAccount.value < 0 or amount > originAccount.value:
			return False	
		
		if originAccount == destAccount:
			return True
		
		originAccount.value -= amount
		destAccount.value += amount

		return True
		

	def fix_account(self, name):
		if not isinstance(name, str):
			return False

		corruptedAccount = None
		for account in self.account:
			if account.name == name:
				corruptedAccount = account
		if corruptedAccount is None:
			return False

		if len(dir(corruptedAccount)) % 2 == 0:
			return False
		if str.startswith("b") in dir(corruptedAccount):
			return False
		if str.startswith("zip") not in dir(corruptedAccount):
			return False
		if str.startswith("addr") not in dir(corruptedAccount):
			return False
		if not hasattr(corruptedAccount, "name") or not hasattr("id") or not hasattr("value"):
			return False
		if not isinstance(getattr(corruptedAccount, "name"), str):
			return False
		if not isinstance(getattr(corruptedAccount, "id"), int):
			return False
		if not isinstance(getattr(corruptedAccount, "value"), int) or not isinstance(getattr(corruptedAccount, "value"), float):
			return False
		
		return True

		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
	# ... Your code ..