def yazdir(cikti, girdi, state):
    print("Input String   ", end = " ")
    for i in girdi:
        print(i, end = "  ")

    print("\nState\t    ", end = " ")
    for i in state:
        print(i, end = " ")

    print("\nOutput\t    ", end = " ")
    for i in cikti:
        print(i, end = "  ")    

    print("\n---------------------------")

def durumKontrol(oldStates, afters, output, girdi):
    eskiDurum = oldStates[0]
    state = ["q0"]
    cikti = list()
    i = 0
    while i < len(girdi[0]):
        j = 0
        while j < len(output):
            if eskiDurum ==  oldStates[j]:
                alfabe = 0
                while alfabe < len(girdi[2]):
                    if girdi[0][i] == girdi[2][alfabe]:
                        eskiDurum = afters[alfabe][j]
                        state.append(afters[alfabe][j])
                        cikti.append(output[j])    
                        break
                    alfabe += 1
                break
            j += 1
            
        i += 1

    cikti.append(output[0])

    yazdir(cikti, girdi[0], state)
                
def main():
    dosya = open("GECISTABLOSU.txt")
    satirSayisi = len(dosya.readlines())
    dosya.close()
    satirListesi = list()
    
    afters, output, states = list(), list(), list()
    girdi = ["","","",""]
    
    dosya = open("GECISTABLOSU.txt")

    i = 0
    while i < satirSayisi:
        satirListesi.append(dosya.readline())
        i += 1

    print(satirListesi)

    dosya.close()

    # Input ------------------------------------------------

    dosya = open("INPUT.txt")

    girdi[0] = [*dosya.readline()[:-1]]
    girdi[1] = dosya.readline()[3:-1].split(",")
    girdi[2] = dosya.readline()[3:-1].split(",")
    girdi[3] = dosya.readline()[3:-1].split(",")

    print("---------------------------\nGirdiler : ")
    for i in girdi:
        print(i)
    print("---------------------------")
    
    # Afters ----------------------------------------------

    i = 0
    while i < len(girdi[2]):
        afters.append(list())
        i += 1

    j = 1    
    while j < satirSayisi:
        eklemeMiktari = 0
        i = 0
        while i < len(girdi[2]):    
            afters[i].append(satirListesi[j][4 + eklemeMiktari: 6 + eklemeMiktari])
            eklemeMiktari += 4
            i += 1
        j += 1   

    # States ------------------------------------------------

    i = 1
    while i < satirSayisi:
        states.append(satirListesi[i][0:2])
        i += 1

    # Output ------------------------------------------------

    dosya = open("OUTPUT.txt")

    outputListesiGecici = dosya.readlines()

    for i in range(1, len(outputListesiGecici)):
        output.append(outputListesiGecici[i][0])

    dosya.close()

    durumKontrol(states, afters, output, girdi)

if __name__ == "__main__":
    main()