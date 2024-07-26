girdi = list()

def benimFonk(i, girdi, sonuc):
    for a in range(0, 3):
        girdi[i] = "?"
        girdi.remove("?")
    
    girdi.insert(i, sonuc)

def main():
    girdi = input("Lutfen metni giriniz : ").split(" ")
    sonuc = 0
    print(girdi)
    for i in girdi:
        if i.find(".") > 0:
            girdi[girdi.index(i)] = float(i)      
        elif i.isdigit():
            girdi[girdi.index(i)] = int(i)      
    i = len(girdi) - 3
    while i >= 0:
        if girdi[i] == "/":
            sonuc += girdi[i + 1] / girdi[i + 2]
            benimFonk(i, girdi, sonuc)
        elif girdi[i] == "*":
            sonuc += girdi[i + 1] * girdi[i + 2]
            benimFonk(i, girdi, sonuc) 
        elif girdi[i] == "-":
            sonuc += girdi[i + 1] - girdi[i + 2]
            benimFonk(i, girdi, sonuc)
        elif girdi[i] == "+":
            sonuc += girdi[i + 1] + girdi[i + 2]
            benimFonk(i, girdi, sonuc)
        sonuc = 0
        i -= 1
    sonuc = girdi[0]
    print(sonuc)

if __name__ == "__main__":
    main()