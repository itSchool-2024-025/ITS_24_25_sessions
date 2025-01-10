from library.Teren import Teren


class TerenIntravilan(Teren):
    def __init__(self, form, price, area, acces_stradal):
        super().__init__(form, price, area)
        self.acces_stradal = acces_stradal

if __name__ == "__main__":
    terenint = TerenIntravilan("drept", 123, 1200, True)