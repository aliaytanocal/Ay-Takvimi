#Bu kısımda kullanıcıdan bir yıl girilmesini istiyoruz.
yil = int(input("Lütfen bir yıl giriniz: "))

#Bu kısımda kullanıcıdan bir ay girilmesini istiyoruz.
ay = int(input("Lütfen bir ay giriniz: "))

#Bu kısımda ay takviminin başlığını yazdırıyoruz.
print("\n\t\t", ay, yil, "Ay Takvimi\n")

#Bu kısımda ayın ilk gününü hesaplıyoruz.
#Bu hesaplamada yıl 0'dan başlar ve Ocak ayı 1 olarak kabul edilir.
#Ocak ve Şubat aylarından önceki aylar için yıl -1 yapılır.
if ay == 1:
    yil -= 1
    ay = 13
elif ay == 2:
    yil -= 1
    ay = 14

#Bu kısımda ayın ilk gününü hesaplıyoruz.
#Formül: (1 + (13 * (ay + 1)) / 5 + yil + (yil / 4) - (yil / 100) + (yil / 400)) % 7
#Bu formül Gregorian takvimine göre ayın ilk gününü hesaplar.
ilk_gun = (1 + (13 * (ay + 1)) / 5 + yil + (yil / 4) - (yil / 100) + (yil / 400)) % 7

#Bu kısımda ay takvimini yazdırıyoruz.
#Önce günlerin isimlerini yazdırıyoruz.
print(" Paz  Pzt  Sal  Çar  Per  Cum  Cmt")

#Daha sonra ayın ilk günü kadar boşluk bırakıyoruz.
for i in range(int(ilk_gun)):
    print("     ", end="")

#Daha sonra ayın tüm günlerini yazdırıyoruz.
#Bir satırda 7 gün yer alır ve bir sonraki satıra geçildiğinde boşluk bırakılır.
for i in range(1, 31):
    print("{:5}".format(i), end="")
    if (i + int
