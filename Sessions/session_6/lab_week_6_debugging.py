class Car:

    def __init__(self, initial_speed: int = 0) -> None:
        self.current_speed = initial_speed
        self.distance_km = 0
        self.tick_count = 0

    def accelerate(self) -> None:
        speed_step = 5
        self.current_speed += speed_step

    # def brake(self):
    #     self.speed -= 5

    def brake(self):
        speed_step = 5
        if self.current_speed >= speed_step:
            self.current_speed -= speed_step
        else:
            self.current_speed = 0

    def step(self)  -> None:
        self.distance_km += self.current_speed
        self.tick_count += 1

    def average_speed(self) -> float:
        return self.distance_km / self.tick_count


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        menu_choice = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if menu_choice not in "ABOS" or len(menu_choice) != 1:
            print("I don't know how to do that")
            continue
        if menu_choice == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif menu_choice == 'B':
            my_car.brake()
            print("Braking...")
        elif menu_choice == 'O':
            print("The car have drove {} kilometers".format(my_car.distance_km))
        elif menu_choice == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()