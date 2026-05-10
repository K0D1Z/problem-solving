# Zadanie 2: Kompresja listy przez eliminację oscylacji 🔁
#
# Masz daną jednokierunkową listę wiązaną liczb całkowitych, gdzie węzeł jest zdefiniowany przez poniższą strukturę:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Twoim zadaniem jest usunąć wszystkie fragmenty listy, w których wartości tworzą
# lokalne „oscylacje”, czyli wzór:
#
# a → b → c, gdzie:
# (a < b > c) lub (a > b < c)
#
# Innymi słowy: środkowy element jest lokalnym maksimum lub minimum.
#
# Usuwamy tylko środkowy element, ale operację powtarzamy tak długo,
# aż lista przestanie zawierać takie wzorce.
#
# Funkcja powinna zwrócić głowę zmodyfikowanej listy.
#
#
# Sygnatura funkcji:
#
# def remove_oscillations(head: Optional[ListNode]) -> Optional[ListNode]
#
# Podaj złożoność czasową zaproponowanego rozwiązania w komentarzu.
#
# Przykład 1
#
# Wejście: 1 → 3 → 2 → 4 → 3
#
# Kroki:
#
# 1 → 3 → 2 → 4 → 3
#       ↑
#       usuń 3
#
# 1 → 2 → 4 → 3
#         ↑
#         usuń 4
#
# 1 → 2 → 3
#
# Wyjście: 1 → 2 → 3
#
# Przykład 2
#
# Wejście:
#
# 5 → 3 → 4 → 2 → 1
#
# Wyjście:
#
# 5 → 3 → 2 → 1
#
# Przykład 3
#
# Wejście: 1 → 2 → 3 → 4
#
# Wyjście: 1 → 2 → 3 → 4
#
# (brak oscylacji)

from typing import List, Tuple, Optional
from utils import parse_input, ListNode
import os
import sys

"""

Złożoność czasowa algorytmu:
W algorytmie zawsze przynajmniej raz przechodzimy przez całą listę
w drugiej pętli while, w najlepszym przypadku pierwsza pętla while wykona się 
tylko raz (gdy w liście od początku nie było oscylacji) - wtedy złożoność 
optymistyczna to Ω(n). Dla najgorszego przypadku pierwsza pętla while zostanie
wywołana n - 2 razy - po usunięciu oscylacji w pierwszym przebiegu wewnętrznej
pętli powstaną nowe oscylacje; zatem złożoność w pesymistycznym przypadku 
wyniesie O(n^2). Ze względu na różnice w notacjach O oraz Ω nie można wyznaczyć
złożoność czasową w notacji θ dla ogólnego przypadku.

Złożoność pamięciowa algorytmu:
Nie operujemy na tablicach i nie wywołujemy rekurencyjnie funkcji - używamy
jedynie pojedynczych kopii wskaźników - złożoność pamięciowa zatem to θ(1).

"""


def removeOscillations(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:  # jeżeli w liście nie ma elementów, nie badamy oscylacji
        return head
    if head.next is None:  # jeżeli w liście jest tylko jeden element, nie badamy oscylacji
        return head

    # dla listy dwóch elementów pierwsza pętla while nie wykona się i zostanie
    # zwrócona głowa - nie badamy oscylacji dla dwóch elementów listy

    is_oscillation_found = True  # zakładamy, że w liście są oscylacje
    while is_oscillation_found:  # powtarzamy procedurę jeżeli w poprzednim przejściu pętli znaleziono oscylację
        is_oscillation_found = False  # na razie nie znaleziono oscylacji
        ptr = head  # tworzymy kopię wskaźnika na head
        while ptr.next.next != None:  # powtarzamy pętlę, dopóki drugi sąsiad naszego wskaźnika nie jest NULL
            a = ptr  # tworzymy kopię wskaźnika oraz jego dwóch sąsiadów (dla czytelności kodu)
            b = ptr.next
            c = ptr.next.next
            if a.val < b.val > c.val or a.val > b.val < c.val:  # sprawdzamy, czy b jest lokalnym ekstremum
                ptr.next = ptr.next.next  # jeżeli b jest rzeczywiście lokalnym ekstemum, to zmieniamy sąsiada wskaźnika
                is_oscillation_found = True  # znaleziono oscylację - powtarzamy procedurę jeszcze raz
            else:
                ptr = ptr.next  # jeżeli nie znaleźliśmy ekstremum, to przypisujemy ptr jego sąsiada
    return head  # zwracamy głowę (nie jest możliwe usunięcie pierwszego elementu listy)

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
