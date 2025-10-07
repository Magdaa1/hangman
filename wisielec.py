import random
import time

# Baza słów z kategoriami
KATEGORIE = {
    "🐾 ZWIERZĘTA": [
        "KOT", "PIES", "SŁOŃ", "TYGRYS", "LEW", "ŻYRAFA", "HIPOPOTAM", "KROKODYL",
        "PINGWIN", "DELFIN", "REKIN", "WIELORYB", "ORZEŁ", "SOKÓŁ", "PAPUGA"
    ],
    "🏙️ MIASTA": [
        "WARSZAWA", "KRAKÓW", "GDAŃSK", "WROCŁAW", "POZNAŃ", "ŁÓDŹ", "SZCZECIN",
        "BYDGOSZCZ", "LUBLIN", "KATOWICE", "BIAŁYSTOK", "RZESZÓW", "TORUŃ"
    ],
    "💼 ZAWODY": [
        "PROGRAMISTA", "LEKARZ", "NAUCZYCIEL", "INŻYNIER", "ARCHITEKT", "PRAWNIK",
        "KSIĘGOWY", "DZIENNIKARZ", "AKTOR", "MUZYK", "MALARZ", "KUCHARZ"
    ],
    "💻 TECHNOLOGIA": [
        "PYTHON", "ALGORYTM", "KOMPUTER", "INTERNET", "APLIKACJA", "PROGRAM",
        "BAZA", "SERWER", "KLIENT", "PROTOKÓŁ", "FRAMEWORK", "BIBLIOTEKA"
    ],
    "🌍 GEOGRAFIA": [
        "KONTYNENT", "OCEAN", "GÓRA", "RZEKA", "JEZIORO", "PUSTYNIA", "LAS",
        "WYSPA", "PÓŁWYSEP", "ZATOKA", "CIEŚNINA", "ARCHIPELAG"
    ]
}

# Poziomy trudności
POZIOMY = {
    "🟢 ŁATWY": {
        "opis": "Krótkie słowa, więcej prób",
        "min_długość": 3,
        "max_długość": 6,
        "max_błędów": 8,
        "podpowiedzi": 2
    },
    "🟡 ŚREDNI": {
        "opis": "Średnie słowa, standardowe zasady",
        "min_długość": 5,
        "max_długość": 9,
        "max_błędów": 6,
        "podpowiedzi": 1
    },
    "🔴 TRUDNY": {
        "opis": "Długie słowa, mniej prób",
        "min_długość": 8,
        "max_długość": 15,
        "max_błędów": 4,
        "podpowiedzi": 0
    },
    "💀 EKSPERT": {
        "opis": "Tylko dla mistrzów!",
        "min_długość": 10,
        "max_długość": 15,
        "max_błędów": 3,
        "podpowiedzi": 0
    }
}


def wyswietl_menu_kategorii():
    """Wyświetla menu wyboru kategorii"""
    print("\n🎯 === WYBIERZ KATEGORIĘ ===")
    kategorie_lista = list(KATEGORIE.keys())

    for i, kategoria in enumerate(kategorie_lista, 1):
        ile_słów = len(KATEGORIE[kategoria])
        print(f"{i}. {kategoria} ({ile_słów} słów)")

    print(f"{len(kategorie_lista) + 1}. 🎲 LOSOWA KATEGORIA")

    while True:
        try:
            wybor = int(input(f"\nWybierz (1-{len(kategorie_lista) + 1}): "))
            if 1 <= wybor <= len(kategorie_lista):
                return kategorie_lista[wybor - 1]
            elif wybor == len(kategorie_lista) + 1:
                return random.choice(kategorie_lista)
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj liczbę!")


def wyswietl_menu_poziomu():
    """Wyświetla menu wyboru poziomu trudności"""
    print("\n⚡ === WYBIERZ POZIOM TRUDNOŚCI ===")
    poziomy_lista = list(POZIOMY.keys())

    for i, poziom in enumerate(poziomy_lista, 1):
        info = POZIOMY[poziom]
        print(f"{i}. {poziom}")
        print(f"   {info['opis']}")
        print(f"   Słowa: {info['min_długość']}-{info['max_długość']} liter | "
              f"Błędy: {info['max_błędów']} | Podpowiedzi: {info['podpowiedzi']}")

    while True:
        try:
            wybor = int(input(f"\nWybierz (1-{len(poziomy_lista)}): "))
            if 1 <= wybor <= len(poziomy_lista):
                return poziomy_lista[wybor - 1]
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj liczbę!")


