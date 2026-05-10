# Zadanie 4. Dane jest drzewo binarne o korzeniu root oraz liczba całkowita target.
# Zwróć true, jeśli istnieje taka ścieżka w tym drzewie od korzenia do liścia, taka że
# suma wszystkich wartości wzdłuż tej ścieżki jest równa target. W tym celu zaimplementuj
# metodę has_path_sum(root: Optional[Node], target: int) -> bool, która dla danych root oraz
# target zwróci true jeżeli taka ścieżka istnieje oraz false w przeciwnym wypadku.
#
# Przykład 1:
#
# target = 22
# root:
#
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1
#
# Output: true
#
# Ścieżka: 5 -> 4 -> 11 -> 2
# Suma wartości na tej ścieżce wynosi 22, co odpowiada wartości target.
#
# Przykład 2:
#
# target = 5
# root:
#     1
#    / \
#   2   3
#
# Output: false
# W drzewie nie ma żadnej ścieżki od korzenia do liścia, której suma wartości wynosiłaby 5.
#
# Przykład 3:
#
# target = 38
# root:
#      3
#     / \
#    9  20
#      /  \
#     15   7
#
# Output: true
# Ścieżka: 3 -> 20 -> 15
# Suma wartości na tej ścieżce wynosi 38, co odpowiada target.

from typing import Optional
from utils import Node, parse_input
import sys, os

"""
Złożoność czasowa:
O(N), gdzie N to liczba węzłów - funkcja jest wywoływana rekurencyjnie dla każdego
node'a, a złożoność operacji jest stała asymptotycznie w samej funkcji.
Złożoność pamięciowa:
O(H), gdzie H to wysokość drzewa - jest to maksymalna liczbą ramek wywołań rekurencyjnych
funkcji na stosie
"""


def has_path_sum(root: Optional[Node], target: int, sum_=0) -> bool:
    if root is None:
        return False
    new_sum_ = root.val + sum_
    if target == new_sum_ and root.left is None and root.right is None:
        return True
    return has_path_sum(root.left, target, new_sum_) or has_path_sum(root.right, target, new_sum_)

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
