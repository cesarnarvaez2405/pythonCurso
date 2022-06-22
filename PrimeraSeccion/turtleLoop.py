
print("This will execute first")

for _ in range (3):
    print("Primera vaina")
    print("Segunda vaina")

print("Probando como es fuera del loop")

import turtle

wn = turtle.Screen()
elan = turtle.Turtle()
juan = turtle.Turtle()
juan.color("blue")
juan.pensize(10)

distance = 70
angle = 90
for _ in range(6):
    elan.forward(distance)
    elan.left(angle)
    

for _ in range (3):
    elan.forward(distance)
    elan.left(120)

for _ in range(4):
    juan.right(90)
    juan.forward(distance)
    
wn.exitonclick()