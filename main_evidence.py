from Metody import Akce
from Metody import Vstup
from NovyPojistenec import NovyPojistenec
# import tříd obsahujících použité metody


akce = Akce()
akce.vyber_akci()
# volání metody pro vypsání úvodního textu "MOZNE AKCE"


seznam_pojistencu = []
# prázdný seznam pojištěnců

seznam_pojistencu.append(NovyPojistenec("Adam", "Novák", 21, 724234567))
seznam_pojistencu.append(NovyPojistenec("Petr", "Růžek", 57, 777234567))
seznam_pojistencu.append(NovyPojistenec("Libor", "Brbla", 42, 605234567))
# naplnění seznamu


pokracovat = True
while pokracovat == True:
    # "tělo" aplikace

    akce = input("\nVyberte akci:\n")


    if akce == "1":
    # přidání nového pojištěnce do seznamu
        vstup = Vstup()
        pojistenec = vstup.vypln_udaje()
        print(pojistenec, "\n")
        seznam_pojistencu.append(pojistenec)
        input("\nData byla uložena. Pokračujte libovolnou klávesou...")
        akce = Akce()
        akce.vyber_akci()


    elif akce == "2":
    # výpis všech pojištěnců v seznamu
        for pojistenec in seznam_pojistencu:
            print(pojistenec)
        input("\nPokračujte libovolnou klávesou...")
        akce = Akce()
        akce.vyber_akci()


    elif akce == "3":
    # vyhledání pojištěnce v existujícím seznamu
        hledane_jmeno = input("Zadejte jméno pojistence: \n")
        hledane_prijmeni = input("Zadejte příjmení: \n")
        for pojistenec in seznam_pojistencu:
            if hledane_jmeno == pojistenec.jmeno and hledane_prijmeni == pojistenec.prijmeni:
                print(pojistenec)
        input("\nPokračujte libovolnou klávesou...")
        akce = Akce()
        akce.vyber_akci()


    elif akce == "4":
    # volba pro ukončení aplikace
        print("Program byl ukončen.")
        break


    elif akce != "1" or "2" or "3" or "4":
    # ošetření chybného zadání čísla akce
        print("Neplatná volba!")
        input("\nPokračujte libovolnou klávesou...")
        akce = Akce()
        akce.vyber_akci()

else:
    pass


