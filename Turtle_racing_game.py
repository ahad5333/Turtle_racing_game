from turtle import Turtle, Screen
import random

# --- Setup screen ---
screen = Screen()
screen.setup(width=900, height=500)
screen.bgcolor("lightblue")
screen.title("🏁 Turtle Race Game 🐢")

# --- Draw finish line ---
finish_line = Turtle()
finish_line.penup()
finish_line.hideturtle()
finish_line.goto(400, 200)
finish_line.pendown()
finish_line.color("black")
finish_line.pensize(3)
finish_line.right(90)
finish_line.forward(400)
finish_line.penup()
finish_line.goto(400, 220)
finish_line.write("FINISH", align="center", font=("Arial", 16, "bold"))

# --- Draw race tracks ---
track_drawer = Turtle()
track_drawer.hideturtle()
track_drawer.speed(0)
track_drawer.color("white")
track_drawer.penup()
track_drawer.goto(-450, -100)
for i in range(6):
    track_drawer.pendown()
    track_drawer.forward(850)
    track_drawer.penup()
    track_drawer.goto(-450, -100 + (i + 1) * 50)

# --- Colors & positions ---
colors = ["red", "yellow", "green", "blue", "purple", "black"]
y_positions = [-75, -25, 25, 75, 125, 175]

# --- User bet ---
user_bet = screen.textinput(
    title="Place your Bet 🏁", 
    prompt="Which turtle will win the race? (red, yellow, green, blue, purple, black): "
)

# --- Create turtles ---
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-420, y=y_positions[i])
    all_turtles.append(new_turtle)

# --- Start race ---
is_race_on = bool(user_bet)
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:  # finish line
            is_race_on = False
            winning_color = turtle.pencolor()

            # Display winner on screen
            announcer = Turtle()
            announcer.hideturtle()
            announcer.penup()
            announcer.goto(0, 0)
            if winning_color == user_bet:
                announcer.color("green")
                announcer.write(f"🎉 You Won! The {winning_color} turtle won!", align="center", font=("Arial", 20, "bold"))
            else:
                announcer.color("red")
                announcer.write(f"😞 You Lost! The {winning_color} turtle won!", align="center", font=("Arial", 20, "bold"))
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