def wybierz_slowo(kategoria, poziom):
    """Wybiera słowo odpowiednie dla poziomu trudności"""
    słowa_kategorii = KATEGORIE[kategoria]
    poziom_info = POZIOMY[poziom]

    # Filtruj słowa według długości
    odpowiednie_słowa = [
        słowo for słowo in słowa_kategorii
        if poziom_info['min_długość'] <= len(słowo) <= poziom_info['max_długość']
    ]

    if not odpowiednie_słowa:
        # Fallback - weź wszystkie słowa z kategorii
        odpowiednie_słowa = słowa_kategorii

    return random.choice(odpowiednie_słowa).upper()


def wyswietl_stan(slowo, odgadniete):
    """Wyświetla stan słowa z odgadniętymi literami"""
    return " ".join([litera if litera in odgadniete else "_" for litera in slowo])


def użyj_podpowiedzi(slowo, odgadniete, pozostałe_podpowiedzi):
    """System podpowiedzi"""
    if pozostałe_podpowiedzi <= 0:
        print("❌ Brak dostępnych podpowiedzi!")
        return odgadniete, pozostałe_podpowiedzi

    print("\n💡 === PODPOWIEDZI ===")
    print("1. 🔤 Odkryj losową literę")
    print("2. 📊 Pokaż częstotliwość liter")
    print("3. ❌ Anuluj")

    try:
        wybor = int(input("Wybierz podpowiedź (1-3): "))

        if wybor == 1:
            # Odkryj losową literę
            nieoddane = [l for l in slowo if l not in odgadniete]
            if nieoddane:
                nowa_litera = random.choice(nieoddane)
                odgadniete.add(nowa_litera)
                print(f"✨ Odkrywam literę: {nowa_litera}")
                return odgadniete, pozostałe_podpowiedzi - 1

        elif wybor == 2:
            # Częstotliwość liter w alfabecie polskim
            częstotliwość = {
                'A': 8.91, 'E': 7.66, 'I': 8.21, 'O': 7.75, 'Y': 3.76,
                'N': 5.52, 'R': 4.69, 'S': 4.32, 'T': 3.98, 'L': 3.51,
                'K': 3.51, 'M': 2.80, 'P': 3.13, 'W': 4.65, 'Z': 5.64,
                'C': 3.96, 'D': 3.25, 'B': 1.47, 'G': 1.42, 'H': 1.08
            }

            print("\n📊 Najczęstsze litery w języku polskim:")
            sorted_letters = sorted(częstotliwość.items(), key=lambda x: x[1], reverse=True)
            for i, (litera, freq) in enumerate(sorted_letters[:10], 1):
                status = "✅" if litera in odgadniete else "⬜"
                print(f"{i:2}. {litera} ({freq}%) {status}")

            return odgadniete, pozostałe_podpowiedzi - 1

        elif wybor == 3:
            return odgadniete, pozostałe_podpowiedzi

    except ValueError:
        print("❌ Nieprawidłowy wybór!")

    return odgadniete, pozostałe_podpowiedzi


