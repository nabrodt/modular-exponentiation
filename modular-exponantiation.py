# TODO computation time
# TODO own algorithm

import time

def main():
    task1()
    task2()
    task3()
    task4()


# Task 1: 5^99 mod 11
def task1():
    print('Task 1: 5^99 mod 11')
    print('Wolfram alpha solution: 9')
    a1 = pow(5, 99) % 11
    print(a1)
    start_time = time.time()
    a2 = pow(5, 99, 11)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(a2)

# Task 2: 50^529 mod 13
def task2():
    print('Task 2: 50^529 mod 13')
    print('Wolfram alpha solution: 11')
    b1 = pow(50, 529) % 13
    print(b1)
    start_time = time.time()
    b2 = pow(50, 529, 13)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(b2)

# Task 3: 50^999 mod 17
def task3():
    print('Task 3: 50^999 mod 17')
    print('Wolfram alpha solution: 16')
    c1 = pow(50, 999) % 17
    print(c1)
    start_time = time.time()
    c2 = pow(50, 999, 17)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(c2)


# Own task: 999^999 mod 14
def task4():
    print('Own task: 999^999 mod 14')
    print('Wolfram alpha solution: 13')
    d1 = pow(50, 50) % 3
    print(d1)
    start_time = time.time()
    d2 = pow(50, 50, 3)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(d2)


main()