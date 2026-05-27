barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 70, 15)
]

kapasitas_tas = 50


def hitung_fitness(kromosom, barang, kapasitas):
    total_harga = 0
    total_bobot = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]
            total_bobot += barang[i][2]

    if total_bobot > kapasitas:
        return 0

    return total_harga


if __name__ == "__main__":
    populasi = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1]
    ]

    print("Nilai Fitness")

    for i, individu in enumerate(populasi):
        fitness = hitung_fitness(individu, barang, kapasitas_tas)
        print(f"Individu {i+1} = {fitness}")