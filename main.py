import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

bet = screen.textinput(title="Make a bet", prompt="Which turtle win win the race? Enter a color: ")
while bet not in colors:
    if bet is None:
        screen.exitonclick()
    print(f"There is no {bet} turtle participating in the race. Try again")
    bet = screen.textinput(title="Make a bet", prompt="Which turtle win win the race? Enter a color: ")

all_turtles = []

y_coord = -70
for i in range(6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=y_coord + (30 * i))
    all_turtles.append(turtle)


def finish_line():
    finish_line_turtle = Turtle()
    finish_line_turtle.hideturtle()
    finish_line_turtle.penup()
    finish_line_turtle.goto(x=220, y=110)
    finish_line_turtle.right(90)
    finish_line_turtle.pendown()
    finish_line_turtle.pensize(5)
    finish_line_turtle.forward(200)


is_race_on = False

if bet in colors:
    is_race_on = True
    finish_line()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won! The {winning_color} turtle won the race!")
            else:
                print(f"You Lost. The {winning_color} turtle won the race!")
            break
        turtle.forward(random.randint(1, 10))

screen.exitonclick()
