from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Make you bet", prompt="Choose a color of your turtle: ").lower()
colors = ['orange', 'indigo', 'red', 'green', 'yellow', 'blue']
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
for i in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

if choice:
    is_on = True
while is_on:
    for turtle in turtles:
        turtle.fd(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_on = False
            if choice == turtle.pencolor():
                print(f"You've won the winner is: {turtle.pencolor()} turtle")
            else:
                print(f"You've lost the winner is: {turtle.pencolor()} turtle")


screen.exitonclick()
