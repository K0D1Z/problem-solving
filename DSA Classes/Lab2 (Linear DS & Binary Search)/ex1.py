# Zadanie 1 – Setne zadanie na LeetCode
#
# Student przez rok rozwiązuje zadania na platformie programistycznej.
# Dane są w postaci dwuwymiarowej tablicy: progress[week][day]
#
#     Każdy tydzień ma dokładnie 7 dni.
#
#     progress[w][d] oznacza łączną liczbę poprawnie rozwiązanych zadań do końca danego dnia.
#
#     Wartości są niemalejące (liczba rozwiązanych zadań nigdy nie maleje).
#
# Przykład
#
# progress = [
#     [0, 0, 1, 1, 3, 3, 5],
#     [5, 7, 10, 15, 20, 25, 30],
#     ...
# ]
#
# Treść zadania
#
# Napisz funkcję:
#
# def day_of_100th_problem(progress: List[List[int]]) -> Tuple[int, int]:
#
# która zwraca: (week_index, day_index)
#
# pierwszego dnia, w którym liczba rozwiązanych zadań była co najmniej 100.
#
# Jeśli student w ciągu roku nie osiągnął 100 rozwiązań — zwróć: (-1, -1)

from typing import List, Tuple
from utils import parse_input
import os
import sys

'''
Analiza złożoności czasowej algorytmu:
- O(n^2) - w przypadku, gdy liczba zadań wyniosła co najmniej 100
ostatniego dnia ostatniego tygodnia lub gdy nie było dnia w liście,
którego wartość wynosiła co najmniej 100

- Ω(1) - w przypadku, gdy pod koniec pierwszego dnia 
pierwszego tygodnia łączna liczba rozwiązanych zadań 
wyniosła co najmniej 100

- ponieważ złożoność w notacji O i Ω są różne, to nie mogę określić
ogólnej złożoność algorytmu w notacji θ, możemy ewentualnie określić
złożoność w notacji θ dla poszczególnego przypadku (optymistycznego,
pesymistycznego lub średniego)

Analiza złożoności pamięciowej algorytmu:
- O(1), Ω(1), θ(1) - w całym programie nie używamy dodatkowych zmiennych
tablicowych, tylko odczytujemy indeksy z przekazanej jako argument listy;
tak naprawdę nie deklarujemy nawet zmiennych pomocniczych.
'''


def day_of_100th_problem(progress: List[List[int]]) -> Tuple[int, int]:
    for week in range(len(progress)):  # pętla wykonuje się n razy
        for day in range(len(progress[week])):  # pętla wykonuje się m razy
            if progress[week][day] >= 100:  # n*m powtórzeń daje O(n^2)
                return (week, day)  # O(1)
    return (-1, -1)  # O(1)

# if __name__ == "__main__":
#     if "--debug" in sys.argv:
#         from run_tests import run_tests
#
#         run_tests()
#     else:
#         raw_input = parse_input(input(), os.path.abspath(__file__))
