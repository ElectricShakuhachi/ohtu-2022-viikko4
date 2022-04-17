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
        self.kori.lisaa_tuote(Tuote("Karkki", 3))
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 2))
        self.kori.lisaa_tuote(Tuote("Banaani", 1))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(Tuote("Laukku", 20))
        self.kori.lisaa_tuote(Tuote("Keksi", 1))
        self.assertEqual(self.kori.hinta(), 21)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_kaksi_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(Tuote("Basilika", 2))
        self.kori.lisaa_tuote(Tuote("Basilika", 2))
        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        self.kori.lisaa_tuote(Tuote("Sipuli", 2))
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_ostos_jonka_nimi_sama_ja_lukumaara_yksi(self):
        self.kori.lisaa_tuote(Tuote("Kinkku", 4))
        self.assertEqual(self.kori.ostokset()["Kinkku"].tuotteen_nimi(), "Kinkku")
        self.assertEqual(self.kori.ostokset()["Kinkku"].lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(Tuote("Kurkku", 3))
        self.kori.lisaa_tuote(Tuote("Salmiakki", 1))
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(Tuote("Limppu", 2))
        self.kori.lisaa_tuote(Tuote("Limppu", 2))
        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_tuote_jonka_nimi_on_lisatty_tuote_ja_lukumaara_2(self):
        self.kori.lisaa_tuote(Tuote("Hiiva", 1))
        self.kori.lisaa_tuote(Tuote("Hiiva", 1))
        self.assertEqual(self.kori.ostokset()["Hiiva"].tuotteen_nimi(), "Hiiva")
        self.assertEqual(self.kori.ostokset()["Hiiva"].lukumaara(), 2)

    def test_jos_korissa_kaksi_samaa_tuotetta_toisen_poistamisen_jalkeen_yksi_ostos_jonka_maara_1(self):
        self.kori.lisaa_tuote(Tuote("Tomaatti", 2))
        self.kori.lisaa_tuote(Tuote("Tomaatti", 2))
        self.kori.poista_tuote(Tuote("Tomaatti", 2))
        self.assertEqual(self.kori.ostokset()["Tomaatti"].tuotteen_nimi(), "Tomaatti")
        self.assertEqual(self.kori.ostokset()["Tomaatti"].lukumaara(), 1)

    def test_jos_koriin_on_lisatty_yksi_tuote_ja_sama_poistetaan_on_kori_tyhja(self):
        self.kori.lisaa_tuote(Tuote("Oliivi", 1))
        self.kori.poista_tuote(Tuote("Oliivi", 1))
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.hinta(), 0)
