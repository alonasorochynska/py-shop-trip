from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    fuel_price: float

    def cost_of_km(self):
        return (self.fuel_consumption / 100) * self.fuel_price
