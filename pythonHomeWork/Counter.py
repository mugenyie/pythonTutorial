class Counter(object):
	"""docstring for ClassName"""
	number = 0

	def __init__(self):
		type(self).number += 1

	def __del__(self):
		type(self).number -= 1


		