from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black"]


class Cars():
    def __init__(self):
        self.all_cars = []

    def car_odds(self):
        n = random.randint(1,6)
        if n == 1:
            self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        y = random.randint(-23,23)*10
        new_car.goto(300, y)
        self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(random.randint(5,20))