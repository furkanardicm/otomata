# girilen ifade eğer hiç yıldız içermiyorsa ( örneğin "a+b" ) yazdırmaSayisi adli değişkene maximum yazdırabileceği sayı girilmelidir 
# Mevcut örnek için bu işlem şu şekildedir. a+b nin yazdıracağı kelime sayisi 1 tanedir, bu nedenle yazdirmaSayacina maximum 1 değeri yazilmalidir 
# Çıktı uzun döngüden kaynaklı geç gelebiliyor 




import random

    # YAZDIR -----------------------------------------------------------------------------------------------------------------------------------------------
    
def yazdir(gelenListe, yazdirmaSayisi):
    kelimem = list()
    kelimem.extend(gelenListe)
    kelimem.append("|")
    sonListem = list()
    for i in range(0, len(kelimem)):
        geciciIndex = i + 1
        if kelimem[i] == "|":
            break

        if kelimem[i].isdigit() and kelimem[i - 1].isalpha():
            sayac = 0
                    
            while sayac < randomDegerUret(yazdirmaSayisi):
                sonListem.append(kelimem[i - 1])
                sayac += 1
        
        elif i != len(kelimem) - 1 and kelimem[i+1].isdigit() and kelimem[i] != "0":
            sayac3 = 0

            while sayac3 < randomDegerUret(yazdirmaSayisi):
                sonListem.append(kelimem[i])
                sayac3 += 1

        elif kelimem[i] != "0" and i != len(kelimem) - 1:
            sonListem.append(kelimem[i])

        else:
            sonListem = kelimem[:len(kelimem) - 1]

    return kelimeYap(sonListem)        

    # RANDOM DEĞER ÜRET ------------------------------------------------------------------------------------------------------------------------------------

def randomDegerUret(elemanSayisi):
    x = random.randint(0, elemanSayisi - 1)
    return x

def randomDegerUret2(sayi1, elemanSayisi):
    x = random.randint(sayi1, elemanSayisi - 1)
    return x

    # TOPLAM FONKSİYONU ------------------------------------------------------------------------------------------------------------------------------------

def toplamFonksiyonu(anaListe):
    for i in range(0, len(anaListe)):

        if type(anaListe[i]) is list:
            anaListe[i] = "".join(toplamFonksiyonu(anaListe[i]))
    
        elif anaListe[i] == "+":
            cokluSecim = kelimeYap(anaListe)
            if cokluSecim.count("+") > 1 and cokluSecim.find("(") == -1:
                gecici = cokluSecim.split("+")
                bos = gecici[randomDegerUret(len(gecici))]
                anaListe = bos
                return anaListe

            anaListe[i] = "?"
            gecici = kelimeYap(anaListe).split("?")
            bos = gecici[randomDegerUret(len(gecici))]

            if kelimeYap(bos).find("(") != -1:
                anaListe = parantezleriYerlestir(bos, [*bos])

                for index in range(0, len(anaListe)):
                    if type(anaListe[index]) is list:
                        anaListe[index] = "".join(toplamFonksiyonu(anaListe[index]))

                return toplamFonksiyonu(anaListe)

            else:
                anaListe = bos
                return anaListe
    
    return anaListe

    # PARANTEZLERİ YERLEŞTİR -------------------------------------------------------------------------------------------------------------------------------

def parantezleriYerlestir(ifade, sonListe):
    anaListe = list()
    temp = ""
    parantezSayisi, acikParantezIndex, kapaliParantezIndex = 0, 0, 0
    
    i = 0
    while i < len(sonListe):

        if sonListe[i] == "(":
            parantezSayisi += 1
            acikParantezIndex = i + 1

            kapaliParantezIndex = acikParantezIndex
            while parantezSayisi != 0:
                if sonListe[kapaliParantezIndex] == "(":
                    parantezSayisi += 1

                elif sonListe[kapaliParantezIndex] == ")":
                    parantezSayisi -= 1

                kapaliParantezIndex += 1

            kapaliParantezIndex -= 1
            temp = ""
            temp = ifade[acikParantezIndex: kapaliParantezIndex]
            araListe = [*temp]
            anaListe.append(parantezleriYerlestir(temp, araListe))
            
            i = kapaliParantezIndex
            
        else:
            if sonListe[i] == "*":
                anaListe.append("0")

            else:
                anaListe.append(sonListe[i])  

        i += 1
    return anaListe

    # KELİME YAP -------------------------------------------------------------------------------------------------------------------------------------------

def kelimeYap(liste):
    kelime = ""
    for i in range(0, len(liste)):
        if type(liste[i]) is list:
            kelime = kelime + "(" + kelimeYap(liste[i]) + ")"

        else:
            kelime = kelime + liste[i]  

    return kelime

    # GİRDİ KONTROL ----------------------------------------------------------------------------------------------------------------------------------------

def girdiKontrol(alfabe, ifade):
    legalListe = list()
    legalListe = ["(", ")", "+", "*", "0"]
    legalListe.extend(alfabe)
    for i in [*ifade]:
        if i in legalListe:
            pass
        else:
            return 0 
    return 1

    # CIKTI LİSTESİNİ ELDE EDİYORUZ -------------------------------------------------------------------------------------------------------------------------------------------------

def ciktiListesiEldeEt(x, ifade, listem, yazdirmaSayisi):
    
    ciktiListem = list()
    a = list()

    i = 0
    while i < yazdirmaSayisi:
        a = toplamFonksiyonu(x)
        x = parantezleriYerlestir(ifade, listem)
        ciktim = yazdir(a, i+1)
        if ciktim in ciktiListem:            
            i -= 1
        else:
            ciktiListem.append(ciktim)

        i += 1
    return ciktiListem

    # MAIN -------------------------------------------------------------------------------------------------------------------------------------------------

def main():

    # KULLANICIDAN BİLGİ AL --------------------------------------------------------------------------------------------------------------------------------

    while True:
        alfabe = input("Lütfen alfabeyi giriniz : ").split(",")
        ifade = input("Lütfen ifadeyi giriniz : ")
        yazdirmaSayisi = int(input("Lütfen yazdirmak istediğiniz eleman sayisini giriniz : "))

        if girdiKontrol(alfabe, ifade):
            break

        else:
            print("HATA ! Girdiğiniz ifade alfabede olan harflerden farklı. Lütfen tekrar giriniz.")

    listem = [*ifade]
    print("Ifadem --> ", ifade)
    x = parantezleriYerlestir(ifade, listem)
    print("x Listesi --> ", x)

    # -----------------------------------------------------------------------------------------------------------------------------------------------------

    if "0" not in x:
        ciktiListem = ciktiListesiEldeEt(x, ifade, listem, yazdirmaSayisi)
    else:
        ciktiListem = ciktiListesiEldeEt(x, ifade, listem, 150)

    print(ciktiListem)

    while True:
        print("\n-----------------------------------------------------------")
        arananIfade = input("Lutfen aradiginiz ifadeyi giriniz : ")

        if arananIfade in ciktiListem:
            print("Girdiğiniz ifade Bu Dile Aittir !")
        else:
            print("Girdiğiniz ifade Bu Dile Ait DEĞİLDİR !")

        cevap = input("Isleme devam etmek ister misiniz ? (e/h) : ")

        if cevap == "h":
            print("\nIslem Sonlandiriliyor ... \n")
            break

if __name__ == "__main__":
    main()