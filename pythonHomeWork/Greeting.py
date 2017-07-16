class Greeting:
	def __init__(self, name):
		self.name = name
	def __del__(self):
		print("destructor started")
	def SayHello(self):
		print("Hello "), self.name
	"""docstring for ClassName"""
		