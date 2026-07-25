import turtle
screen = turtle.Screen()
background_color = screen.bgcolor("lightblue")
screen.title("Turtle Graphics Example")
board = turtle.Turtle()
board.speed(0)
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
for i in range(36):
    board.color(colors[i % len(colors)])
    board.forward(100)
    board.right(170)
    board.width(i / 10 + 1)
board.penup()
board.goto(0, -60)
board.setheading(98)
board.pendown()
board.color("Gold" , "yellow")
board.begin_fill()
for _ in range(5):
    board.forward(120)
    board.right(144)
board.end_fill()
petal_colors = ["pink", "lightgreen", "lightblue", "lavender", "lightyellow"]
for i in range(5):
 board.color(petal_colors[i % len(petal_colors)])
board.penup()   
for j in range(5):
    board.goto(0, -60)
    board.setheading(72 * j + 36)
    board.forward(120)
    board.pendown()
    board.begin_fill()
    for _ in range(2):
        board.circle(60, 60)
        board.left(120)
        board.circle(60, 60)
        board.left(120)
    board.end_fill()
    board.penup()