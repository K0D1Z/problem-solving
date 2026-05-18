# Dany jest korzeń drzewa BST root oraz wartości dwóch węzłów znajdujących się w tym drzewie (p i q). Znajdź najniższego wspólnego przodka węzłów p i q.
#
# W tym celu zaimplementuj metodę get_lowest_common_ancestor(root: Optional[Node], p: int, q: int) -> int, która zwróci wartość najniższego wspólnego przodka dla węzłów o wartościach p i q.
#
# Najniższy wspólny przodek między dwoma węzłami p i q jest najniższym węzłem w drzewie, który ma zarówno p, jak i q jako potomków. Zakładamy, że węzeł może być potomkiem samego siebie.
#
# Przyjmij, że następujące założenia są spełnione:
#
#     wszystkie wartości węzłów w drzewie root są unikatowe
#     drzewo root zawiera wartości p i q
#     p ≠ q
#
# Przykład 1:
#
# p = 2, q = 8
# root:
#          6
#       /    \
#      2      8
#     / \    / \
#    0   4  7   9
#       / \
#      3   5
#
# Output: 6
# Najniższy wspólny przodek węzłów 2 i 8 to węzeł 6.
#
# Przykład 2:
#
# p = 1, q = 6
# root:
#          5
#       /    \
#      3      8
#     / \    / \
#    2   4  7   9
#       / \
#      1   6
#
# Output: 4
# Najniższy wspólny przodek węzłów 1 i 6 to węzeł 4.
#
# Przykład 3:
#
# p = 1, q = 4
# root:
#          5
#       /    \
#      3      8
#     / \    / \
#    2   4  7   9
#       / \
#      1   6
#
# Output: 4
# Wyjaśnienie: Najniższy wspólny przodek węzłów 1 i 4 to węzeł 4.

from typing import Optional, List
from utils import Node, parse_input
import sys, os

"""
Pierwsze intuicyjne rozwiązanie, poniżej zakomentowane rozwiązanie
optymalne wykorzystujące właściwości BST

Złożoność czasowa rozwiązania:
O((n + m + + n + m n*m) asymptotycznie O(n*m) - gdzie n to liczba węzłów do pokonania w celu znalezienia wartości p
a m to liczba węzłów do pokonania w celu znalezienia wartości q - w najgorszym przypadku
pętle while będą musiały przejść po całym drzewie, które jest zdegenerowane do listy jednokierunkowej.
Analogicznie przy porównywaniu listy przodków koszt pętli for będzie wynosił
O(n*m) przy operowaniu na listach pythonowych i wykorzystaniu operacji in.

Złożoność pamięciowa rozwiązania:
O(n + m) gdzie n to liczba przodków elementu q, a m to liczba przodków elementu p
Wykorzystuję tutaj dwie pomocnicze tablice do przechowywania wartości przodków elementów,
co zwiększa złożoność pamięciową rozwiązania - asymptotycznie jest to złożonośc liniowa
"""


def get_lowest_common_ancestor(root: Optional[Node], p: int, q: int) -> int:
    # z warunku, że drzewo root zawiera p i q nie muszę się martwić o wartości None
    # analogicznie, ponieważ drzewo zawiera unikatowe wartości, to pierwszy wspólny element list to nasz szukany przodek

    # znajdź p i stwórz listę jego przodków (które musiałem przejść, żeby dostać się do p)
    p_node = root
    p_ancestors = []

    p_ancestors.append(p_node.val)
    while p_node.val != p:
        if p_node.val > p:
            p_node = p_node.left
        elif p_node.val < p:
            p_node = p_node.right
        p_ancestors.append(p_node.val)

    # znajdź q i stwórz listę jego przodków (które musiałem przejść, żeby dostać się do q)
    q_node = root
    q_ancestors = []
    q_ancestors.append(q_node.val)
    while q_node.val != q:
        if q_node.val > q:
            q_node = q_node.left
        elif q_node.val < q:
            q_node = q_node.right
        q_ancestors.append(q_node.val)

    # znajdź pierwszy wspólny element dla obu list - poszukujemy OD KOŃCA LISTY - dlatego muszę je odwrócić
    p_ancestors.reverse()  # złożoność liniowa (O(n))
    q_ancestors.reverse()  # złożoność liniowa (O(m))
    for value in p_ancestors:  # pętla dla n elementów
        if value in q_ancestors:  # złożoność liniowa (O(m))
            return value
    return None


# """
# Optymalne rozwiązanie: O(h) czasowo i O(1) liniowo
# """
# def get_lowest_common_ancestor(root: Optional[Node], p: int, q: int) -> int:
#     current = root

#     while current is not None:
#         if p < current.val and q < current.val:
#             current = current.left
#         elif p > current.val and q > current.val:
#             current = current.right
#         else:
#             # Ścieżki do p i q się rozwidlają lub current.val to p lub q
#             return current.val
#     return None

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