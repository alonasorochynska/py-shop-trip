from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict


def print_check(name: str, product_cart: dict, shop: Shop) -> None:
    print(f"\nDate: 04/01/2021 12:33:41\n"
          f"Thanks, {name}, for your purchase!\n"
          f"You have bought:")
    total_cost = 0
    for product, number in product_cart.items():
        cost = shop.products[product] * number
        print(f"{number} {product}s for {cost} dollars")
        total_cost += cost
    print(f"Total cost is {round(total_cost, 2)} dollars\n"
          f"See you again!\n")
