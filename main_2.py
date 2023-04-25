from clovek import Pojisteny
pojisteny = Pojisteny
pojisteni = []

def pridat_pojisteneho():
    jmeno = input("Zadej jméno:\n ")
    prijmeni = input("Zadej příjmení:\n ")
    vek = input("Zadej věk:\n ")
    telefon = input("Zadej telefon:\n ")
    pojisteni.append({"jmeno": jmeno, "prijmeni": prijmeni, "vek": vek, "telefon": telefon})
    print("Nový pojištěný byl přidán.")


def vypsat_pojistene():
    print("Seznam všech pojištěných:")
    for p in pojisteni:
        print(p["jmeno"], p["prijmeni"], p["vek"], p["telefon"])



def najit_pojisteneho():
    jmeno = input("Zadej jméno pojištěného:\n ")
    prijmeni = input("Zadej příjmení pojištěného:\n ")
    nalezeno = False
    for p in pojisteni:
        if p["jmeno"] == jmeno and p["prijmeni"] == prijmeni:
            nalezeno = True
            print(p["jmeno"], p["prijmeni"], p["vek"], p["telefon"])
    if not nalezeno:
        print("Pojištěný s tímto jménem a příjmením nebyl nalezen.")


def main():
    print("=====Vítejte v aplikaci pro evidenci pojištěných!=====\n")
    while True:
        print("Vyberte akci:\n")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        volba = input("Pokračujte dalším výběrem...\n")
        if volba == "1":
            pridat_pojisteneho()
        elif volba == "2":
            vypsat_pojistene()
        elif volba == "3":
            najit_pojisteneho()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")
main()