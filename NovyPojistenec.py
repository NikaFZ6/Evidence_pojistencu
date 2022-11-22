class NovyPojistenec:
# třída reprezentující výpis informací o pojistenci

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefonni_cislo = telefonni_cislo

    def __str__(self):
        # Metoda pro výpis pojistence
        return f"\n{self.jmeno} " + f"\t" + f"{self.prijmeni} " + f"\t" + f"{self.vek} " + f"\t" + f"{self.telefonni_cislo}"
