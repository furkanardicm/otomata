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

def durumKontrol(oldStates, afters, outputs, girdi):
    eskiDurum = oldStates[0]
    state = ["q0"]
    cikti = list()
    i = 0
    while i < len(girdi[0]):
        j = 0
        while j < len(oldStates):
            if eskiDurum ==  oldStates[j]:
                alfabe = 0
                while alfabe < len(girdi[2]):
                    if girdi[0][i] == girdi[2][alfabe]:
                        eskiDurum = afters[alfabe][j]
                        state.append(afters[alfabe][j])
                        cikti.append(outputs[alfabe][j])    
                        break
                    alfabe += 1
                break
            j += 1
            
        i += 1

    yazdir(cikti, girdi[0], state)
                
def main():
    dosya = open("GECISTABLOSU.txt")
    satirSayisi = len(dosya.readlines()) - 1
    dosya.close()
    satirListesi = list()
    
    afters, outputs, states = list(), list(), list()
    girdi = ["","","",""]
    
    dosya = open("GECISTABLOSU.txt")
    dosya.readline()
    i = 0
    while i < satirSayisi:
        satirListesi.append(dosya.readline())
        i += 1

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
            eklemeMiktari += 8
            i += 1
        j += 1   

    # States ------------------------------------------------

    i = 0
    while i < len(girdi[1]):
        states.append(girdi[1][i])
        i += 1

    # Outputs ------------------------------------------------

    i = 0
    while i < len(girdi[2]):
        outputs.append(list())
        i += 1


    i = 0
    eklemeMiktari = 0
    while i < len(girdi[2]):
        j = 0
        while j < satirSayisi - 1:
            outputs[i].append(satirListesi[j + 1][8 + eklemeMiktari: 9 + eklemeMiktari])
            j += 1
        eklemeMiktari += 8
        i += 1    

    durumKontrol(states, afters, outputs, girdi)
    print(outputs)
    
if __name__ == "__main__":
    main()