# Dane jest drzewo binarne z korzeniem root. Zadanie polega na przejściu drzewa poziomami od korzenia w dół, od lewej do prawej i zapisać proces przechodzenia drzewa
#
# W tym celu zaimplementuj metodę get_level_order(root: Optional[Node]) -> List[List[int]], która przyjmuje korzeń drzewa i zwraca listę list (List[List[int]]), która reprezentuje proces przechodzenia drzewa. Zewnętrzna lista reprezentuje kolejne poziomy, a wewnętrzne listy reprezentują kolejne wartości węzłów na danym poziomie.
#
# Przykład 1:
#
# root:
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: [[3],[9,20],[15,7]]
#
# Przykład 2:
#
# root:
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# Output: [[1],[2,3],[4,5]]

from typing import Optional, List
from utils import Node, parse_input
import sys, os

"""
Złożoność czasowa:
O(n * n) - ze względu na użycie operacji del na kolejce, która kosztuje O(n)
złożoność się zwiększa (normalnie przy użyciu modułu queue byłoby to stałe)
n - liczba węzłów drzewa - odwiedzamy i przetwarzamy każdy węzeł jeden raz

Złożoność pamięciowa:
O(n) - gdzie n to liczba węzłów - w najgorszym przypadku (pełne drzewo), do kolejki
dodane zostanie n/2 elementów - tak samo do listy level_list przechowującej
tymczasowo wartości z danego poziomu. Wynikowa lista result będzie miała n
elementów w zagnieżdzonych listach co dodatkowa zwiększa złożoność pamięciową, ale
sumarycznie asymptotyczna złożoność pamięciowa wyniesie O(n)
"""


def get_level_order(root: Optional[Node]) -> List[List[int]]:
    result = []
    if root is None:
        return result  # zwróć pustą listę jak root jest None

    queue = [root]  # zainicjuj kolejkę z tylko rootem

    while queue:  # wykonuj pętle, dopóki kolejka nie jest pusta
        level = len(queue)  # oblicz obecny poziom
        level_list = []  # stwórz listę na node'y z obecnego poziomu

        for i in range(level):
            node = queue[0]  # weź pierwszy element z kolejki
            del queue[0]  # usuń ten wybrany element
            level_list.append(node.val)  # dodaj ten element do tymczasowej listy

            # jeżeli liść node'a nie jest None do dodaj go do kolejki na koniec
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        # po przejściu całego poziomu dodaj listę z wartościami do wynikowej listy
        result.append(level_list)
    return result  # na koniec zwróć wynikową listę


# ###############################
# # don't modify the code below #
# ###############################
# if __name__ == "__main__":
#     if "--debug" in sys.argv:
#         from run_tests import run_tests
#
#         run_tests()
#     else:
#         raw_input = parse_input(input(), os.path.abspath(__file__))