KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti: int=KAPASITEETTI, kasvatuskoko: int=OLETUSKASVATUS):
        if kapasiteetti < 1 or kasvatuskoko < 0:
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava positiivisia kokonaislukuja")
        self.luvut = set()

    def kuuluu(self, n):
        return n in self.luvut

    def lisaa(self, n):
        if n in self.luvut:
            return False
        self.luvut.add(n)
        return True

    def poista(self, n):
        if n in self.luvut:
            self.luvut.remove(n)
            return True
        return False

    def mahtavuus(self):
        return len(self.luvut)

    def to_int_list(self):
        return list(self.luvut)

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for i in a.luvut:
            x.lisaa(i)
        for i in b.luvut:
            x.lisaa(i)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        for i in [number for number in a.luvut if number in b.luvut]:
            y.lisaa(i)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        for i in a.luvut:
            z.lisaa(i)
        for i in b.luvut:
            z.poista(i)
        return z

    def __str__(self):
        if len(self.luvut) == 0:
            return "{}"
        return str(self.luvut)
