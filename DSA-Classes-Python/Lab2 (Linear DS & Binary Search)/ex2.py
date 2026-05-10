# Zadanie 2: Odwrotna Notacja Polska 🥟
#
# Napisz funkcję, która przyjmuję tablicę tokenów reprezentujących wyrażenia arytmetyczne zapisane w odwrotnej notacji polskiej i oblicza wartość przekazanego do niej wyrażenia.
#
# Uwagi:
#
#     tokenami mogą być liczby całkowite od -100 do 100, oraz operatory arytmetyczne: ’+’, ’*’, "/", "-",
#     w testowych oraz właściwych przypadkach nie zachodzi dzielenie przez zero,
#     lista tokenów reprezentuje poprawne wyrażenie w odwrotnej notacji polskiej,
#     wynik dzielenia powinien być zaokrąglany w kierunku zera, tj. należy pominąć jego część dziesiętną (np. 5.6 jest zaokrąglane do 5 a -5.6 jest zaokrąglane do -5)
#
# ✅ Przykład 1:
# Wejście: [2,1,+,3,*]
# Prawidłowe wyjście: 9
# Wyjaśnienie: ((2 + 1) * 3) = 9
#
# ✅ Przykład 2:
# Wejście: [4,13,5,/,+]
# Prawidłowe wyjście: 6
# Wyjaśnienie: (4 + (13 / 5)) = 6
#
# ✅ Przykład 3:
# Wejście: [10,6,9,3,+,-11,*,/,*,17,+,5,+]
# Prawidłowe wyjście: 22
# Wyjaśnienie: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22

from typing import List
from utils import parse_input
import os
import sys


# tworzę dodatkową klasę Stack dla wygody
class Stack:
    def __init__(self):
        self.stack = []  # O(1)

    def push(self, n):
        self.stack.append(n)  # O(1) - z dokumentacji pythona

    def pop(self):
        return self.stack.pop()  # O(1) - z dokumentacji pythona

    def size(self):
        return len(self.stack)  # O(1) - z dokumentacji pythona

    def top(self):
        return self.stack[-1]  # O(1)


'''
Złożoność czasowa algorytmu:
O(n), Ω(n), θ(n) - niezależnie od danych wejściowych jedyna pętla for w kodzie
wykona się n razy, gdzie n to długość przekazanej listy tokenów

Złożoność pamięciowa algorytmu:
O(n) - wrzucamy na stos (n - (n // 2) elementów, gdzie n // 2 to liczba 
operatorów w przekazanej liście tokenów. Z tego wynika, że złożoność pamięciowa
wynosi O(n). Dla optymistycznego przypadku złożoność pamięciowa jest stała 
(na stos dajemy tylko dwie wartości, z których liczymy wynik za pomocą operatora 
na trzecim miejscu listy tokenów), wynosi więc Ω(1).
W tych dwóch faktów nie możemy podać ogólnej złożoności pamięciowej w notacji θ.
Możemy to zrobić tylko dla konkretnego przypadku.

'''


def evalRPN(tokens: List[str]) -> int:
    stack = Stack()  # O(1)
    list_len = len(tokens)  # O(1)
    for i in range(list_len):  # pętla wykonująca się n razy
        token = tokens[i]  # n operacji
        if token not in ['-', '+', '/', '*']:  # n operacji
            stack.push(int(token))  # n operacji
        else:  # n operacji
            if stack.size() < 2:  # n operacji
                raise Exception("Podano nieprawidłowe wyrażenie ONP")  # 1 operacja
            operator = token  # n operacji
            number2 = stack.pop()  # n operacji
            number1 = stack.pop()  # n operacji
            if operator == '+':  # n operacji
                stack.push(number1 + number2)  # n operacji
            elif operator == '-':  # n operacji
                stack.push(number1 - number2)  # n operacji
            elif operator == '*':  # n operacji
                stack.push(number1 * number2)  # n operacji
            else:  # n operacji
                if number2 == 0:  # n operacji
                    raise Exception("Dzielenie przez zero")  # 1 operacja
                else:  # n operacji
                    stack.push(int(number1 / number2))  # n operacji
    return int(stack.top())  # 1 operacja

# Wniosek z analizy kodu -> złożoność czasowa O(n) (jedna pętla)

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
