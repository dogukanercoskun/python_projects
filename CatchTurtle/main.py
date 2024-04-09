import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch Turtle")
FONT = ('Arial', 30, 'normal')
grad_size = 20
score = 0
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
game_over = False



def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score : 0", move=False, align="center", font=FONT)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time : {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def handle_click(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(arg=f"Score : {score}", move=False, align="center", font=FONT)



def make_turtle():
    global game_over
    t = turtle.Turtle(visible=False)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    screen_size = turtle.screensize()
    w = screen_size[0]
    h = screen_size[1]
    x = random.randint(-w, w)
    y = random.randint(-h, h)
    turtle.tracer(0)
    t.showturtle()
    t.goto(x, y)
    t.onclick(handle_click)
    turtle.tracer(1)

    def remove_turtle():
        t.hideturtle()
        if not game_over:
            make_turtle()

    screen.ontimer(remove_turtle, 800)


def startup_game():

    setup_score_turtle()
    countdown(10)
    make_turtle()


startup_game()
turtle.mainloop()
