import unittest

from wisielec import wyswietl_stan, wybierz_slowo, POZIOMY


class TestLogikiGry(unittest.TestCase):
    def test_wyswietl_stan(self):
       slowo = "ORZEŁ"
       odgadniete = {'R','E'}
       self.assertEqual(wyswietl_stan(slowo,odgadniete), "_ R _ E _", "Stan powinien poprawnie pokazywac odgadniete litery.")

       slowo_puste = "TEST"
       self.assertEqual(wyswietl_stan(slowo_puste, set()),"_ _ _ _", "Wszytskie litery powinne byc zakryte.")

    def test_wybierz_slowo_dlugosc(self):
        # Sprawdzenie, czy dla poziomu "ŚREDNI" słowo jest odpowiedniej długości
        poziom = "🟡 ŚREDNI"
        kategoria = "🐾 ZWIERZĘTA"  # musi mieć słowa w tym zakresie
        slowo = wybierz_slowo(kategoria, poziom)

        min_dl = POZIOMY[poziom]['min_długość']
        max_dl = POZIOMY[poziom]['max_długość']

        self.assertTrue(min_dl <= len(slowo) <= max_dl,
                        f"Słowo powinno mieć od {min_dl} do {max_dl} liter.")


# Uruchomienie testów
if __name__ == '__main__':
    unittest.main()