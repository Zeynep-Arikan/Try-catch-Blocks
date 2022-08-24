liste = ["1","3","5ab","0b","der","70","15"]
# 1: liste elemanları içindeki sayısal değerleri bulunuz.

for x in liste:
    try:
        result= int(x)
        print(result)
    except ValueError:
        continue

#2: kulanıcı q degerini girmedikçe aldığınız her inputun sayı oldugunda emin olun aksi halde hata mesajı yazın
while True:
    sayi = input('sayi: ')
    if sayi == 'q':
        break
    try:
        result = float(sayi)
        print(result)
    except:
        print('geçersiz sayi')
        continue

#3: girilen parola içinde türkçe karakter hatası veriniz

def  checkPassword(parola):
    turkce = 'şçöüıİğ'

    for i in parola:
        if i in turkce:
            raise TypeError('parola türkçe karakter içeremez')
        else:
            pass
    print('geçerli parola')
parola = input('parola: ')

try:
    checkPassword(parola)
except TypeError as err:
    print(err)

#4: faktöriyel fonksiyonu oluşturup fonksiyona gelen deger için hata mesajlarını verin.

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif deger')
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

for x in [5,10,20,-4,'12s']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
            print(err)
            continue
    print(y)