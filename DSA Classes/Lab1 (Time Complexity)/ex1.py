# Zadanie 1 – Najdłuższy niemalejący fragment
#
# Cel zadania
#
# Celem zadania jest zaimplementowanie funkcji analizującej tablicę liczb oraz określenie jej złożoności czasowej i pamięciowej. Zadanie ma na celu utrwalenie pracy z pętlą, analizą przypadków oraz rozumieniem złożoności obliczeniowej algorytmu.
# Treść zadania
#
# Zaimplementuj funkcję, która dla podanej tablicy liczb całkowitych numbers zwraca długość najdłuższego spójnego fragmentu tablicy, w którym elementy są niemalejące. Fragment niemalejący to taki, w którym każdy kolejny element jest większy lub równy poprzedniemu. Fragment spójny to taki złożony z elementów kolejno następujących po sobie w ciągu bazowym.
# Przykłady
#
# 1. Dla tablicy: [1, 2, 2, 5, 3, 4, 4, 4, 1] wynikiem powinno być: 4 ponieważ najdłuższy niemalejący spójny fragment to: [3, 4, 4, 4].
#
# 2. Dla tablicy: [5, 4, 3, 2] wynikiem powinno być: 1. Każdy pojedynczy element jest fragmentem niemalejącym długości 1.
#
# 3. Dla tablicy: [1, 2, 3, 4, 5] wynikiem powinno być: 5
#
# Część analityczna (obowiązkowa)
#
# Po zaimplementowaniu funkcji:
#
#     Określ złożoność czasową algorytmu.
#
#     Określ złożoność pamięciową algorytmu. (wystarczy czasowa, nie przerabialiśmy jeszcze pamięciowej na lekcji :))
#
#     Wskaż:
#
#         przypadek najlepszy (best case),
#
#         przypadek najgorszy (worst case),
#
#         czy różnią się one asymptotycznie.
#
# Odpowiedzi wraz z uzasadnieniem umieść w komentarzu nad funkcją.

from typing import List
from utils import parse_input
import os
import sys

"""
Nie wliczam inicjalizacji obiektu range - nie będzie to miało
znaczenia podczas wyznaczania czynnika dominującego

Złożoność czasowa algorytmu:
Przybliżony wzór funkcji czasu: T(n) = C1 + C2 * (n-1), gdzie
C1, C2 - stałe, n - długość listy, z czego wynika złożoność liniowa
algorytmu: n * Θ(1) ∈ Θ(n)

O(n), Ω(n), Θ(n) - następuje n wykonań pętli, gdzie n to długość
listy w argumencie funkcji, wszystkie pozostałe operacje w funkcji mają
stałą złożoność czasową Θ(1)

Przypadek najlepszy - cała lista składa się z ciągu rosnącego lub lista
składa się tylko z jednego elementu.
Przypadek najgorszy - cała lista składa się z ciągu niemalejącego.
W praktyce czynnik dominujący dla przypadku najgorszego i najlepszego 
jest równy n, więc nie różnią się one asymptotycznie. 

Dla listy pustej algorytm od razu zwraca 0 - wtedy złożoność czasowa 
wynosi Θ(1).

Złożoność pamięciowa (nie było jeszcze na zajęciach, ale w tym przypadku
łatwa do określenia) - wynosi Θ(1) - mamy stałą liczbę zmiennych pomocniczych,
nie tworzymy dodatkowych list, jedyna lista, którą używamy została przekazana
w argumencie funkcji.

"""


def longest_non_decreasing_segment(numbers: List[int]) -> int:
    if not numbers:  # Θ(1)
        return 0  # Θ(1)
    numbers_length = len(numbers)  # Θ(1) z dokumentacji Pythona
    max_length = 1  # Θ(1)
    segment_length = 1  # Θ(1)
    for i in range(numbers_length - 1):  # Θ(n)
        if numbers[i + 1] >= numbers[i]:  # Θ(1)
            segment_length += 1  # Θ(1)
            if segment_length > max_length:  # Θ(1)
                max_length = segment_length  # Θ(1)
        else:  # Θ(1)
            segment_length = 1  # Θ(1)
    return max_length  # Θ(1)

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
