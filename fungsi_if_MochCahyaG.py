"DISNEY ISLAND"
print('Silahkan isi form di bawah ini untuk verifikasi umur anda')
print('=====================================================')

ages = 2,4,7,10
talls = 70,120,150
price = 30000, 40000, 50000, 80000
tall_extra = 10000, 15000, 20000

age = int(input('Umur = '))
tb = int(input('Tinggi badan = '))

if age < ages[0]:
    print('Dilarang Masuk')
elif age < ages[1]:
    if tb > talls[0]:
        print('Tarif Masuk Rp. ',price[0] + tall_extra[0])
    else:
        print('Tarif Masuk Rp. ',price[0])
elif age < ages[2]:
    if tb > talls[1]:
        print('Tarif Masuk Rp. ',price[1] + tall_extra[1])
    else:
        print('Tarif Masuk Rp. ',price[1])
elif age < ages[3]:
    if tb > talls[2]:
        print('Tarif Masuk Rp. ',price[2] + tall_extra[2])
    else:
        print('Tarif Masuk Rp. ',price[2])
else:
    print('Tarif Masuk Rp. ',int(price[3]))





