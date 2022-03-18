class Car:
    def __init__(self, speed, color, name):
        self.is_police = False
        self.name = name
        self.color = color
        self.max_speed = speed
        self.speed = 0
        self.direction = 'ahead'

    def go(self, speed):
        if speed > self.max_speed:
            print(f'{self.name} can not do this. Too Fast!!')
        else:
            self.speed = speed
            print(f'{self.name} riding at {self.speed} km/h')
        return self.speed

    def stop(self):
        self.speed = 0
        print(f'{self.name} stopped')
        return self.speed

    def turn(self, direction):
        if self.speed != 0:
            self.direction = direction
            print(f'{self.name} turned to the {self.direction}')
        else:
            print(f"{self.name} isn't riding now, it can't turn")
        return self.direction

    def show_speed(self):
        if self.speed > 0:
            print(f'{self.name} riding now at {self.speed} km/h')
        else:
            print(f'{self.name} not riding now')
        return self.speed


class TownCar(Car):

    speed_limit = 60

    def go(self, speed):
        self.speed = speed
        if self.speed <= TownCar.speed_limit:
            print(f'car riding at {self.speed} km/h')
        else:
            print(f'{self.name} riding too fast!!!! ({self.speed})')
        return self.speed


class WorkCar(TownCar):
    TownCar.speed_limit = 40


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


ferrari = SportCar(350, 'RED', 'Ferrari F360 Modena')
lifan = TownCar(150, 'BLUE', 'Lifan Smiley')
gaz = WorkCar(100, 'WHITE', 'GAZelle')
cop_car = PoliceCar(250, 'Special', 'Ford Crown Victoria')

ferrari.go(300)
lifan.show_speed()
lifan.go(100)
lifan.show_speed()
ferrari.stop()
gaz.turn('right')
print(gaz.direction)
gaz.go(50)
gaz.turn('left')
print(gaz.direction)
print(ferrari.is_police)
print(cop_car.color)
print(cop_car.is_police)
cop_car.show_speed()
cop_car.go(100)
cop_car.show_speed()
