class Counter(object):
	"""docstring for ClassName"""
	number = 0

	def __init__(self):
		type(self).number += 1

	def __del__(self):
		type(self).number -= 1

class Account(Counter):
	"""docstring for ClassName"""
	def __init__(self, holder, number, balance, credit_line=1500):
		self.__Holder = holder
		self.__Number = number
		self.__Balance = balance
		self.__CreditLine = credit_line
		Counter.__init__(self)
		pass

	def transfer(self, target, amount):
		if (self.Balance - amount < -self.CreditLine):
			#insufficient balance
			return False
		else:
			self.Balance -= amount
			target.Balance += amount
			return True
			pass
		pass
	def deposit(self, amount):
		self.Balance = amount
		pass
	def withdraw(self, amount):
		if (self.Balance - amount < -self.CreditLine):
			#insufficient balance
			return False
		else:
			self.Balance -= amount
			return True
			pass
		pass
	def balance(self):
		return self.Balance
		pass
	def __del__(self):
		Account.counter -= 1





		