# Zadanie 1: Scalanie drzew 🖇️
#
# Mając dane 2 korzenie drzew binarnych root1 i root2, zwróć scalone drzewo. W tym celu zaimplementuj metodę merge_trees(root1: Optional[Node], root2: Optional[Node])-> Optional[Node], która przyjmuje dwa korzenie i zwraca korzeń scalonego drzewa.
#
# Przebieg procesu scalania:
#
# Wyobraź sobie, że umieszczasz drzewa root1 i root2 jedno na drugim. Niektóre węzły obu drzew się pokryją, podczas gdy inne nie. Zadanie polega na scaleniu obu drzew w nowe drzewo binarne. Zasada scalania jest taka, że jeśli dwa węzły się pokrywają, to wartości węzłów się sumują jako nowa wartość scalonego węzła. W przeciwnym razie zostanie użyty niepusty węzeł jako węzeł nowego drzewa. Proces scalania musi się rozpocząć od korzeni obu drzew.
#
# Przykład 1:
#
# Drzewo 1      Drzewo 2      Scalone Drzewo
#     1             2              3
#    / \           / \            / \
#   3   2         1   3          4   5
#  /               \   \        / \   \
# 5                 4   7      5   4   7
#
# Przykład 2:
#
# Drzewo 1      Drzewo 2      Scalone Drzewo
#     0             2              2
#    /             / \            / \
#   3            -3   3          0   3
#  /                            /
# 5                            5



from typing import Optional
from utils import Node, parse_input
import sys, os

"""
Złożoność czasowa:
O(n) - gdzie n to liczba pokrywających się ze sobą węzłów w obu drzewach
Następuje rekurencyjny podział problemu na prostsze do rozwiązania podproblemy, których jest w sumie n.

Złożoność pamięciowa:
O(logn) dla przeciętnego przypadku z własności drzewa,
O(n) dla jednego z drzew zdegradowanego do listy jednokierunkowej
Pamięć jest zużywana tylko na wywołania rekurencyjne - wszystkie operacje w funkcji są stałe pamięciowo
"""


def merge_trees(root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
    if root1 is None:  # przypadki bazowe, jeżeli jeden z Node'ów jest None to zwracam ten drugi (niezależnie czy też jest None)
        return root2
    if root2 is None:
        return root1

    # jeżeli oba Node'y nie były None, to merguję wartości obu Node'ów tworząc nowy
    root = Node(root1.val + root2.val)

    root.left = merge_trees(root1.left,
                            root2.left)  # rekurencyjnie wywołuję funkcję dla lewego i prawego poddrzewa roota
    root.right = merge_trees(root1.right, root2.right)

    return root  # zwracam roota (zostanie on przypisany do left albo right w poprzednich wywołaniach rekurencyjnych, odtwarzając drzewo bottom-up)


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