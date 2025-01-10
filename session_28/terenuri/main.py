from library import *

def init_teren_intravilan():
    """
    form, price, area, acces_stradal
    :return:
    """
    form = input("Ce fel de forma are terenul intravilan?")
    price = input("Ce pret are terenul intravilan?")
    area = input("Ce suprafata are terenul intravilan?")
    acces_stradal = input("Terenul intravilan are acces stradal?")
    return TerenIntravilan(form, price, area, acces_stradal)


if __name__ == '__main__':
    gestiune_de_terenuri = []
    # Get necessary inputs to instantiate TerenIntravilan
    gestiune_de_terenuri.append(init_teren_intravilan())