import random
import matplotlib.pyplot as plt

from InisiasiPopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import roulette_wheel_selection
from crossover import one_point_crossover
from mutation import uniform_mutation


barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 69, 11),
    ("Barang6", 70, 9),
    ("Barang7", 80, 15),
    ("Barang8", 90, 10),
    ("Barang9", 25, 3)
]

kapasitas_tas = 50


def genetic_algorithm(
    generasi=50,
    jumlah_populasi=20,
    crossover_rate=0.7,
    mutation_rate=0.1
):

    jumlah_gen = len(barang)

    populasi = inisialisasi_populasi(
        jumlah_populasi,
        jumlah_gen
    )

    grafik_best = []

    best_individu = None
    best_fitness = 0

    for g in range(generasi):

        fitness_populasi = [
            hitung_fitness(individu, barang, kapasitas_tas)
            for individu in populasi
        ]

        nilai_terbaik = max(fitness_populasi)
        grafik_best.append(nilai_terbaik)

        if nilai_terbaik > best_fitness:
            best_fitness = nilai_terbaik
            index = fitness_populasi.index(nilai_terbaik)
            best_individu = populasi[index]

        populasi_baru = []

        while len(populasi_baru) < jumlah_populasi:

            parent1 = roulette_wheel_selection(
                populasi,
                fitness_populasi
            )

            parent2 = roulette_wheel_selection(
                populasi,
                fitness_populasi
            )

            if random.random() < crossover_rate:
                anak1, anak2 = one_point_crossover(
                    parent1,
                    parent2
                )
            else:
                anak1 = parent1.copy()
                anak2 = parent2.copy()

            anak1 = uniform_mutation(anak1, mutation_rate)
            anak2 = uniform_mutation(anak2, mutation_rate)

            populasi_baru.extend([anak1, anak2])

        populasi = populasi_baru[:jumlah_populasi]

    print("\nHasil Terbaik")
    print("Fitness :", best_fitness)

    total_bobot = 0

    for i in range(len(best_individu)):
        if best_individu[i] == 1:
            print("-", barang[i][0])
            total_bobot += barang[i][2]

    print("Total Bobot :", total_bobot)

    plt.plot(grafik_best)
    plt.title("Perkembangan Fitness")
    plt.xlabel("Generasi")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.show()


genetic_algorithm()
