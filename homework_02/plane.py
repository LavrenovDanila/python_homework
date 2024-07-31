# plane.py

from base import Vehicle
import exceptions

class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise exceptions.CargoOverload("Перегрузка! Максимальный груз превышен.")
        self.cargo += amount

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo