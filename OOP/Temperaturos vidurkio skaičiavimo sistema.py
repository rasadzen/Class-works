def prideti_temperatura(temperaturos, miestas, miesto_temperatura):
    if miestas in temperaturos:
        temperaturos[miestas].append(miesto_temperatura)
    else:
        temperaturos[miestas] = [miesto_temperatura]

def skaiciuoti_vidurki(temperaturos, miestas):
    if miestas in temperaturos and len(temperaturos[miestas]) > 0:  #skaiciuoja jeigu daugiau nei 0 reiksmiu
        return sum(temperaturos[miestas])/len(temperaturos[miestas])
    else:
        return None

def main():
    temperaturos = {}

    while True:
        veiksmas = int(input("Pasirinkite veiksma: \n1 Pridėti temperatūrą mieste / jei miesto nėra - pridėti miestą ir temperatūrą\n2 Rodyti temperatūros vidurkį mieste\n3 Uždaryti programą.\n--> "))
        if veiksmas == 1:
            miestas = input("Pasirinkite miestą-> ").capitalize()
            try:
                miesto_temperatura = float(input("Įveskite temperatūrą mieste -> "))
                prideti_temperatura(temperaturos, miestas, miesto_temperatura)
                print(f"Temperatūra {miesto_temperatura}℃ sėkimngai pridėta prie {miestas}! ")
            except ValueError:
                print("Klaida: Temperatūra turi būti skaičius!")
                return
        elif veiksmas == 2:
            miestas = input("Įveskite miestą kurio vidutinę temperatūrą norite matyti -> ")
            vidutine_temperatura = skaiciuoti_vidurki(temperaturos, miestas)
            if vidutine_temperatura is not None:
                print(f"{miestas} vidutinė temperatūra yra {vidutine_temperatura:.1f}℃ laipsniai.")
            else:
                print(f"Nėra duomenų apie {miestas} temperatūrą.")

        elif veiksmas == 3:
            print("Programa uždaroma..")
            break
        else:
            print("Klaida:\nNeteisingas pasirinkimas.")

if __name__ == "__main__":
    main()

