

class LowFuelError(Exception):
    "Исключение, возникающее при недостаточном уровне топлива для старта."
    pass

class NotEnoughFuel(Exception):
    "Исключение, возникающее при недостаточном топливе для движения."
    pass

class CargoOverload(Exception):
    "Исключение, возникающее при перегрузке грузоподъемности."
    pass