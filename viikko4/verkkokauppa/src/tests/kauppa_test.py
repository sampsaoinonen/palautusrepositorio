import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 100
            if tuote_id == 2:
                return 200
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 10)
            if tuote_id == 3:
                return Tuote(3, "kananmuna", 15)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):        
        self.viitegeneraattori_mock.uusi.return_value = 42
                    
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called()


    def test_yhden_tuotteen_ostoksessa_tilisiirto_metodia_kutsutaan(self):            
        self.viitegeneraattori_mock.uusi.return_value = 52
                
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Matti Esko", "545")
        self.pankki_mock.tilisiirto.assert_called_with("Matti Esko", 52, "545", "33333-44455", 10)

    def test_kahden_eri_tuotteen_ostoksessa_tilisiirto_metodia_kutsutaan(self):        
        self.viitegeneraattori_mock.uusi.return_value = 62

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Matti Pekka", "555")
        self.pankki_mock.tilisiirto.assert_called_with("Matti Pekka", 62, "555", "33333-44455", 15)

    def test_kahden_saman_tuotteen_ostoksessa_tilisiirto_metodia_kutsutaan(self):        
        self.viitegeneraattori_mock.uusi.return_value = 72

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Matti Jorma", "555")
        self.pankki_mock.tilisiirto.assert_called_with("Matti Jorma", 72, "555", "33333-44455", 10)

    def test_tuotteen_ostoksessa_tilisiirto_metodia_kutsutaan(self):        
        self.viitegeneraattori_mock.uusi.return_value = 82
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("Matti Saukki", "555")
        self.pankki_mock.tilisiirto.assert_called_with("Matti Saukki", 82, "555", "33333-44455", 5)

    def test_aloita_asiointi_kutsuminen_nollaa_tiedot(self):
        self.viitegeneraattori_mock.uusi.return_value = 92

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Matti Saukki", "555")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Jorkki", "444")
        self.pankki_mock.tilisiirto.assert_called_with("Jorkki", 92, "444", "33333-44455", 5)

    def test_uusi_viitenumero_joka_tapahtumalle(self):
        self.viitegeneraattori_mock.uusi.return_value = 92

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Jukka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.viitegeneraattori_mock.uusi.return_value = 93
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Jukka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.viitegeneraattori_mock.uusi.return_value = 94
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Jukka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_poista_ostoksen_lisays(self):
        self.viitegeneraattori_mock.uusi.return_value = 100
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("Pertsa", "123")
        self.pankki_mock.tilisiirto.assert_called_with("Pertsa", 100, "123", "33333-44455", 5)