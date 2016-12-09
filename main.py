def check_odd_occurences(data_array):
    panjang = len(data_array)
    paired = []
    jomblo = []
    for i in range(panjang):



N = input('Masukkan jumlah data : ')
list = []
if (N%2 == 1):
    i=1
    while i <= N:
        data = input('Masukkan nilai ke-%d : '%i)
        list.append(data)
        i += 1
else:
    print 'Jumlah harus ganjil'

check_odd_occurences(list)
print list
