class Auto:
    def __init__(self, marka_, tipus_, gyartasi_ev):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = int(gyartasi_ev)
        self.sebesseg = 0

    def __str__(self):
        return f"{self.marka} {self.tipus} {self.gyartasi_ev}, sebesség:{self.sebesseg}"

    def gyorsit(self, ertek):
        self.sebesseg += ertek
        if self.sebesseg > 200:
            self.sebesseg = 200

    def lassit(self, ertek):
        self.sebesseg -= ertek
        if self.sebesseg < 0:
            self.sebesseg = 0
            print("Megaltal")
