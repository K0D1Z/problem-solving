# Zadanie 1: Gra w kamienie 🌑
#
# Gramy w grę z kamieniami. W każdej turze wybieramy dwa najcięższe kamienie i uderzamy nimi o siebie nawzajem. Załóżmy, że dwa najcięższe kamienie mają wagi x i y oraz że x ≤ y. Oto możliwe wyniki zderzenia:
#
#     Jeśli x == y, to oba kamienie ulegają zniszczeniu.
#     Jeśli x! = y, to zniszczeniu ulega kamień o wadze x. Natomiast drugi kamień (ten który przed zderzeniem miał wagę y) zmienia swoją wagę na y − x.
#
# Gra kończy się gdy w grze pozostaje co najwyżej jeden kamień.
#
# Napisz program, który przyjmuje tablicę liczb całkowitych, w której pod i-tym indeksem zapisano wagę i-tego kamienia i zwraca wagę ostatniego pozostałego w grze kamienia.
#
# Jeśli gra zakończy się brakiem kamieni to program powinien zwrócić 0.
#
# Rozwiązanie powinno mieć złożoność O(nlogn). W tym celu zastosuj odpowiednie struktury danych poznane na lekcji.
#
# ⚠️ Określ czasową złożoność obliczeniową Twojego rozwiązania (wraz z uzasadnieniem) jako komentarz na początku implementowanej funkcji. ⚠️
#
# ✅ Przykład 1.:
# Wejście: 2 7 4 1 8 1
# Prawidłowe wyjście: 1
# Wyjaśnienie:
#
#     Zderzenie 7 i 8 powoduje powstanie kamienia o wadze 1.
#     Tablica zamienia się w [2 4 1 1 1].
#     Zderzenie 2 i 4 powoduje powstanie kamienia o wadze 2.
#     Tablica zamienia się w [2 1 1 1].
#     Zderzenie 2 i 1 powoduje powstanie kamienia o wadze 1.
#     Tablica zamienia się w [1 1 1].
#     Zderzenie 1 i 1 powoduje powstanie kamienia o wadze 0.
#     Tablica zamienia się w [1].
#
# ✅ Przykład 2.:
# Wejście: 2
# Prawidłowe wyjście: 2
#
# ✅ Przykład 3.:
# Wejście: 2 8
# Prawidłowe wyjście: 6


from typing import List, Tuple
from utils import parse_input
import os
import sys
from queue import PriorityQueue # domyślnie działa jak min-heap, dlatego będę musiał negować wagi, aby algorytm zadziałał

"""
Złożoność czasowa:
Przechodzimy po liście stones i wykonujemy operację put na kolejce priorytetowej.
Operacja put jest O(logn) zatem sumarycznie operacja dodawania elementów do
kolejki priorytetowej na początku jest O(nlogn).
Pętla while maksymalnie wykona się około n razy dla pesymistycznego przypadku oraz
n/2 razy dla przypadku optylistycznego. Wywołujemy dwa razy operację
get, która jest O(logn) i w ostatnim ifie jeszcze jeden raz. Ostatecznie złożoność
całego algorytmu asymptotycznie jest O(nlogn).
Złożoność pamięciowa:
Używam dodatkowej kolejki priorytetowej dodaję do niej n elementów - to jest max
ilość elementów, które będą w tej kolejce. Inne operacje na pamięci są stałe, zatem
ostateczna złożoność pamięciowa jest O(n)
"""
def lastStoneWeight(stones: List[int]) -> int:
    queue_len = 0 # zainicjuj zmienną liczącą rozmiar kolejki
    q = PriorityQueue() # inicjuję kolejkę priorytetową
    for i in stones: # przeiteruj całą tablicę stones
        q.put(-i) # wrzuć wagi kamieni tako krotka
        queue_len += 1
    while queue_len > 1: # dopóki w kolejce priorytetowej zostały co najmniej dwa elementy działaj dalej
        el1 = -q.get() # weź z kolejki element o największej wadze
        el2 = -q.get() # weź z kolejki element o drugiej największej wadze
        queue_len -= 2
        el3 = el1 - el2 # oblicz różnicę między wagą elementu maksymalnego a drugiego maksymalnego
        if el3 > 0: # jeżeli waga wynikowege elementu nie jest równa 0 to dodaj ten element do kolejki
            q.put(-el3)
            queue_len += 1
    # pętla się kończy
    if q.empty():
        return 0 # kolejka jest pusta, wszystkie kamienie zbiły swoje wagi, zwracamy 0
    return -q.get() # pozostał element, to jest to ostatni kamień, już więcej nie zbijemy tych kamieni dlatego zwracam wagę tego kamienia


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