import math
from dataclasses import dataclass


from app.shop import Shop, print_check


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict


def cost_of_km(customer: Customer, data: dict) -> int | float:
    return (customer.car["fuel_consumption"] / 100) * data["FUEL_PRICE"]


def cost_by_distance(
        customer: Customer,
        shop: Shop,
        data: dict
) -> int | float:
    return (math.dist(
        customer.location, shop.location
    ) * 2) * cost_of_km(customer, data)


def cost_of_products(customer: Customer, shop: Shop) -> int | float:
    return sum(
        [shop.products[product] * number
         for product, number in customer.product_cart.items()]
    )


def total_price(customer: Customer, shop: Shop, data: dict) -> int | float:
    return cost_by_distance(
        customer, shop, data) + cost_of_products(
        customer, shop)


def trip_and_purchase(data: dict) -> None:
    for customer_data in data["customers"]:
        customer = Customer(**customer_data)
        print(f"{customer.name} has {customer.money} dollars")

        shops = {}  # key: total_cost, value: Shop

        for shop_data in data["shops"]:
            shop = Shop(**shop_data)

            total_cost = total_price(customer, shop, data)

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(total_cost, 2)}"
            )

            shops[total_cost] = shop

        if customer.money < min(shops):
            return print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        print(f"{customer.name} rides to {shops[min(shops)].name}")

        print_check(customer.name, customer.product_cart, shops[min(shops)])

        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now has "
            f"{round(customer.money - min(shops), 2)} dollars\n"
        )
