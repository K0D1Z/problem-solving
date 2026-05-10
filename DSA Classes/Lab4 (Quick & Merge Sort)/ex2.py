# Zadanie 2 - Scalanie list z sumowaniem duplikatów 🧩 (4 punkty)
#
# Zaimplementuj funkcję:
#
# def merge_sum_duplicates(l1: Optional[Node], l2: Optional[None]) -> Optional[Node]:
#
# która scala dwie posortowane rosnąco listy jednokierunkowe, tworząc nową listę, w której:
#
#     elementy są posortowane rosnąco
#     jeśli dana wartość występuje w obu listach (lub wielokrotnie), to wszystkie jej wystąpienia są sumowane do jednego elementu
#
# Przykłady
# Przykład 1
#
# l1: 1 → 2 → 2 → 3
# l2: 2 → 3 → 3 → 4
#
# wynik:
# 1 → 6 → 9 → 4
#
# Wyjaśnienie:
#
#     1 → 1×1 = 1
#     2 → (2+1)=3 razy → 2×3 = 6
#     3 → (1+2)=3 razy → 3×3 = 9
#     4 → 4×1 = 4
#
# Przykład 2
#
# l1: 5 → 5 → 5
# l2: 5 → 5
#
# wynik:
# 25

from typing import Optional
from utils import parse_input, ListNode  # dodałem brakujący import ListNode
import os
import sys

'''
Złożoność czasowa algorytmu:
O(n + m) - gdzie n i m to długości przekazanych list jednokierunkowych;
niezależnie od przypadku musimy przejść przez elementy obu list, zatem asymptotycznie
złożoności to odpowiednio O(n), Ω(n), θ(n)

Złożoność pamięciowa algorytmu:
O(n + m) - w pesymistycznym przypadku nie ma elementów, które powtarzają się
zarówno w liście pierwszej i drugiej - w obu listach są tylko i wyłącznie
unikalne wartości; w takim przypadku trzeba stworzyć n + m nowych ListNode'ów 
dla wynikowej listy, gdzie n i m to długości przekazanych list; asymptotycznie
złożoność pamięciowa dla przypadku pesymistycznego jest zatem liniowa
Ω(1) - w optymistycznym przypadku tworzymy tylko jeden nowy ListNode - w obu
listach wszystkie elementy są takie same, zatem dodajemy do listy wynikowej tylko
jeden element; 
Nie można określić złożoności  θ dla ogólnego przypadku
'''


def merge_sum_duplicates(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ptr1 = l1  # wskaźnik na elementy pierwszej listy
    ptr2 = l2  # wskaźnik na elementy drugiej listy
    new_list = ListNode()  # nowa lista docelowo zawierająca wynik
    head = new_list  # wskaźnik na głowę nowej listy

    while ptr1 is not None or ptr2 is not None:  # pętla działa, dopóki oba wskaźniki nie są None
        if ptr1 is not None and ptr2 is not None:  # jeżeli oba wskaźniki nie są None, to wybieramy minimalną wartość
            current_val = min(ptr1.val,
                              ptr2.val)  # przechowujemy wartość do sprawdzania ilości jej wystąpień w obu listach
        elif ptr1 is not None:  # jeżeli drugi wskaźnik jest None, to pracujemy na elementach listy pierwszej
            current_val = ptr1.val  # jeżeli pierwszy wskaźnik jest None, to pracujemy na elementach listy drugiej
        else:
            current_val = ptr2.val

        counter = 0  # licznik wystąpień danej wartości w obu listach
        while ptr1 is not None and ptr1.val == current_val:  # pętla wynonuje się dopóki pierwszy wskaźnik nie jest None i
            counter += 1  # jego wartość jest równa sprawdzanej wartości current_val
            ptr1 = ptr1.next

        while ptr2 != None and ptr2.val == current_val:  # analogiczna pętla dla drugiej listy
            counter += 1
            ptr2 = ptr2.next

        new_node = ListNode()  # tworzymy nowy ListNode
        new_node.val = counter * current_val  # wartość nowego ListNode'a to iloczyn obecnie sprawdzanej wartości z liczbą wystąpień tej wartości
        new_list.next = new_node  # aktualizujemy następny element listy do zwrócenia
        new_list = new_list.next  # aktualizujemy wskaźnik na ogon listy

    return head.next  # zwracam następny element głowy, ponieważ pierwszy element listy miał val równe 0 (domyślnie)

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
