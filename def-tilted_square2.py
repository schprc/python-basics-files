# bonus: you could have a separate function for drawing a square,
# which might be useful later:

import turtle

def square():
	for _ in range(4):
		turtle.forward(50)
		turtle.left(90)

def tilted_square():
	turtle.left(20)
	square()

tilted_square()
tilted_square()
tilted_square()
