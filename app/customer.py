import math

from dataclasses import dataclass


from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def cost_by_distance(self, car: Car, shop: Shop):
        return (math.dist(self.location, shop.location) * 2) * car.cost_of_km()

    def cost_of_products(self, shop: Shop):
        return sum([shop.products[product] * number for product, number in self.product_cart.items()])

    def total_cost(self, car: Car, shop: Shop):
        return self.cost_by_distance(car, shop) + self.cost_of_products(shop)
