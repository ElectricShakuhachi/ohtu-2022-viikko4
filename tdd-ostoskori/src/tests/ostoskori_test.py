import unittest
from unittest.mock import Mock, ANY
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_1_tavara(self):
        self.kori.lisaa_tuote(Tuote("Omena", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(Tuote("Omena", 2))
        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Omena", 2))
        self.kori.lisaa_tuote(Tuote("Banaani", 1))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(Tuote("Omena", 2))
        self.kori.lisaa_tuote(Tuote("Banaani", 1))
        self.assertEqual(self.kori.hinta(), 3)