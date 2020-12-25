import objects


def star_hub_txlvl():
    return float(objects.star_hub_200x_json()['data']['modulator_txlvl'])
