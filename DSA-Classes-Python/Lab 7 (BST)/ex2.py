# Zadanie 2 (4pkt)
#
# Mając podane dwa korzenie reprezentujące dwa drzewa binarne (root and subRoot), sprawdź czy subRoot jest poddrzewem root. W tym celu zaimplementuj 2 funkcje:
#
#     is_subtree(root: Optional[Node], subRoot: Optional[Node]) - zwraca true jeżeli subRoot jest poddrzewem root, w przeciwnym razie zwraca false.
#     is_same_tree(p: Optional[Node], q: Optional[Node])- zwraca true jeżeli drzewa p i q są identyczne
#
# Drzewo binarne z korzeniem w węźle subRoot jest poddrzewem drzewa binarnego z korzeniem w węźle root, jeśli subRoot jest węzłem w tym drzewie i wszystkie węzły z poddrzewa z korzeniem w subRoot są także węzłami w poddrzewie z korzeniem w root, oraz kolejność, struktura i wartości węzłów są zachowane. Innymi słowy, subRoot musi być węzłem w drzewie root, a każdy węzeł w poddrzewie z korzeniem w subRoot musi być również węzłem w poddrzewie z korzeniem w root. Przyjmij, że drzewo binarne jest poddrzewem samego siebie.
#
# Przykład 1:
#
# Drzewo root:
#
#         1
#        / \
#       2   3
#           /
#          4
#
# Drzewo subRoot:
#
#       3
#      /
#     4
#
# W pierwszym przypadku, subRoot jest poddrzewem root, ponieważ wszystkie węzły z poddrzewa subRoot są zawarte w drzewie root.
#
# Przykład 2:
#
# Drzewo root:
#
#         1
#        / \
#       2   3
#           /
#          4
#
# Drzewo subRoot:
#
#       3
#      / \
#     4   5
#
# W drugim przypadku, subRoot nie jest poddrzewem root, ponieważ węzeł 5 z drzewa subRoot nie jest zawarty w poddrzewie root.
#
# Przykład 3:
#
# Drzewo root:
#
#         1
#        / \
#       2   3
#           /\
#          4  5
#         /
#        6
#
# Drzewo subRoot:
#
#       3
#      / \
#     4   5
#
# W trzecim przypadku, subRoot nie jest poddrzewem root, ponieważ węzeł 6 z drzewa root nie jest zawarty w poddrzewie subRoot.
#
# Dwa drzewa binarne są identyczne, gdy mają te same struktury oraz każdy odpowiadający sobie węzeł ma taką samą wartość. Innymi słowy, drzewa muszą mieć te same wartości w każdym węźle i muszą być zbudowane w dokładnie takiej samej strukturze.
#
# Przykładem dwóch identycznych drzew binarnych jest:
#
# Drzewo 1:                Drzewo 2:
#     1                         1
#    / \                       / \
#   2   3                     2   3
#
# Oba drzewa mają te same wartości w węzłach (1, 2 i 3) oraz identyczną strukturę (korzeń z dwoma dzieci).

from typing import Optional
from utils import Node, parse_input
import sys, os

"""
Złożoność czasowa:
- Dla funkcji is_same_tree: O(N), gdzie N to liczba węzłów w drzewie o mniejszej 
liczbie węzłów (N razy wywołujemy rekurencyjnie funkcję o asymptotycznie stałej złożoności)
- Dla funkcji is_subtree: asymptotycznie O(N * M), gdzie N i M to liczba 
węzłów w drzewach (wywołujemy funkcję is_same_tree N razy), pesymistycznie obie struktury to 
bardzo długie ścieżki z takimi samymi wartościami, ale różniące się dopiero na samym końcu.

Złożoność pamięciowa:
- Dla funkcji is_same_tree: O(H), gdzie H to wysokość drzewa o mniejszej wysokości
(na stosie w jednym momencie będzie maksymalnie H ramek wywołań rekurencyjnych funkcji)
- Dla funkcji is_subtree: O(H_root + H_subRoot)
"""


def is_same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
    if p is None and q is None:  # jeżeli doszliśmy do momentu, w którym p i q są None,
        return True  # zwracamy prawdę (bo dwa Node'y są identyczne)

    if p is None or q is None or p.val != q.val:  # jeżeli jeden z elementów nie jest None (bo nie przeszedł pierwszego ifa)
        return False  # lub wartości elementów są różne, zwracamy fałsz
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)  # wywołujemy funkcję rekurencyjnie dla
    # lewych i prawych poddrzew p i q (ostateczie funkcja zwróci prawdę),
    # tylko gdy WSZYSTKIE wywołania rekurencyjne zwrócą prawdę


def is_subtree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    if root is None:  # jeżeli nasz root jest None, to subRoot na pewno
        return False  # nie jest poddrzewem, zwracamy Fałsz
    if subRoot is None:  # jeżeli nasz subRoot jest None, to jest oN poddrzewem
        return True  # każdego drzewa, zwracamy prawdę

    if is_same_tree(root, subRoot):  # jeżeli root i subRoot to te same drzewa - zwróć prawdę
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)
    # sprawdzamy, czy lewe LUB prawe poddrzewo roota jest takie samo tak subRoot

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
