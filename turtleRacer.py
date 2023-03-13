import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['Red', 'Green', 'Blue', 'Orange', 'Yellow', 'Black', 'Purple','Pink', 'Brown', 'Cyan']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try again!")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                winner_color = colors[turtles.index(racer)]
                winner_turtle = turtle.Turtle()
                winner_turtle.hideturtle()
                winner_turtle.penup()
                winner_turtle.setpos(0, 0)
                winner_turtle.write("Winner: {} Turtle!".format(winner_color), align="center", font=("Arial", 24, "bold"))
                time.sleep(5)
                return winner_color


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color, in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racer")

    # Add countdown timer
    countdown_turtle = turtle.Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setpos(0, 0)
    countdown_turtle.write("3", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("2", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("1", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown_turtle.clear()


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
