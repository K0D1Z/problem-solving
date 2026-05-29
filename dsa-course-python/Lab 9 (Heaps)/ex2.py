# Zadanie 2: Minimalna liczba cykli procesora 💻
#
# Na wejściu do programu otrzymujesz minimalną długość przerwy n wyrażoną w liczbie cykli procesora oraz tablicę zadań do wykonania. Zadania są reprezentowane przez litery od A do Z. Wykonanie każdego zadania trwa jeden cykl procesora. Zadania mogą być wykonane w dowolnej kolejności, ale pomiędzy każdymi dwoma wykonaniami tego samego zadania musi upłynąć co najmniej n cykli procesora. Innymi słowy: między dwoma zadaniami reprezentowanymi przez tę samą literę musi znaleźć się conajmniej n cykli odstępu, w czasie których mogą być wykonywane zadania oznaczone innymi literami.
#
# Program powinien zwracać minimalną liczbę cykli wymaganych do wykonania wszystkich zadań. Na wejściu podawana jest dodatnia liczba całkowita n reprezentująca czas chłodzenia oraz ciąg liter od A do Z oddzielonych spacjami (litery od A do Z bez polskich znaków) reprezentujących zadania do wykonania.
#
# ✅ Przykład 1.:
# Wejście: 2 A A A B B B
# Wyjście: 8
# Wyjaśnienie: n = 2, możliwa sekwencja to: A -> B -> przerwa -> A -> B -> przerwa -> A -> B.
#
# Po ukończeniu zadania A trzeba odczekać dwa cykle zanim znowu będzie można wykonać zadanie A. To samo dotyczy zadania B. W trzecim cyklu nie można wykonać ani zadania A, ani zadania B, więc trzeba wstrzymać prace. Po czwartym cyklu można znowu wykonać zadanie A, ponieważ upłynęły już dwa cykle procesora od poprzedniego wykonania zadania A.
#
# ✅ Przykład 2.:
# Wejście: 1 A C A B D B
# Wyjście: 6
# Wyjaśnienie: n = 1, możliwa sekwencja to: A -> B -> C -> D -> A -> B.
#
# Z czasem chłodzenia równym 1, można powtarzać zadanie po wykonaniu dowolnego innego zadania.
#
# ✅ Przykład 3.: Wejście: 3 A A A B B B
# Wyjście: 10
# Wyjaśnienie: Możliwa sekwencja to: A -> B -> przerwa -> przerwa -> A -> B -> przerwa -> przerwa -> A -> B.
#
# Są tylko dwa rodzaje zadań, A i B, które muszą być oddzielone przez 3 cykle. To prowadzi do dwukrotnego oczekiwania pomiędzy powtórzeniami tych zadań
#
# ⚠️ Określ czasową złożoność obliczeniową Twojego rozwiązania (wraz z uzasadnieniem) jako komentarz na początku implementowanej funkcji. ⚠️

from typing import List, Tuple
from utils import parse_input
import os
import sys
from collections import defaultdict

"""
Złożoność czasowa rozwiązania:
Iteruję po liście tasków o długości n - O(n) koszt
dict.values to O(n), tak samo dict.keys() oraz dict.items()
set() oraz sum() też O(n)
Stworzenie listy ready_task w pętli while która wykona się m razy
zajmie w najgorszym przypadku m, dalej też mamy operacje o koszcie O(m)
Sumarycznie asymptotycznie rozwiązanie zajmie O(n*m) (n - liczba zadań, m - liczba unikalnych zadań)
co nie jest optymalnym rozwiązaniem (ale działa :D)

Złożoność pamięciowa rozwiązania:
O(n) - tworzę dwa nowe słowniki oraz listę o długości n gotowych tasków,
asymptotycznie daje to nadal O(n), reszta zmiennych ma złożoność stałą
n to tutaj liczba unikalnych zadań a ponieważ alfabet jest skończony to
złożoność pamięciowa jest stała ??? czyli ostatecznie O(1) (chyba)
"""


def leastInterval(tasks: List[str], n: int) -> int:
    d = defaultdict(int)
    break_time = defaultdict(int)
    time_spent = 0
    for i in tasks:  # zmapuj ile razy i jakie taski są do zrobienia
        d[i] += 1
        break_time[i] = 0
    flag = set(d.values())
    while sum(d.values()) > 0:  # pętla wykonuje się dopóki jest do zrobienia jakiś task jeszcze
        ready_tasks = [key for key, value in break_time.items() if value == 0 and d[key] > 0]
        if not ready_tasks:  # robimy przerwę, jeżeli każdy element musi czekać
            time_spent += 1
        else:  # w przeciwnym wypadku wykonujemy zadanie i dodajemy przerwę czasową dla kolejnego wykonania tego zadania
            current_task = max(ready_tasks, key=lambda x: d[x])
            d[current_task] -= 1
            break_time[current_task] = n + 1  # jedynkę dodaję bo zaraz ją odejmę w kolejnym etapie
            time_spent += 1
        for i in break_time.keys():
            if break_time[i] > 0:  # usuń o 1 czas oczekiwania tylko jak jest większy od 0
                break_time[i] -= 1
    return time_spent


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