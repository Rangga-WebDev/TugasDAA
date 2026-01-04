def knapsakCihuy(kapasitas, item):
    n = len(item)
    nama = [i[0] for i in item]
    berat = [i[1] for i in item]
    nilai = [i[2] for i in item]

    K = [[0 for x in range(kapasitas + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(kapasitas + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif berat[i-1] <= w:
                K[i][w] = max(nilai[i-1] + K[i-1][w-berat[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    itemTerpilih = []
    totalVal = K[n][kapasitas]
    w = kapasitas
    
    for i in range(n, 0, -1):
        if totalVal <= 0: break
        if totalVal != K[i-1][w]:
            itemTerpilih.append(item[i-1])
            totalVal -= nilai[i-1]
            w -= berat[i-1]

    return K[n][kapasitas], itemTerpilih

item = [
    ("Medkit", 2, 15),
    ("Air Galon", 5, 10),
    ("Makanan Kaleng", 3, 12),
    ("Shotgun", 6, 25),
    ("Radio", 1, 8),
    ("Baterai", 1, 5),
    ("Tenda", 8, 20),
    ("Jaket", 2, 7),
    ("Peta", 1, 9),
    ("Pisau", 1, 14)
]
kapasitas_tas = 25

max_val, pilih = knapsakCihuy(kapasitas_tas, item)
totalBerat = sum(i[1] for i in pilih)

print("Mainkan : ") 
print(f"Total Nilai Maksimum: {max_val}")
print(f"Total Berat: {totalBerat} / {kapasitas_tas} kg")
print("Barang yang dibawa:")
for item in pilih:
    print(f"- {item[0]} (Berat: {item[1]}, Nilai: {item[2]})")
