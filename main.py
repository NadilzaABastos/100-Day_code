import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game")
screen.tracer(0)

player = Player()

screen.listen()
car_manager = CarManager()
screen.onkey(player.up, "Up")

scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creat_car()
    car_manager.move_cars()

    # Car collision

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Level UP
        if player.linha_fnal():
            player.level_up()
            car_manager.level_speeds()
            scoreboard.point()




screen.exitonclick()