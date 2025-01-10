from library.Teren import Teren


class TerenExtravilan(Teren):
    def __init__(self, form, price, area, tip_de_sol):
        super().__init__(form, price, area)
        self.tip_de_sol = tip_de_sol
