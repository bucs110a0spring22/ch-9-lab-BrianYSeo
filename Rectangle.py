class Rectangle:
	def __init__(self, x, y, h, w):
		if x < 0:
			self.x = 0
		else:
			self.x = x
		if y < 0:
			self.y = 0
		else:
			self.y = y
		if h < 0:
			self.height = 0
		else:
			self.height = h
		if w < 0:
			self.width = 0
		else:
			self.width = w
	def __str__(self):
		return f"Your rectangle is at ({self.x},{self.y}). The height of the rectangle is {self.height} and the width is {self.width}."