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

    
