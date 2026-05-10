# Zadanie 1: Zbalansowane drzewa ⚖️
#
# Na wejściu dany jest korzeń drzewa binarnego. Sprawdź czy dane drzewo binarne jest zbalansowane i zwróć jego wysokość. W tym celu zaimplementuj dwie funkcje:
#
#     get_height(root: Optional[Node]), która zwraca wysokość drzewa z korzeniem w root
#     is_balanced(root: Optional[Node]), która zwraca true jeżeli drzewo jest zbalansowane i false w przeciwnym przypadku
#
# Wysokość drzewa to długość najdłuższej ścieżki od korzenia do liścia. Przyjmij, że drzewo puste ma wysokość -1, a drzewo składające się tylko z korzenia ma wysokość 0.
#
# Drzewo binarne jest zbalansowane (zrównoważone), gdy dla każdego węzła różnica między wysokościami jego poddrzew nie przekracza jednego. Innymi słowy, dla każdego węzła w drzewie binarnym, wysokość jego lewego poddrzewa i wysokość jego prawego poddrzewa różnią się co najwyżej o 1. Drzewo puste jest zbalansowane.
#
# Sprawdzanie czy dane drzewo jest zbalansowane można zaimplementować z użyciem funkcji sprawdzającej wysokość drzewa, jednak wtedy rozwiązanie ma złożoność kwadratową. Spróbuj zaimplementować rozwiązania o złożoności O(n)O(n) gdzie n to jest liczba węzłów w drzewie. Implementacja rozwiązania w czasie liniowym może wymagać wykorzystania funkcji pomocniczej.
#
# Przykład 1:
#
# Drzewo zbalansowane o wysokości 2:
#
#        10
#      /    \
#     5     15
#    / \   /  \
#   3   7 12   20
#
# W tym drzewie każdy węzeł ma różnicę wysokości jego lewego i prawego poddrzewa nie większą niż 1. Na przykład, dla korzenia 10, wysokość lewego poddrzewa wynosi 1 oraz wysokość prawego poddrzewa wynosi 1, więc różnica wynosi 0. Podobnie dla węzła 5, wysokość lewego poddrzewa wynosi 0 oraz wysokość prawego poddrzewa wynosi 0, co daje różnicę 0. Ten wzorzec zachodzi dla wszystkich węzłów w drzewie, co sprawia, że jest ono zbalansowane.
#
# Przykład 2:
#
# Drzewa niezbalansowane o wysokości 2:
#
#    10
#     \
#      15
#       \
#        20
#
# W tym drzewie różnica wysokości lewego i prawego poddrzewa dla korzenia (10) wynosi -2, co wskazuje na brak zrównoważenia.

from typing import Optional
from utils import Node, parse_input
import sys, os

"""
Złożoność czasowa:
- get_height - O(N), gdzie N to liczba węzłów w drzewie (dla każdego z nich wywołujemy
rekurencyjnie funkcję get_height, która wykonuje operacje o stałym koszcie)
- check_balance - O(N), gdzie N to liczba węzłów w drzewie (dla każdego z nich wywołujemy
rekurencyjnie funkcję get_height, która wykonuje operacje o stałym koszcie)
- is_balanced - dokładnie taka sama złożoność jak check_balance - tylko 
sprawdzamy dodatkowo, czy wynik check_balance jest > -1 - co jest stałe czasowo

Złożoność pamięciowa:
- get_height: O(H), gdzie H to wysokość drzewa (tyle maksymalnie ramek wywołań 
rekurencyjnych funkcji będzie w jednym momencie będzie na stosie)
- check_balance: O(H), gdzie H to wysokość drzewa (tyle maksymalnie ramek wywołań 
rekurencyjnych funkcji będzie w jednym momencie będzie na stosie)
- is_balanced: dokładnie taka sama jak check_balance

check_balance robi dwie rzeczy naraz zastępująć get_height (jeżeli drzewo jest 
zbalansowane to zwraca jego wysokość), jednocześnie wykrywa, czy drzewo jest
zbalansowane - zwraca -1 lub inną wybraną liczbę ujemną, gdy drzewo nie jest zbalansowane
"""


def get_height(root: Optional[Node]) -> int:
    if root is None:
        return -1  # zgodnie z konwencją, wysokość drzewa pustego jest równa -1
    left = 1 + get_height(
        root.left)  # zwiększamy wysokość o 1 i rekurencyjnie wywołujemy sprawdzanie wysokości poddrzewa lewego
    right = 1 + get_height(
        root.right)  # zwiększamy wysokość o 1 i rekurencyjnie wywołujemy sprawdzanie wysokości poddrzewa prawego
    return max(left, right)  # zwracamy maksymalną wysokość (największą wysokość obliczonego poddrzewa)


def check_balance(node: Optional[Node]) -> int:
    if node is None:  # dla node'a wysokość to 0
        return 0
    left = check_balance(node.left)  # rekurencyjnie wywołujemy sprawdzanie balansu dla lewego poddrzewa
    if left == -1:  # jeżeli left jest równe -1 (czyli albo we wcześniejszym wywołaniu rekurencyjnym był równy -1 lub zaszło  abs(right - left) > 1), to zwróć -1
        return -1
    right = check_balance(node.right)  # rekurencyjnie wywołujemy sprawdzanie balansu dla prawego poddrzewa
    if right == -1:  # jeżeli right jest równe -1 (czyli albo we wcześniejszym wywołaniu rekurencyjnym był równy -1 lub zaszło  abs(right - left) > 1), to zwróć -1
        return -1
    if abs(right - left) > 1:  # jeżeli wysokości right i left różnią się co najmniej o 2 - drzewo nie jest zbalansowane, zwracamy -1
        return -1
    return 1 + max(left,
                   right)  # jeżeli wszystko jest dobrze i nie wykryto niezbalansowania, przekaż rekurencyjnie w górę wysokość węzła


def is_balanced(root: Optional[Node]) -> bool:
    return check_balance(
        root) > -1  # jeżeli wynikiem check_balance jest -1 - to znaczy że w jednym z wywołań rekurencyjnych wykryto niezbalansowanie
    # w takim wypadku funkcja check_balance zawsze zwróci -1, w przeciwnym wypadku zwróci po prostu wysokość drzewa

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
