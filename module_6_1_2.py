class Car:
    def __init__(self):
        self.price = 1000000
    def horse_powers(self):
        return "Unknown"
class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000
    def horse_powers(self):
        return 300
class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 1200000
    def horse_powers(self):
        return 250


nissan_car = Nissan()
print(f"Nissan car price: {nissan_car.price}")
print(f"Nissan car horse powers: {nissan_car.horse_powers()}")

kia_car = Kia()
print(f"Kia car price: {kia_car.price}")
print(f"Kia car horse powers: {kia_car.horse_powers()}")