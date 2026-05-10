# Zadanie 2 – Rozkład poziomów pewności do kubełków 🪣 (4 punkty)
#
# Posiadasz listę wyników pewności (confidence scores) wygenerowanych przez model AI. Wyniki zapisane są w tablicy scores jako liczby zmiennoprzecinkowe.
#
# Każdy wynik spełnia warunek:  0.0 ≤ scores[i] < 1.0
#
# Zaimplementuj funkcję:  bucket_scatter(scores:list[float]) która:
#
# 👉 tworzy dokładnie N kubełków (gdzie N = len(scores))
# 👉 przypisuje każdy element do odpowiedniego kubełka zgodnie z zasadą:
#
# Elementy w każdym kubełku muszą zachować kolejność ich występowania w tablicy wejściowej (tzn. przed sortowaniem).
# Przykład
#
# Wejście:
# scores = [0.79, 0.13, 0.16, 0.64, 0.39]
#
# Wyjście:
# [
#   [0.13, 0.16],
#   [0.39],
#   [],
#   [0.64],
#   [0.79]
# ]

from typing import List, Tuple
from utils import parse_input
import os
import sys
import math

"""
Złożoność czasowa algorytmu:
Wykonujemy 2 pętle, które przechodzą n razy, wszystkie inne operacje wykonują się
w czasie liniowym. Z tego powodu złożoność czasowa wyniesie O(n) - tak samo dla
notacji omega i theta.

Złożoność pamięciowa algorytmu: tworzymy dodatkową listę, która zawiera n kubełków, które
także są listami, do kubełków trafiają zawsze wszystkie elementy z listy scores
(mogą być różnie rozłożone - na kilka lub wszystkie kubełki lub równomiernie).
Niezależnie od rozkładu elementów, zawsze dopisujemy n wartości do kubełków. 
Z tego powodu złożoność pamięciowa wyniesie O(n) - tak samo dla notacji omega
i theta.
"""


def bucket_scatter(scores: list[float]):
    n = len(scores)
    B = [[] for _ in range(
        n)]  # inicjuję tablicę B-przechowujemy n pustych kubełków, do których następnie będziemy dodawać elementy listy scores
    for i in range(n):
        B[math.floor(n * scores[i])].append(scores[
                                                i])  # liczymy indeks kubełka, do którego trafi element, następnie appendujemy ten element do wybranego kubełka
    # zgodnie z poleceniem nie sortujemy list wewnątrz listy B
    return B  # po prostu zwracam listę B

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
