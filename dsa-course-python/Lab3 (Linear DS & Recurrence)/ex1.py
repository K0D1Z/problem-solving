# Zadanie 1 – Symulator systemu plików 📁 (4 punkty)
#
# Napisz funkcję  def file_system_simulator(commands: List[str]) -> str
# , która przetwarza listę poleceń nawigacji po systemie plików i zwraca
# aktualną ścieżkę bezwzględną po wykonaniu wszystkich poleceń.
#
#
# Określ złożoność czasową i pamięciową swojego rozwiązania w komentarzu - jeżeli jest to możliwe użyj notacji Theta.
#
# Symulowany system plików zaczyna się w katalogu głównym "/".
#
# Polecenia mogą być następujące:
#
#     "cd <nazwa_katalogu>" — przejdź do podkatalogu
#     "cd .." — przejdź do katalogu nadrzędnego
#     "pwd" — zwróć aktualną ścieżkę bezwzględną
#
#
# Nazwy katalogów zawierają tylko małe litery i nie zawierają znaku "/".
#
# Jeśli aktualny katalog to katalog główny "/", wykonanie "cd .." powinno pozostawić Cię w "/".
#
# Podczas budowania ścieżki:
#
#     Katalogi powinny być oddzielone znakiem "/".
#     Katalog główny powinien być reprezentowany jako "/".
#     Końcowa ścieżka nie powinna zawierać końcowego ukośnika, chyba że jest to katalog główny.
#
#
#
# Przykład 1
# Wejście: ["cd home", "cd student", "pwd"]
#
# Wyjście: "/home/student"
#
# Wyjaśnienie:
#
# Start w "/"
#
# cd home → "/home"
#
# cd student → "/home/student"
#
# pwd zwraca "/home/student"
#
#
#
# Przykład 2
# Wejście: ["cd home", "cd student", "cd projects", "cd ..", "pwd"]
#
# Wyjście: "/home/student"
#
# Wyjaśnienie:
#
# Start w "/"
#
# cd home → "/home"
#
# cd student → "/home/student"
#
# cd projects → "/home/student/projects"
#
# cd .. → "/home/student"
#
# pwd zwraca "/home/student"
#
#
#
# Przykład 3
# Wejście: ["cd home", "cd ..", "cd ..", "pwd"]
#
# Wyjście: "/"
#
# Wyjaśnienie:
#
# Start w "/"
#
# cd home → "/home"
#
# cd .. → "/"
#
# cd .. → nadal "/"
#
# pwd zwraca "/"
#
#
# Wskazówka: użyj stosu

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""

Złożoność czasowa algorytmu: 
O(n^2) - przechodzimy przez listę commands zawsze n razy, gdzie n to rozmiar 
listy; w najgorszym przypadku wchodzimy coraz głębiej w strukturę katalogów
(nie używając komendy cd ..) przez co przy wywołaniu komendy pwd na stosie 
będzie n - 1 elementów - pętla wewnętrzna, która służy do konkatenacji ścieżki
przejdzie zatem n - 1 razy. W najlepszym przypadku złożoność czasowa wynosi
Ω(1) (na stosie nie ma żadnego elementu, pętla wykona się tylko raz)
Nie możemy zatem wyciągnąć złożoności pamięciowej w notacji θ.


Złożoność pamięciowa algorytmu:
O(n) - w najgorszym przypadku wchodzimy coraz głębiej w strukturę katalogów
(nie używając komendy cd ..) - przy wywołaniu komendy pwd na stosie będzie 
n - 1 elementów; w najlepszym przypadku na stosie nie wrzucamy żadnego elemenu -
od razu wywołujemy komendę pwd; w takim przypadku złożoność pamięciowa to
Ω(1) - nie możemy zatem wyciągnąć złożoności pamięciowej w notacji θ.

"""


def file_system_simulator(commands: List[str]) -> str:
    stack = []
    for i in commands:
        words = i.strip().split()
        if words[0] == 'cd':
            if words[1] == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(words[1])
        elif words[0] == 'pwd':
            path = ''
            for j in stack:
                path = path + '/' + j
            return path

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
