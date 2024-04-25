class Studentas:
    def __init__(self, vardas, pavarde, studiju_programa):
        self.vardas = vardas
        self.pavarde = pavarde
        self.studiju_programa = studiju_programa
    def __str__(self):
        return f'{self.vardas} {self.pavarde} {self.studiju_programa}'

class StudentuValdymoSistema:
    def __init__(self):
        self.studentai = []

    def prideti_studenta(self, studentas):
        self.studentai.append(studentas)
        print(f"Studentas {studentas} pridetas studentas!")

    def salinti_studenta(self, vardas, pavarde):
        for studentas in self.studentai:
            if studentas.vardas == vardas and studentas.pavarde == pavarde:
                self.studentai.remove(studentas)
                print(f"Sudentas {vardas} {pavarde} pasalintas sekmingai")
                return
        print("Studentas nerastas")

    def atnaujinti_studento_info(self, vardas, pavarde, nauja_programa):
        for studentas in self.studentai:
            if studentas.vardas == vardas and studentas.pavarde == pavarde:
                studentas.studiju_programa = nauja_programa
                print(f'Studento {vardas} {pavarde} informacija atnaujinta sekmingai!')
                return
            print("Studentas nerastas")

    def rodyti_visus_studentus(self):
        if not self.studentai:
            print("Studentu sarasas tuscias")
            return
        for studentas in self.studentai:
            print(studentas)

sistema = StudentuValdymoSistema()

studentas1 = Studentas("Antanas", "Antanaitis", "Biologija")
studentas2 = Studentas("Ona", "Onaitiene", "Matematika")
sistema.prideti_studenta(studentas1)
sistema.prideti_studenta(studentas2)

print("\n Visi studentai:")
sistema.rodyti_visus_studentus()
print('----------------------')

sistema.atnaujinti_studento_info("Antanas", "Antanaitis", "Programos sistemu inzinerija")
print("\nVisi studentai po atnaujinimo:")
sistema.rodyti_visus_studentus()
sistema.salinti_studenta("Antanas", "Antanaitis")

print("----------------------")
print("\nGalutinis studentu sarasas:")
sistema.rodyti_visus_studentus()

