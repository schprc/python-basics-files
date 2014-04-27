import turtle

def tilted_square():
	turtle.left(20)     # now we can change the angle only here
	for _ in range(4):
		turtle.forward(50)
		turtle.left(90)

tilted_square()
tilted_square()
tilted_square()


