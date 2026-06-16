# Zadanie 2:  Badanie systemu korzeniowego Miasteczka Studenckiego 🫚
#
# Miasteczko studenckie jest porośnięte drzewami posiadającymi rozległy system korzeni. System ten jest reprezentowany przez graf G, którego wierzchołki reprezentują drzewa, mogące łączyć się systemami korzeniowymi z innymi drzewami, co jest reprezentowane przez krawędzie grafu. Aby zbadać system korzeniowy miasteczka, studenci wybrali k drzew i wszczepili im k różnych gatunków grzybów numerowanych od
# 0 do k−1.
#
# W jednostce czasu grzyb może rozrastać się z drzewa na wszystkie, z którymi bezpośrednio łączy się korzeniami, ale które w poprzedniej jednostce czasu nie były opanowane przez żadnego grzyba. Jeśli dwa lub więcej gatunków grzyba docierają do (nieopanowanego) drzewa w tej samej jednostce czasu, wygrywa ten z najmniejszym indeksem i on opanowuje drzewo.
#
# Zadanie polega na zaimplementowaniu funkcji getCountOfInfectedTrees(G: List[List[int]], infectedTrees: [List[int], fungusNr: int) -> int, która wyznacza ile drzew zostanie ostatecznie opanowanych przez grzyb o numerze fungusNr. Funkcja przyjmuje następujące argumenty:
#
#     graf G w postaci list sąsiędztwa,
#     tablica infectedTrees zawierająca numery drzew, którym wszczepiono grzyby,
#     fungusNr - numer grzyba. Funkcja powinna zwrócić liczbę drzew opanowanych przez grzyb numer fungusNr.
#
# 💡 Można dodawać własne funkcje pomocnicze.
#
# ⚠️ Określ czasową złożoność obliczeniową Twojego rozwiązania (wraz z uzasadnieniem) jako komentarz na początku implementowanej funkcji. ⚠️
# Przykłady
#
# ✅ Przykład 1:
#
# Wejście:
#
# G = [[1,3],[0,2,4],[1,5],
#      [0,4,6],[1,3,5,7],[2,4,8],
#      [3,7],[4,6,8],[7,5]]
# infectedTrees = [8,2,6]
# fungusNr = 1
#
# Wyjście: 3
#
# Wyjaśnienie:
#
# Grzyb nr 0 zostaje wszczepiony do drzewa nr 8.
# Grzyb nr 1 zostaje wszczepiony do drzewa nr 2.
# Grzyb nr 2 zostaje wszczepiony do drzewa nr 6.
#
# Opanowane grzybem nr 1 będą drzewa: 0,1,2.

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
Złożoność czasowa: O(E + V), gdzie V to liczba wierzchołków, a E to liczba krawędzi
Każde drzewo trafia do listy BFS tylko jeden raz, kiedy zostaje zainfekowane. W pętli
potem przechodzimy po listach sąsiedztwa grafu G, co oznacza że każda liczba zostanie
sprawdzona stałą liczbę razy - max 2 razy. Operacje na słowniku next_ones
zajmuje O(1) średnio, a ostatnia pętla iteruje po tablicy o rozmiarze V

Złożoność pamięciowa: O(V), tablica fungus_list ma rozmiar V, każda inna
struktura danych także ma maksymalnie rozmiar V w najgorszym rozmiarze.
"""


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    vertices = len(G)  # liczba wierzchołków
    fungus_list = [-1] * vertices  # przechowujemy indeks grzyba, który opanował pierwszy dany wierzchołek
    # inicjujemy fungus list oraz listę przeszukiwania BFS
    bfs = []
    for i, j in enumerate(infectedTrees):
        fungus_list[j] = i
        bfs.append(j)

    # symulacja kolejnych iteracji procesu
    while bfs:
        next_ones = {}
        for i in bfs:
            current_fungus = fungus_list[i]
            for j in G[i]:
                if fungus_list[j] == -1:  # wybieramy tylko nieopanowane jeszcze drzewa
                    if j not in next_ones:  # jeżeli grzyb nie jest w kolejce kandydatów do zarażenia w tej iteracji, to dodajemy go do kolejki
                        next_ones[j] = current_fungus
                    else:  # grzyb jest już w kolejce, wygrywa grzyb z mniejszym indeksem
                        if current_fungus < next_ones[j]:
                            next_ones[j] = current_fungus
        next_bfs = []
        for tree, fungus in next_ones.items():
            fungus_list[tree] = fungus
            next_bfs.append(tree)
        bfs = next_bfs

    # zliczam drzewa ostatecznie opanowane przez poszukiwany gatunek grzyba
    count = 0
    for x in fungus_list:
        if x == fungusNrToCount:
            count += 1

    return count


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