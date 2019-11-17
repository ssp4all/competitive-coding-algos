class dog:
	def __init__(self, name):
		self.name = name

class xyz(dog):
	def __init__(self, tail):
		self.tail = tail
		dog.__init__(self, "dog")

x = xyz("abc")
print(x.name)