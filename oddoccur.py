def check_odd_occurences(data_array):
    for i, val in enumerate(data_array):
        if (data_array.count(val) % 2) == 1:
            return i
    return -1

data = [9, 3, 9, 3, 9, 7, 9]
jomblo = check_odd_occurences(data)
print("elemen pada indeks ke-", jomblo, " (", data[jomblo], ") tidak mempunyai pasangan")