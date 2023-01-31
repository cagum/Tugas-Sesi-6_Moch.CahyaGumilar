print('Moch. Cahya Gumilar')
print('NIM : 20220040116, TI22B')
print('Menghitung Jumlah Kalori yang Terbakar')

aktivitas = input("Aktivitas olahraga yang dilakukan (lari, push-up, atau plank)? ")
durasi = int(input("Berapa lama waktu yang digunakan (dalam menit)? "))
if aktivitas == "lari":
    kalori_terbakar = (durasi/5) * 60
elif aktivitas == "push-up":
    kalori_terbakar = (durasi/30) * 200
elif aktivitas == "plank":
    kalori_terbakar = durasi * 5
else:
    kalori_terbakar = 0

print("Jumlah kalori yang terbakar adalah", kalori_terbakar,'Kalori')