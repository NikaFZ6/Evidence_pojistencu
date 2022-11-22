from NovyPojistenec import NovyPojistenec
# import třídy obsahujících použité metody

class Akce:
# Třídad reprezentující "hlavičku" aplikace


    def vyber_akci(self):
        # metoda pro vykreslení úvodního textu
        self.__vycisti_obrazovku()
        print("\n---------------------------------")
        print("Evidence pojištěnců")
        print("---------------------------------")
        print("\nMOZNE AKCE: ")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vypsat všechny pojištěnce")
        print("3 - Vyhledej pojištěnce")
        print("4 - Konec")


    def __vycisti_obrazovku(self):
        #Vymaže obrazovku konzole. Nemůžu zjistit, proč nefunguje :-/
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])



class Vstup:
# Třída reprezentuje zadání údajů o novém pojištěnci

    def __init__(self):
        pass

    def vypln_udaje(self):
        self.jmeno = input("\nZadejte jméno nového pojištěnce: \n")
        self.prijmeni = input("Zadejte příjmení nového pojištěnce: \n")


        self.vek = int(input("Zadejte věk nového pojištěnce: \n"))
        while (self.vek < 0 or self.vek > 99):
            print("Zadali jste neplatnou hodnotu.\n")
            self.vek = int(input("Zadejte věk nového pojištěnce: \n"))
        else:
            pass


        self.telefonni_cislo = str(input("Zadejte telefonní číslo nového pojištěnce: \n"))
        while (len(self.telefonni_cislo) < 9 or len(self.telefonni_cislo) > 9):
            print("Zadali jste neplatnou hodnotu.\n")
            self.telefonni_cislo = str(input("Zadejte telefonní číslo nového pojištěnce: \n"))
        else:
            pass

        pojistenec = NovyPojistenec(self.jmeno, self.prijmeni, self.vek, self.telefonni_cislo)
        return pojistenec

