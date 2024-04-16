import json


from app.customer import trip_and_purchase


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    trip_and_purchase(data)


# print(shop_trip())
