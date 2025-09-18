from datetime import datetime
import json
import os
import random
os.system('clear')


class Car:
    def __init__(self, plate):
        self.plate = plate
        self.budget = random.randint(10000, 100000)

    def show_car(self):
        car = {
            'plate': self.plate,
            'budget': self.budget
        }
        return car


class CarStatus:
    def __init__(self, car: Car):
        self.plate = car.plate
        self.budget = car.budget
        self.arrival_time = None
        self.exit_time = None
        self.status = None
        self.found = False

    def enter(self):
        now = datetime.now()
        self.arrival_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.status = "in"
        self.budget = self.budget - 5000
        self.exit_time = None

    def exit(self):
        now = datetime.now()
        self.exit_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.status = "out"

    def save_car(self):
        new_car = {
            'plate': self.plate,
            'budget': self.budget,
            'arrival_time': self.arrival_time,
            'exit_time': self.exit_time,
            'status': self.status
        }
        try:
            with open('cars.json', 'r') as file:
                car_list = json.load(file)
        except FileNotFoundError:
            car_list = []

        car_list.append(new_car)

        with open('cars.json', 'w') as file:
            json.dump(car_list, file, indent=4)

    def check_car(self):
        try:
            with open('cars.json', 'r') as file:
                cars = json.load(file)
        except FileNotFoundError:
            cars = []

        self.found = False
        for car in cars:
            if self.plate == car["plate"] and car["status"] == "in":
                self.found = True
                self.exit()
                car.update({
                    "exit_time": self.exit_time,
                    "status": self.status
                })
                break
            elif self.plate == car["plate"] and car["status"] == "out":
                self.found = True
                self.enter()
                car.update({
                    'arrival_time': self.arrival_time,
                    'budget': car["budget"] - 5000,
                    'exit_time': self.exit_time,
                    'status': self.status
                })
        if not self.found:
            self.enter()
            self.save_car()
            return 0
        with open('cars.json', 'w') as file:
            json.dump(cars, file, indent=4)


class ManagerParking:
    def show_cars(self):
        text_show = ''
        with open('cars.json', 'r') as file:
            cars_list = json.load(file)
        return cars_list


if __name__ == "__main__":
    car = input("Enter Plate Number : \n")
    create_car_object = Car(car)
    print(create_car_object.show_car())
    carStatus_obj = CarStatus(create_car_object).check_car()
    car_list = ManagerParking().show_cars()
    print(car_list)