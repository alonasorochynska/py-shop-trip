import json


from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    with open("config.json", "r") as f:
        data = json.load(f)


    for customer_data in data["customers"]:
        customer = Customer(**customer_data)
        print(f"{customer.name} has {customer.money} dollars")

        shops = {}  # key: total_cost, value: Shop

        for shop_data in data["shops"]:
            shop = Shop(**shop_data)

            total_cost = customer.total_cost(customer.car, shop)

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {total_cost}"
            )

            shops[total_cost] = shop




