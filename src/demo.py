import math

class point():
	'''class to define structure of a point'''
	
	def __init__(self, x, y):
		'''initialise with (0, 0)'''
		self.x = x
		self.y = y
		return

	def __str__(self):
		'''prety print a point'''
		return "(%g, %g)"%(self.x, self.y)

class rectange():
	'''rectangle interface'''

	def __init__(self, corner, width, height):
		'''initialise rectange'''
		self.width = width
		self.height = height
		self.corner1 = corner
		self.corner2 = point(self.corner1.x + width, self.corner1.y + height)
		
	def __str__(self):
		'''pretty print rectange'''
		output = []
		for i in range(self.width):
			output.append('**') #create side1
		output.append('\n')

		for i in range(self.height):
			output.append("*")
			for j in range(self.width - 1):
				output.append("  ")
			output.append("*\n")

		for i in range(self.width):
			output.append('**') #create side1
		output.append('\n')

		return "".join(output)

def trycatch():
	'''demonstrate try catch'''
	try:
		while True:
			print "Hello"
	except KeyboardInterrupt:
		print "Key board interrupted by user"
	finally:
		print "Good byE!"

if __name__ == '__main__':
	'''main function'''
	#p1 = point(2, 3)
	#p2 = point(4, 3)
	#corner = point(1, 1)
	#h = 10
	#w = 2
	#rect = rectange(corner, h, w)
	#print rect
	trycatch()
