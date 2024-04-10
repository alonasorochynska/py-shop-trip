import datetime

from dataclasses import dataclass


from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict


    def print_check(self, customer: Customer):
        print(f"Date: {datetime.datetime.now}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        total_cost = 0
        for product, number in customer.product_cart.items():
            cost = self.products[product] * number
            print(f"{number} {product}s for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars"
              f"See you again!")
