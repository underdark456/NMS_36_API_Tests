from modulator import modulator_txlvl
from JSON_POST import star_hub_txlvl

if star_hub_txlvl() == modulator_txlvl():
    print(f'OK! web value: {modulator_txlvl()} \n\tAPI value: {star_hub_txlvl()}')
else:
    print('hueta')