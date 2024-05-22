#koşullar,döngüler,listeler,fonksiyonlar konusu pekiştirme.
#beytullahgüney
def yashesapla(isim,soyisim,yıl):
    yıl = int(yıl)
    yas = 2023-yıl
    yas = str(yas)
    sonuc = isim + " " + soyisim + " Yaş Bilgisi : " + yas
    return sonuc

tekraretme = 0

adet = input("Kaç kullanıcı tanımlanıcak ? : ")
adet = int(adet)

dogumyılları = []
isimleri = []
soyisimleri = []
meslekleri = []
kullanıcılar = []


while  adet > 0:
    adet = adet - 1

    #kayıt etme
    dogumyili = input("Doğum Yılı : ")
    dogumyili = int(dogumyili)

    isim = input("İsmi : ")
    soyad = input("Soyadı : ")
    meslek = input("Meslek : ")


    print("---------------------------")

    #listelere ekleeme
    dogumyılları.append(dogumyili)
    isimleri.append(isim)
    soyisimleri.append(soyad)
    meslekleri.append(meslek)


    kullanıcılar.append(isim + " " + soyad)

print("1 - Sisteme kayıtlı kullanıcıların doğum yıllarını görüntüleme")
print("2 - Sisteme kayıtlı kullanıcıların isimlerini görüntüleme")
print("3 - Sisteme kayıtlı kullanıcıların soyisimlerini görüntüleme")
print("4 - Sisteme kayıtlı kullanıcıların mesleklerini görüntüleme")
print("5 - Sisteme kayıtlı kullanıcıları görüntüleme")
print("6 - Sisteme kayıtlı kullanıcıların yaşlarını görüntüleme")

while True:

    print("A tuşuna basarak çıkış yapabilirsiniz..")
    print("")
    islem = input("Yapılcak İşlemi giriniz : ")

    if islem == "A" or islem == "a":
        tekraretme = 0
        print("Kayıtlar yapılmışdır. İyi günler..")
        break
    else:
         if islem == "1":
             tekraretme = 0
             for i in dogumyılları:
                 print("Doğum yılları : " , i)

         elif islem == "2":
             tekraretme = 0
             for i in isimleri:
                 print ("İsimler : ",i)

         elif islem == "3":
             tekraretme = 0
             for i in soyisimleri:
                 print("Soyisimleri : ",i)

         elif islem == "4":
             tekraretme = 0
             for i in meslekleri:
                 print("Meslekleri : ",i)

         elif islem == "5":
             tekraretme = 0
             for i in kullanıcılar:
                 print("Kullanıcılar : ",i)

         elif islem == "6":
             tekraretme = 0
             a = list(map(yashesapla,isimleri,soyisimleri,dogumyılları))
             print(a)

         elif islem == "":
             print("")
             print("Lütfen geçerli bir değer giriniz veya A tuşuna basarak çıkınız..")

         else:
             if tekraretme == 3:
                 print("")
                 print("Çok fazla geçersiz değer girdiğiniz için sistemden çıkış yapılıyor..")
                 break
             else:
                 print("")
                 print("Lütfen geçerli bir değer giriniz")
                 tekraretme = tekraretme + 1






