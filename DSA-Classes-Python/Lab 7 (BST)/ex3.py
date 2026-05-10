# Zadanie 3: Poprawne drzewo BST (3pkt)
#
# Na wejściu masz dany korzeń drzewa binarnego. Sprawdź czy dane drzewo binarne
# jest drzewem BST. W tym celu zaimplementuj metodę is_valid_BST(root: Optional[Node]),
# która przyjmuje korzeń drzewa binarnego i zwraca true jeżeli to drzewo jest BST oraz false w
# przeciwnym przypadku.
#
# Drzewo binarne jest drzewem BST, gdy dla każdego węzła w drzewie, wartość węzła
# est większa niż wartość wszystkich węzłów w jego lewym poddrzewie oraz mniejsza niż
# wartość wszystkich węzłów w jego prawym poddrzewie.

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


def evaluate(node: Optional[Node], low: int, high: int) -> bool:
    if node is None:  # przypadek bazowy, jeżeli dotrzemy do liścia, to dla jego dzieci zwracamy True po prostu, nie ma co porównywać
        return True
    if not (low < node.val < high):  # jeżeli wartość nie mieści się w sprawdzanym zakresie, to drzewo nie jest poprawne
        return False

    node_left_new_high = node_right_new_low = node.val  # oblicz nowe minimum i maksimum sprawdzanego zakresu

    # zachowujemy minima i maksima, aby pamiętać o wartościach największych i najmniejszych rodziców węzła
    return evaluate(node.left, low, node_left_new_high) and evaluate(node.right, node_right_new_low,
                                                                     high)  # rekurencyjnie wołamy funkcję evaluate z nowymi zakresami
    # jeżeli choćby jedno evaluate zwróci False,
    # to znaczy, że drzewo nie jest poprawne


def is_valid_BST(root: Optional[Node]) -> bool:
    return evaluate(root, float('-inf'), float(
        'inf'))  # dla roota górna i dolna granica to max i min wartość obsługiwana przez Python - nie ma ścisłych granic na razie

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
