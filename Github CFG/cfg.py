temelKelimeler, anaListe, xIcerenIfade, kelimeler, degiskenler, boyut, toplam = list(), list(), list(), list(), list(), int(), int()

def degiskenKontrol(kelime):
    sayac = 0
    for i in degiskenler:
        if i in kelime:
            sayac += 2
        
    return int(sayac)

def girdiAl():
    geciciListe = input("Kelimeleri giriniz (S-->aa|aX|aXX,X-->b|ab) : ").split(",")
    
    for i in range(1, len(geciciListe)):
        temelKelimeler.append(geciciListe[i].split("-->")[1].split("|"))

    for i in range(1, len(geciciListe)):
        degiskenler.append(geciciListe[i].split("-->")[0])

    for i in degiskenler:
        xIcerenIfade.append(list())

    for i in geciciListe[0].split("-->")[1].split("|"):
        kelimeler.append(i)
        sayi = degiskenKontrol(i) - 1
        toplam = sayi
        if sayi == 1:
            xParcala(i)  
        elif sayi > 1:
            for g in [*i]:
                if g.isupper():
                    ilkHarf = g
                    break
            copyOfWord = i
            for a in temelKelimeler[degiskenler.index(ilkHarf)]:
                i = i.replace(ilkHarf, a)
                xIcerenIfade[degiskenler.index(ilkHarf)].append(i)
                xIcerenIfade[degiskenler.index(ilkHarf)].append(i)
                xIcerenIfade[degiskenler.index(ilkHarf) + 1].append(i)
                xIcerenIfade[degiskenler.index(ilkHarf) + 1].append(i)
                i = copyOfWord

        else:
            anaListe.append(i)

def islem(kelime):
    for h in degiskenler:
        kelimeKopya = kelime
        if kelime.find(h) != -1:
            for i in temelKelimeler[degiskenler.index(h)]:
                kelime = kelime.replace(h, i)
                anaListe.append(kelime)
                kelime = kelimeKopya

def xParcala(i):
    if i.count("X") > 1 or i.count("Y") > 1 or i.count("Z") > 1: 
        for a in range(0, len(temelKelimeler)):
            for b in range(0, len(temelKelimeler[a])):
                geciciListe = [*i]
                index = i.index(degiskenler[a])
                geciciListe[index] = temelKelimeler[a][b]
                geciciListe = "".join(geciciListe)
                if geciciListe.count(degiskenler[a]) > 0:
                    geriDonus = xParcala(geciciListe)
                    xIcerenIfade[degiskenler.index(degiskenler[a])].append(geriDonus)
                else:
                    xIcerenIfade[degiskenler.index(degiskenler[a])].append(geciciListe)
    else:
        for j in degiskenler:
            if j in i:
                xIcerenIfade[degiskenler.index(j)].append(i)
                return i            

def main():
    girdiAl()
    boyut = int(input("Gormek istediginiz son kelime kac harfli olsun : ")) 

    sonluListe = list()
    for i in range(0, len(xIcerenIfade)):
        for j in xIcerenIfade[i]:
            kelime1 = j
            for h in degiskenler:
                if kelime1.find(h) != -1:
                    kelimeCopy = kelime1
                    for i in temelKelimeler[degiskenler.index(h)]:
                        kelime1 = kelime1.replace(h, i)
                        sonluListe.append(kelime1)
                        kelime1 = kelimeCopy
                
    for i in range(0, len(xIcerenIfade)):
        for j in xIcerenIfade[i]:
            yeniKelime = j
            for f in range(0, boyut):
                islem(yeniKelime)
                yeniKelime = yeniKelime.replace(degiskenler[i], xIcerenIfade[i][xIcerenIfade[i].index(j)])

    i = 0
    while i < len(anaListe):
        if len(anaListe[i]) > boyut:
            anaListe.remove(anaListe[i])  
            i -= 1
        i += 1    

    tekrarEden = list()
    for i in anaListe:
        if anaListe.count(i) > 1:
            tekrarEden.append(i)

    sonluTekrarEden = list()
    for i in sonluListe:
        if sonluListe.count(i) > 1:
            sonluTekrarEden.append(i)

    yeniListe = list(set(anaListe))
    print("X-Y iceren ifadeler : ", xIcerenIfade)
    print("-----------------\nAna Liste Elemanlari : ", list(sorted(yeniListe, key = len)))
    print("-----------------\nTekrar Eden Elemanlar : ", list(sorted(list(set(tekrarEden)), key = len)))
    print("-----------------\nSonlu Liste : ", list(sorted(list(set(sonluListe)), key = len)))
    print("-----------------\nSonlu Tekrar Eden Elemanlar : ", list(sorted(list(set(sonluTekrarEden)), key = len)))
    print("\n\n")

if __name__ == "__main__":
    main()