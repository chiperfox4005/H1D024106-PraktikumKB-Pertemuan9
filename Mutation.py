import random


def swap_mutation(kromosom):
    kromosom = kromosom.copy()

    a, b = random.sample(range(len(kromosom)), 2)

    kromosom[a], kromosom[b] = kromosom[b], kromosom[a]

    return kromosom


def inversion_mutation(kromosom):
    kromosom = kromosom.copy()

    a = random.randint(0, len(kromosom)-2)
    b = random.randint(a+1, len(kromosom)-1)

    kromosom[a:b] = reversed(kromosom[a:b])

    return kromosom


def uniform_mutation(kromosom, mutation_rate=0.1):
    kromosom = kromosom.copy()

    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]

    return kromosom


if __name__ == "__main__":
    anak = [0, 1, 1, 0, 1]

    print("Sebelum :", anak)
    print("Swap :", swap_mutation(anak))
    print("Inversion :", inversion_mutation(anak))
    print("Uniform :", uniform_mutation(anak))