from datetime import datetime

class Pranesimas:
    id_counter = 1
    def __init__(self, pranesimo_tekstas, autorius):
        self.id = Pranesimas.id_counter
        Pranesimas.id_counter += 1
        self.pranesimo_tekstas = pranesimo_tekstas
        self.autorius = autorius
        self.publikavimo_data = datetime.now()


    def pakeisti_autoriaus_varda(self, naujas_autorius,):
       self.autorius = naujas_autorius

    def rodyti_informacija(self):
        print(f'Pranesimo tekstas: {self.pranesimo_tekstas}')
        print(f'Autorius: {self.autorius}')
        print(f'Publikavimo_data: {self.publikavimo_data.strftime("%Y/%m/%d %H:%M")}')


class Komentaras(Pranesimas):
    def __init__(self, pranesimo_tekstas, autorius, pranesimo_id):
        super().__init__(pranesimo_tekstas, autorius)
        self.pranesimo_id = pranesimo_id
        self.balsai = 0

    def balsuoti(self, balsas):
        self.balsai += balsas


    def rodyti_informacija(self):
        super().rodyti_informacija()
        print(f'Komentaro tekstas: {self.pranesimo_tekstas}')
        print(f'Pranesimo ID: {self.pranesimo_id}')
        print(f'Balsai: {self.balsai}')


class Blogas:
    def __init__(self):
        self.pranesimu_sarasas = []

    def prideti_pranesima_i_sarasa(self, pranesimas):
        self.pranesimu_sarasas.append(pranesimas)

    def rodyti_visus_pranesimus(self, zodis):
        rasti_pranesimai = []
        for pranesimas in self.pranesimu_sarasas:
            if zodis in pranesimas.pranesimo_tekstas:
                rasti_pranesimai.append(pranesimas)
        if not rasti_pranesimai:
            print("Pranesimu su nurodytu zodziu nerasta.")
        else:
            for pranesimas in rasti_pranesimai:
                print(pranesimas.rodyti_informacija())


    def istrinti_pranesima_pagal_pranesimo_id(self, id):
        for i, pranesimas in enumerate(self.pranesimu_sarasas):
            if pranesimas.id == id :
                self.pranesimu_sarasas.pop(i)
                return
        print("Pranesimas su nurodytu ID nerastas")


class PranesimuValdymas:
    def __init__(self):
        self.pranesimai = []
        self.komentarai = []

    def prideti_pranesima(self, pranesimas, autorius):
        self.pranesimai.append(Pranesimas(pranesimas, autorius))

    def prideti_komentara(self, komentaras, autorius, pranesimo_id):
        self.komentarai.append(Komentaras(komentaras, autorius, pranesimo_id))

    def rodyti_pranesimus(self):
        for pranesimas in self.pranesimai:
            pranesimas.rodyti_informacija()
            print('\n---\n')

    def rodyti_komentarus(self, pranesimo_id):
        for komentaras in self.komentarai:
            if komentaras.pranesimo_id == pranesimo_id:
                komentaras.rodyti_informacija()
                print('\n---\n')

    def balsuoti_uz_komentara(self, komentaro_id, balsas):
        for komentaras in self.komentarai:
            if komentaras.id == komentaro_id:
                komentaras.balsuoti(balsas)
                break


def main():
    valdymas = PranesimuValdymas()
    while True:
        print('\n1. Prideti pranesima')
        print('2. Prideti komentara')
        print('3. Rodyti pranesimus')
        print('4. Balsuoti uz komentara')
        print('5. Rodyti komentarus')
        print('6. Iseiti')
        veiksmas = input('Pasirinkite veiksma -->')
        if veiksmas == '1':
            tekstas = input('Iveskite pranesimo teksta --> ')
            autorius = input('Iveskite autoriaus varda --> ')
            valdymas.prideti_pranesima(tekstas, autorius)
        elif veiksmas == '2':
            tekstas = input('Iveskite komentaro teksta --> ')
            autorius = input('Iveskite autoriaus varda --> ')
            pranesimo_id = int(input('Iveskite pranesimo ID --> '))
            valdymas.prideti_komentara(tekstas, autorius, pranesimo_id)
        elif veiksmas == '3':
            valdymas.rodyti_pranesimus()
        elif veiksmas == '4':
            komentaro_id = input('Iveskite komentaro ID --> ')
            balsas = input('Balsuoti uz +1, balsuoti pries -1, \niveskite balsa -->')
            valdymas.balsuoti_uz_komentara(komentaro_id, balsas)
        elif veiksmas == '5':
            pranesimo_id = int(input('Iveskite pranesimo ID --> '))
            valdymas.rodyti_komentarus(pranesimo_id)
        elif veiksmas == '6':
            break
        else:
            print('Neteisingas pasirinkimas, bandykite dar karta..')

if __name__ == '__main__':
    main()





