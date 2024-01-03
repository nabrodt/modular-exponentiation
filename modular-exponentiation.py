import time

# Modular exponentiation algorithm
def modular_exponentiation(base: int, n: int, modul: int):
    result = 1
    power = base % modul
    while n > 0:
        if ((n & 1 ) == 1):
            result = (result * power) % modul
        power = (power * power) % modul
        n = n >> 1
    return result



# Task 1: 5^99 mod 11
def task1():
    print('Task 1: 5^99 mod 11')
    print('Wolfram alpha solution: 9')

    start_time = time.time()
    for i in range(5000):
        a1 = pow(5, 99) % 11
    print("--- %s seconds ---" % (time.time() - start_time))

    print("python solution: %s \n" % (a1))
    # a2 = pow(5, 99, 11)
    # print(a2)

    print('Own algorithm:')
    start_time = time.time()
    for i in range(5000):
        a3 = modular_exponentiation(5, 99, 11)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("own solution: %s \n \n" % (a3))


# Task 2: 50^529 mod 13
def task2():
    print('Task 2: 50^529 mod 13')
    print('Wolfram alpha solution: 11')

    start_time = time.time()
    for i in range(5000):
        b1 = pow(50, 529) % 13
    print("--- %s seconds ---" % (time.time() - start_time))

    print("python solution: %s \n" % (b1))
    # b2 = pow(50, 529, 13)
    # print(b2)

    print('Own algorithm:')
    start_time = time.time()
    for i in range(5000):
        b3 = modular_exponentiation(50, 529, 13)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("own solution: %s \n \n" % (b3))

# Task 3: 50^999 mod 17
def task3():
    print('Task 3: 50^999 mod 17')
    print('Wolfram alpha solution: 16')

    start_time = time.time()
    for i in range(5000):
        c1 = pow(50, 999) % 17
    print("--- %s seconds ---" % (time.time() - start_time))

    print("python solution: %s \n" % (c1))
    # c2 = pow(50, 999, 17)
    # print(c2)

    print('Own algorithm:')
    start_time = time.time()
    for i in range(5000):
        c3 = modular_exponentiation(50, 999, 17)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("own solution: %s \n \n" % (c3))


# Own task: 999^999 mod 14
def task4():
    print('Own task: 999^999 mod 14')
    print('Wolfram alpha solution: 13')

    start_time = time.time()
    for i in range(5000):
        d1 = pow(50, 50) % 3
    print("--- %s seconds ---" % (time.time() - start_time))

    print("python solution: %s \n" % (d1))

    d2 = pow(50, 50, 3)
    print("python solution with pow(50, 50, 3): %s \n" % (d2))

    print('Own algorithm:')
    start_time = time.time()
    for i in range(5000):
        d3 = modular_exponentiation(999, 999, 14)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("own solution: %s" % (d3))

def main():
    task1()
    task2()
    task3()
    task4()

main()