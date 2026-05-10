# Zadanie 2 – Najdłuższy fragment o niemalejących różnicach
#
# Cel zadania
#
# Celem zadania jest zaimplementowanie funkcji analizującej tablicę liczb oraz określenie jej złożoności czasowej i pamięciowej. Zadanie ma na celu utrwalenie pracy z pętlą, analizą przypadków oraz rozumieniem złożoności obliczeniowej algorytmu.
# Treść zadania
#
# Zaimplementuj funkcję, która dla podanej tablicy liczb całkowitych numbers zwraca długość najdłuższego spójnego fragmentu tablicy, w którym wartości bezwzględne różnic między kolejnymi elementami są niemalejące.
#
# Formalnie:
#
# Dla fragmentu al,al+1,...,ar
#
# musi zachodzić: ∣∣ai+1​−ai​∣≤∣ai+2​−ai+1​∣∣
#
# dla wszystkich indeksów w tym fragmencie.
#
# Przykłady
#
# 1. Dla tablicy:  [1, 3, 6, 10] Różnice: 2, 3, 4 Są niemalejące → wynik: 4
#
# 2. Dla tablicy:  [5, 1, 4, 2, 7] Różnice: 4, 3, 2, 5
#
# Najdłuższy poprawny fragment: 4, 2, 5 (różnice: 2, 5) → wynik: 3
#
# 3. Dla tablicy: [10, 8, 7, 6] Różnice: 2, 1, 1
#
# Najdłuższy fragment: 7, 6 (różnica: 1)  → wynik: 2
#
# Część analityczna (obowiązkowa)
#
# Po zaimplementowaniu funkcji:
#
#     Określ złożoność czasową algorytmu.
#
#     Określ złożoność pamięciową algorytmu.
#
#     Wskaż:
#
#         przypadek najlepszy (best case),
#
#         przypadek najgorszy (worst case),
#
#         czy różnią się one asymptotycznie.
#
# Uzasadnij odpowiedzi.

from typing import List
from utils import parse_input
import os
import sys

'''
Funkcja pomocnicza - złożoność θ(1)
'''


def calculate_difference(n1: int, n2: int) -> int:
    return abs(n1 - n2)  # θ(1)


'''
Złożoność czasowa: (n - 2) * Θ(1) ∈ Θ(n) - operacje w pętli powtarzają się 
n - 2 razy, gdzie n to długość listy. Pozostałe operacje mają stały czas 
wykonania. 
Uproszczona funkcja czasu wykonania T(n) = C1 + (n - 2) * C2,
gdzie C1, C2 - stałe, n - długość listy. Z tego wynika, że czynnik 
dominujący to n, z czego wynika, że algorytm ma złożoność czasową Θ(n).

Przypadek optymistyczny - każde wywołanie funkcji calculate_difference
dla kolejnych wyrazów ciągu daje mniejszą wartość od poprzedniej
(dla wszystkich wyrazów listy), inny przypadek optymistyczny - lista 
o długości 1 lub lista pusta.

Przypadek pesymistyczny - każde wywołanie funkcji calculate_difference
dla kolejnych wyrazów ciągu daje większą lub równą wartość 
(dla wszystkich wyrazów listy).

W praktyce złożoności dla przypadków optymistycznego i pesymistycznego
nie różnią się asymptotycznie, w obu przypadkach czynnik dominujący
to n (wynikający z pętli for)

O(n), Ω(n), θ(n)

Złożoność pamięciowa (nie było jeszcze mowa na zajęciach): 
Θ(1) - algorytm wykorzystuje i operuje na zmiennych przechowujących 
wartości liczbowe, nie są tworzone dodatkowe tablice lub inne struktury
'''


def longest_non_decreasing_diff_segment(numbers: List[int]) -> int:
    if not numbers:  # θ(1)
        return 0  # θ(1)
    numbers_length = len(numbers)  # θ(1)
    if numbers_length < 2:  # θ(1)
        return 1  # θ(1)
    previous_abs = calculate_difference(numbers[0], numbers[1])  # θ(1)
    max_segment = 1  # θ(1)
    temp_segment = 1  # θ(1)
    for i in range(1, numbers_length - 1):  # θ(n)
        current_abs = calculate_difference(numbers[i], numbers[i + 1])  # θ(1)
        if current_abs >= previous_abs:  # θ(1)
            temp_segment += 1  # θ(1)
            if temp_segment > max_segment:  # θ(1)
                max_segment = temp_segment  # θ(1)
        else:  # θ(1)
            temp_segment = 1  # θ(1)
        previous_abs = current_abs  # θ(1)
    return max_segment + 1  # θ(1)

    # Na końcu dodaję 1 do ilości elementów ciągu różnic
    # wartości bezwzględnych, którego długość to n.
    # Odpowiadajacy podciąg w liście numbers ma n + 1 wyrazów

###############################
# don't modify the code below #
###############################
# if __name__ == "__main__":
#     if "--debug" in sys.argv:
#         from run_tests import run_tests
#
#         run_tests()
#     else:
#         raw_input = parse_input(input(), os.path.abspath(__file__))
