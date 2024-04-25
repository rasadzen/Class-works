import csv

class Preke:
    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def info(self):
        return f'{self.pavadinimas}, Kaina: {self.kaina}Eur'


class Patiekalas(Preke):
    def __init__(self, pavadinimas, kaina, paruosimo_laikas):
        super().__init__(pavadinimas, kaina)
        self.paruosimo_laikas = paruosimo_laikas

    def info(self):
        return f'{super().info()}, Paruosimo laikas: {self.paruosimo_laikas}min'


class Gerimas(Preke):
    def __init__(self, pavadinimas, kaina, turis):
        super().__init__(pavadinimas, kaina)
        self.turis = turis

    def info(self):
        return f'{super().info()}, Turis: {self.turis}ml'


class Uzsakymas:
    def __init__(self):
        self.prekes = []

    def prideti_preke(self, preke):
        self.prekes.append(preke)

    def apskaiciuoti_suma(self):
        return sum(preke.kaina for preke in self.prekes)

    def uzsakymo_info(self):
        for preke in self.prekes:
            print(preke.info())
        print(f'Bendra suma: {self.apskaiciuoti_suma():.2f} Eur')


class Restoranas:
    def __init__(self):
        self.uzsakymai = []
        self.uzsakymo_id = 0

    def prideti_uzsakyma(self, uzsakymas):
        self.uzsakymo_id += 1
        self.uzsakymai.append((self.uzsakymo_id, uzsakymas, 'Priimtas'))
        print(f'Uzsakymo ID: {self.uzsakymo_id} priimtas!')

    def atnaujinti_busena(self, uzsakymo_id, busena):
        for uzsakymas in self.uzsakymai:
            if uzsakymas[0] == uzsakymo_id:
                self.uzsakymai[self.uzsakymai.index(uzsakymas)] = (uzsakymo_id, uzsakymas[1], busena)
                print(f"Uzsakymo ID: {uzsakymo_id} busena atnaujinta i {busena} ")
                break

    def apskaiciuoti_saskaita(self, uzsakymo_id):
        for uzsakymas in self.uzsakymai:
            if uzsakymas[0] == uzsakymo_id:
                suma = uzsakymas[1].apskaiciuoti_suma()
                print(f"Uzsakymo ID: {uzsakymo_id} Saskaita: {suma:.2f} Eur")
                break

    def rodyti_uzsakymus(self):
        if not self.uzsakymai:
            print("Siuo metu uzsakymu nera!")
            return
        for uzsakymas in self.uzsakymai:
            print(f"Uzsakymo ID: {uzsakymas[0]}, busena: {uzsakymas[2]}")
            uzsakymas[1].uzsakymo_info()
            print('=' * 40)

    def issaugoti_uzsakymus_csv(self, failo_pavadinimas):
        with open(failo_pavadinimas, mode='w', newline='', encoding='utf-8') as failas:
            writer = csv.writer(failas)
            writer.writerow(["Uzsakymo ID", "Prekes pavadinimas", "Kaina", "Busena", "Paruosimo laikas", "Turis"])
            for uzsakymas in self.uzsakymai:
                for preke in uzsakymas[1].prekes:
                    paruosimo_laikas = preke.paruosimo_laikas if hasattr(preke, 'paruosimo_laikas') else ""
                    turis = preke.turis if hasattr(preke, 'turis') else ""
                    writer.writerow(
                        [uzsakymas[0], preke.pavadinimas, preke.kaina, uzsakymas[2], paruosimo_laikas, turis])

    def ikelimas_is_csv(self, failo_pavadinimas):
        with open(failo_pavadinimas, mode='r', newline='', encoding='utf-8') as failas:
            reader = csv.DictReader(failas)
            laikini_uzsakymai = {}
            for eilute in reader:
                uzsakymo_id = int(eilute['Uzsakymo ID'])
                pavadinimas = eilute['Prekes pavadinimas']
                kaina = float(eilute['Kaina'])
                busena = eilute['Busena']
                paruosimo_laikas = eilute.get('Paruosimo laikas', "")
                turis = eilute.get('Turis', "")

                if paruosimo_laikas:
                    preke = Patiekalas(pavadinimas, kaina, int(paruosimo_laikas) if paruosimo_laikas.isdigit() else 0)
                elif turis:
                    preke = Gerimas(pavadinimas, kaina, int(turis) if turis.isdigit() else 0)
                else:
                    preke = Preke(pavadinimas, kaina)

                if uzsakymo_id not in laikini_uzsakymai:
                    laikini_uzsakymai[uzsakymo_id] = Uzsakymas()
                laikini_uzsakymai[uzsakymo_id].prideti_preke(preke)

                self.atnaujinti_busena(uzsakymo_id, busena)
            for uzsakymo_id in laikini_uzsakymai:
                self.prideti_uzsakyma(laikini_uzsakymai[uzsakymo_id])


class Meniu:
    def __init__(self):
        self.patiekalai = []
        self.gerimai = []

    def prideti_patiekala(self, patiekalas):
        self.patiekalai.append(patiekalas)

    def prideti_gerimai(self, gerimas):
        self.gerimai.append(gerimas)

    def rodyti_meniu(self):
        print("Patiekalai:")
        for patiekalas in self.patiekalai:
            print(patiekalas.info())
        print("\nGerimai:")
        for gerimas in self.gerimai:
            print(gerimas.info())

    def rasti_patiekala(self, pavadinimas):
        for patiekalas in self.patiekalai:
            if patiekalas.pavadinimas.lower() == pavadinimas.lower():
                return patiekalas
        return None

    def rasti_gerima(self, pavadinimas):
        for gerimas in self.gerimai:
            if gerimas.pavadinimas.lower() == pavadinimas.lower():
                return gerimas
        return None


# sukuriam restorano objekta
restoranas = Restoranas()
restorano_meniu = Meniu()
# sukuriame keleta prekiu ir uzsakyma
pica = Patiekalas('Margarita', 11.99, 20)
limonadas = Gerimas('Fanta', 1.99, 500)

restorano_meniu.prideti_patiekala(pica)
restorano_meniu.prideti_gerimai(limonadas)
restorano_meniu.rodyti_meniu()

# atnaujiname busena
restoranas.atnaujinti_busena(1, 'Paruostas')
# apskaiciuojame saskaita
restoranas.apskaiciuoti_saskaita(1)
# rodome visus uzsakymus
restoranas.ikelimas_is_csv('uzsakymai.csv')
restoranas.rodyti_uzsakymus()
restoranas.issaugoti_uzsakymus_csv('uzsakymai.csv')