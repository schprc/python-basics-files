import turtle

i = 5

for i in range(20):
    print(i)
    turtle.forward(i+5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()