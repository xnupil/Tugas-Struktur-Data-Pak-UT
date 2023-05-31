import numpy as np

buah = ['Apel', 'Jeruk', 'Pisang', 'Kiwi', 'Mangga']
kalori_buah = [91, 71, 103, 105, 96]
harga_buah = [2360, 2120, 1890, 3870, 2870]
stok_buah = [5, 10, 5, 10, 5]

uang_pak_blangkon = 25000

jumlah_buah_dibeli = np.minimum(stok_buah, np.floor(uang_pak_blangkon / np.array(harga_buah)))

total_kalori = np.sum(jumlah_buah_dibeli * np.array(kalori_buah))

print(int(total_kalori))  

print(jumlah_buah_dibeli)

a = (5*2360)+(10*2120)+(5*1890)+(6*3870)+(5*2870)
print(a)