def wyswietl_wisielca(bledy):
    """ASCII art wisielca"""
    wisielce = [
        """
   +---+
   |   |
       |
       |
       |
       |
=========
        """,
        r"""
   +---+
   |   |
   O   |
       |
       |
       |
=========
        """,
        r"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
        """,
        r"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
        """,
        r"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
        """,
        r"""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
        """,
        r"""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
        """
    ]
    return wisielce[min(bledy, len(wisielce) - 1)]


def main():
    print("🎮 === WISIELEC PREMIUM === 🎮")
    print("🚀 Wersja z kategoriami i poziomami trudności!")

    # Wybór kategorii i poziomu
    kategoria = wyswietl_menu_kategorii()
    poziom = wyswietl_menu_poziomu()

    # Konfiguracja gry
    slowo = wybierz_slowo(kategoria, poziom)
    poziom_info = POZIOMY[poziom]

    odgadniete = set()
    bledy_litery = set()
    bledy = 0
    max_bledow = poziom_info['max_błędów']
    pozostałe_podpowiedzi = poziom_info['podpowiedzi']

    start_time = time.time()

    # Informacje o grze
    print(f"\n🎯 Kategoria: {kategoria}")
    print(f"⚡ Poziom: {poziom}")
    print(f"📝 Słowo ma {len(slowo)} liter")
    print(f"💥 Maksymalnie {max_bledow} błędów")
    print(f"💡 Dostępne podpowiedzi: {pozostałe_podpowiedzi}")

    while bledy < max_bledow:
        print(wyswietl_wisielca(bledy))

        stan = wyswietl_stan(slowo, odgadniete)
        print(f"\n📖 Słowo: {stan}")
        print(f"💥 Błędy: {bledy}/{max_bledow}")

        if odgadniete:
            print(f"✅ Trafione: {sorted(list(odgadniete))}")
        if bledy_litery:
            print(f"❌ Błędne: {sorted(list(bledy_litery))}")

        # Sprawdź wygraną
        if all(litera in odgadniete for litera in slowo):
            czas_gry = int(time.time() - start_time)
            print(wyswietl_wisielca(bledy))
            print(f"\n🎉 BRAWO! Odgadłeś słowo: {slowo}")
            print(f"🏆 Kategoria: {kategoria}")
            print(f"⚡ Poziom: {poziom}")
            print(f"💥 Błędy: {bledy}/{max_bledow}")
            print(f"⏱️ Czas: {czas_gry} sekund")

            # Ocena wyników
            if bledy == 0:
                print("🌟 PERFEKCYJNA GRA!")
            elif bledy <= max_bledow // 3:
                print("🔥 ŚWIETNY WYNIK!")
            elif bledy <= max_bledow // 2:
                print("👍 DOBRA ROBOTA!")
            else:
                print("😅 UDAŁO SIĘ!")
            break

        # Menu podczas gry - UPROSZCZONA WERSJA
        if pozostałe_podpowiedzi > 0:
            print(f"\n💡 Dostępne komendy:")
            print(f"   PODPOWIEDŹ - użyj podpowiedzi ({pozostałe_podpowiedzi} pozostało)")
            print(f"   PODDAJĘ - poddaj się")
            print(f"   lub podaj literę bezpośrednio")
        else:
            print(f"\n💡 PODDAJĘ - aby się poddać, lub podaj literę")

        # Pobierz input
        user_input = input("🎯 Twój ruch: ").upper().strip()

        # Sprawdź komendy specjalne
        if user_input == "PODPOWIEDŹ" and pozostałe_podpowiedzi > 0:
            odgadniete, pozostałe_podpowiedzi = użyj_podpowiedzi(slowo, odgadniete, pozostałe_podpowiedzi)
            continue
        elif user_input == "PODDAJĘ":
            print(f"🏳️ Poddajesz się! Słowo to: {slowo}")
            break
        elif user_input == "PODPOWIEDŹ" and pozostałe_podpowiedzi == 0:
            print("❌ Brak dostępnych podpowiedzi!")
            continue

        # Traktuj jako literę
        litera = user_input

        # Walidacja
        if len(litera) != 1:
            print("❌ Podaj tylko JEDNĄ literę!")
            continue

        if not litera.isalpha():
            print("❌ Podaj literę, nie cyfrę!")
            continue

        if litera in odgadniete or litera in bledy_litery:
            print(f"❌ Litera '{litera}' już była sprawdzana!")
            continue

        # Sprawdź literę
        if litera in slowo:
            odgadniete.add(litera)
            ile_razy = slowo.count(litera)
            if ile_razy == 1:
                print(f"✅ Brawo! Litera '{litera}' jest w słowie!")
            else:
                print(f"✅ Świetnie! Litera '{litera}' występuje {ile_razy} razy!")
        else:
            bledy += 1
            bledy_litery.add(litera)
            print(f"❌ Ups! Litery '{litera}' nie ma w słowie.")
            if bledy < max_bledow:
                print(f"⚠️  Pozostało prób: {max_bledow - bledy}")

        print("-" * 60)

    # Przegrana
    if bledy == max_bledow:
        print(wyswietl_wisielca(bledy))
        print(f"\n💀 PRZEGRANA! Słowo to: {slowo}")
        print(f"🎯 Kategoria: {kategoria}")
        print(f"⚡ Poziom: {poziom}")
        print("🔄 Spróbuj ponownie na łatwiejszym poziomie!")


if __name__ == "__main__":
    main()
