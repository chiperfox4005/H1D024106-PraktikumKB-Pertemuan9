import random

def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    populasi = []

    for i in range(jumlah_populasi):
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)

    return populasi


if __name__ == "__main__":
    populasi_awal = inisialisasi_populasi(10, 5)

    print("Populasi Awal")
    for i, individu in enumerate(populasi_awal):
        print(f"Individu {i+1} : {individu}")