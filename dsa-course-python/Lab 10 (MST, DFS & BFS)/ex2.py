# Zadanie 2: Dominacja na Miasteczku Studenckim
#
# Dana jest dwuwymiarowa macierz campus_grid reprezentująca fragment Miasteczka Studenckiego, gdzie dwie rywalizujące frakcje studentów walczą o wpływy. Na każdym polu siatki znajduje się student z jednej z dwóch rywalizujących drużyn:
#
#     1: Reprezentuje studenta z drużyny 1.
#     0: Reprezentuje studenta z drużyny 0.
#
# Każdy student stanowi węzeł w grafie i jest połączony krawędzią ze wszystkimi 8 studentami go otaczającymi (sąsiedztwo Moore'a).
#
# Celem drużyny 1 jest rozszerzanie swojego terytorium poprzez izolowanie graczy drużyny 0. Gracze 1 mogą odizolować daną ciągłą grupę graczy 0 jeżeli stworzą wokół nich otoczenie bez "dziur" . Oznacza to, że żaden gracz z tej odizolowanej grupy graczy 0 nie styka się z krawędzią macierzy campus_grid - nie da się otoczyć grupy graczy 0, która styka się z krawędzią planszy.
#
# Zadanie polega na zidentyfikowaniu wszystkich izolowanych regionów graczy 0 i zmianie ich na 1 (co oznacza, że Drużyna 1 skutecznie przejęła ten obszar i "przekonwertowała" graczy drużyny 0).
#
# W tym celu zaimplementuj funkcję solve_campus_domination(campus_grid: List[List[int]]) -> List[List[int]], która zwraca stan tablicy po dokonaniu przekonwertowania wszystkich odizolowanych graczy 0.
#
# 💡 Można dodawać własne funkcje pomocnicze.
#
# 💡Hint: Użyj DFS.
#
# ⚠️ Określ czasową złożoność obliczeniową Twojego rozwiązania (wraz z uzasadnieniem) jako komentarz na początku implementowanej funkcji. ⚠️
# Przykłady
#
# ✅ Przykład 1:
#
# Wejście:
#
# initial_campus_grid = [
#     [1, 1, 1, 1],
#     [1, 0, 0, 1],
#     [1, 1, 0, 1],
#     [1, 0, 1, 1]
# ]
#
# Prawidłowe wyjście:
#
# [[1, 1, 1, 1],
# [1, 0, 0, 1],
# [1, 1, 0, 1],
# [1, 0, 1, 1]]
#
# Wyjaśnienie:
#
# Grupa studentów z drużyny 0 nie zostaje odizolowana, gdyż student z drużyny '0' w lewym dolnym rogu znajduje się przy krawędzi kampusu, co uniemożliwia odizolowanie grupy.
#
# ✅ Przykład 2:
#
# Wejście:
#
# initial_campus_grid = [
#     [1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 0, 0, 0]
#     ]
#
# Prawidłowe wyjście:
#
# [[1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [0, 0, 1, 0, 0, 0]]
#
# Grupa studentów z drużyny 0 na środku planszy została odizolowana, natomiast studenci z drużyny 0 znajdujący się na dolnej krawędzi przetrwali.

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
Złożoność czasowa: dfs tak jak w poprzednim zadaniu może wywołać się 
co najwyżej 1 raz dla każdego indeksu -> O(i*j). Wywołujemy także
dwa razy pętle dla skrajnych wierszy i skrajnych kolumn: O(i) oraz O(j).
Na koniec przechodzimy po całym gridzie jeszcze raz O(i*j).
Asymptotycznie złożoność czasowa wyniesie zatem O(i*j), gdzie
i - liczba wierszy, j - liczba kolumn.

Złożoność pamięciowa: nie korzystamy z dodatkowych tablic o zmiennej długości
(dir_vertical i dir_horizontal i inne tablice pomocnicze 
stałe pamięciowo), w tablicy campus_grid tylko modyfikujemy elementy
wszystkie inne zmienne są stałe pamięciowo.
Jedyny narzut pamięciowy daje nam rekurencja, gdzie jednocześnie na stosie
wywołań rekurencyjnych może w najgorszym przypadku być i*j wywołań dfs, 
gdzie i - liczba wierszy, j - liczba kolumn - jest to np. przypadek 
gdy cały jeden wiersz składa się z samych zer - złożoność wyniesie O(i*j)
"""


def dfs(row: int, col: int, global_rows: int, global_cols: int, campus_grid: List[List[int]]) -> None:
    # jeżeli wyszliśmy poza krawędź albo natrafiliśmy na 1 to kończymy przeszukiwanie DFS
    if row < 0 or row >= global_rows or col < 0 or col >= global_cols:
        return
    if campus_grid[row][col] != 0:
        return
    # deklaruję stałą równą -1 przykładowo, która oznacza, że student 0 NIE zostanie zamieniony na 1
    campus_grid[row][col] = -1

    # odpalamy rekurencyjnie DFSa dla sąsiadujących indeksów listy
    dir_vertical = [-1, 0, 1]
    dir_horizontal = [-1, 0, 1]
    for i in dir_vertical:
        for j in dir_horizontal:  # te dwie pętle są stałe czasowo asymptotycznie
            if i == 0 and j == 0:
                continue
            dfs(row + i, col + j, global_rows, global_cols, campus_grid)


def solve_campus_domination(campus_grid: List[List[int]]) -> List[List[int]]:
    if not campus_grid:
        return []
    rows = len(campus_grid)
    cols = len(campus_grid[0])

    # tworzymy listę indeksów skrajnych kolumn i wierszy
    wall_cols_idx = [0, cols - 1]
    wall_rows_idx = [0, rows - 1]

    # najpierw sprawdzamy dwie skrajne kolumny w poszukiwaniu 0 przy krawędzi
    for i in range(rows):
        for j in wall_cols_idx:
            if campus_grid[i][j] == 0:  # znaleziono 0 przy krawędzi
                dfs(i, j, rows, cols, campus_grid)  # wyszukujemy sąsiadujące 0

    # potem sprawdzamy dwa skrajne wiersze górny i dolny w poszykiwaniu 0 przy krawędzi
    for i in wall_rows_idx:
        for j in range(cols):
            if campus_grid[i][j] == 0:  # znaleziono 0 przy krawędzi
                dfs(i, j, rows, cols, campus_grid)  # wyszukujemy sąsiadujące 0

    # teraz przechodzimy całą macierz jeszcze raz aby zamienić -1 na 0 a wszystko inne na 1
    for i in range(rows):
        for j in range(cols):
            if campus_grid[i][
                j] == -1:  # w poprzednich iteracjach studentów, ktorzy nie zostaną przejęci oznaczam jako -1
                campus_grid[i][
                    j] = 0  # przywracam 0 dla tych studentów, którzy sąsiadują z innymi studentami 0 i nie są otoczeni
            else:
                campus_grid[i][j] = 1  # w przeciwnym wypadku albo byli to studenci 1 albo studenci 0 zostali przejęci
    return campus_grid

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
