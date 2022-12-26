from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def creat_car(self):
        space = random.randint(1, 6)
        if space == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            side_y = random.randint(-220, 220)
            new_car.goto(300, side_y)
            self.cars.append(new_car)


    def move_cars(self):

        for car in self.cars:
            car.backward(self.speed)


    def level_speeds(self):
        self.speed += MOVE_INCREMENT






