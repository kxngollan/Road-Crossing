from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Road Crossing")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

playing = True

while playing:
    screen.update()
    time.sleep(scoreboard.game_speed)

    cars.car_odds()
    cars.move()

    if player.ycor() > 260:
        player.reset()
        scoreboard.increase_level()
        print(scoreboard.game_speed)

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            playing = False
    
screen.exitonclick()