#! /usr/bin/env python

import math
import random
import numpy as np  # używam do sprawdzenia poprawności

# ********************Calculations and algorithms****************


def quadratic_equation():
    wsp = input("Podaj współczynniki równania kwadratowego: [a b c]")
    a, b, c = wsp.split()
    a, b, c = float(a), float(b), float(c)
    delta = math.pow(b, 2) - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("To równanie ma 2 pierwiastki: x1=", x1, "x2=", x2)
    elif delta == 0:
        x =(-b)/2*a
        print("Twoje równanie ma jedno rozwiązanie: x =", x)
    elif delta < 0:
        print("Twoje równanie nie ma rozwiązań rzeczywistych")


def sorting(numbers):
    k = len(numbers)
    print(numbers)
    while k > 1:
        change = False
        for i in range(0, k-1):
            if numbers[i] < numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                change = True
        k-1
        if change == False:
            break
    print(numbers)


def scalar_product(a,b):
    if len(a) == len(b):
        scal_prod = 0
        for i in range(0, len(a)):
            scal_prod = scal_prod + (a[i]*b[i])
        print("Iloczyn skalarny wektorów ", a , "i", b , "to:", scal_prod)

    else:
        print(" Nie można obliczyć iloczynu skalarnego !!! WEKTORY różnej długości")


def generate_random_numbers(quantity):
    numbers = []
    for i in range(quantity):
        numbers.append(random.randint(0, 50))
    return numbers


def matrix_generation(x, y):
    #matrix = np.zeros(shape=(x, y))
    matrix = [[0 for x1 in range(y)] for y1 in range(x)]
    for i in range(0, x):
        for j in range(0, y):
            matrix[i][j] = random.randint(-10, 10)
    return matrix


def matrix_sum(m1, m2):
    x1 = len(m1)
    y1 = len(m1[0])
    x2 = len(m2)
    y2 = len(m2[0])
    if x1 != x2 or y1 != y2:
        print("Macierze muszą mieć ten sam rozmiar")
    else:
        sum_numpy = np.add(m1, m2)
        sum_matrix = [[0 for i in range(y1)]for i in range(x1)]
        print(sum_numpy)
        for i in range(0, x1):
            for j in range(0, y1):
                sum_matrix[i][j] = m1[i][j] + m2[i][j]
        print(sum_matrix)


def matrix_multiplication(m1, m2):
    x1 = len(m1)
    y1 = len(m1[0])
    x2 = len(m2)
    y2 = len(m2[0])
    multiplied_matrix = [[0 for i in range(y2)]for i in range(x1)]
    if y1 != x2:
        print("Tych macierzy nie mozna przemnozyć przez siebie")
    else:
        for a in range(x1):
            for b in range(y2):
                for c in range(x2):
                    multiplied_matrix[a][b] += m1[a][c] * m2[c][b]
        multi_numpy = np.dot(m1, m2)
        print(multi_numpy)
        print(multiplied_matrix)


def det_of_matrix(m):
    print(m)
    x = len(m)
    y = len(m[0])
    if x != y:
        print("Aby obliczyć wyznacznik, macierz musi być kwadratowa")
    else:
        m_L = [[0 for i in range(x)]for i in range(y)]
        m_U = [[0 for i in range(x)]for i in range(y)]

        for i in range(x):
            for k in range(i, x):
                suma = 0
                for j in range(i):
                    suma += (m_L[i][j] * m_U[j][k])
                m_U[i][k] = m[i][k] - suma

            for k in range(i, x):
                if i == k:
                    m_L[i][i] = 1
                else:
                    suma = 0
                for j in range(i):
                    suma += (m_L[k][j] * m_U[j][i])
                m_L[k][i] = int(m[k][i] - suma)/m_U[i][i]
        det_U = 1
        det_L = 1
        for i in range(x):
            for k in range(x):
                if i == k:
                    det_U *= m_U[i][i]
                    det_L *= m_L[i][i]
        det = det_U*det_L
        print(det)
        print(np.linalg.det(m))
        print(m_U)
        print(m_L)


if __name__ == '__main__':
    # quadratic_equation()
    # sorting(generate_random_numbers(50))
    # scalar_product([1, 2, 12, 4], [2, 4, 2, 8])
    # matrix_generation(4,4)
    # matrix_sum(matrix_generation(128, 128), matrix_generation(128, 128))
    # matrix_multiplication(matrix_generation(3, 3), matrix_generation(3, 4))
     det_of_matrix(matrix_generation(2, 2)) 
    # luDecomposition(matrix_generation(3,3),3)
