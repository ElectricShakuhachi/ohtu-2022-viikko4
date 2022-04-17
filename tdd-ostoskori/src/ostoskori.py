from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._ostokset.values()])

    def hinta(self):
        return sum([ostos.hinta() for ostos in self._ostokset.values()])

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() not in self._ostokset:
            self._ostokset[lisattava.nimi()] = Ostos(lisattava)
        else:
            self._ostokset[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi() not in self._ostokset:
            pass
        if self._ostokset[poistettava.nimi()].lukumaara() > 1:
            self._ostokset[poistettava.nimi()].muuta_lukumaaraa(-1)
        else:
            self._ostokset.pop(poistettava.nimi())

    def tyhjenna(self):
        self._ostokset = {}

    def ostokset(self):
        return self._ostokset
