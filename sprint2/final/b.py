# -- ПРИНЦИП РАБОТЫ --

# Калькулятор работает на основе стека. Для вычисления значения
# выражения, записанного в обратной польской нотации, выражение
# считывается слева направо.

# Если на вход подан операнд, он помещается на вершину стека. Если на
# вход подан знак операции, то эта операция выполняется над двумя
# значениями, взятыми из стека в порядке добавления. Результат
# выполненной операции помещается на вершину стека. Действие
# продолжается пока входной набор символов обработан не полностью.

# После полной обработки входного набора символов результат вычисления
# выражения находится в вершине стека.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Калькулятор (лат. calculātor «счётчик») — электронное вычислительное
# устройство для выполнения операций над числами или алгебраическими
# формулами.

# Описание алгоритма соответствует определению калькулятора
# принимающего на вход выражение в обратной польской нотации.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Вычисление одной операции стоит O(1), вычисление всего выражения
# O(n), где n - количество операций в выражении.


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Калькулятор потребляет O(n) памяти, где n - количество операций в
# выражении.


# https://contest.yandex.ru/contest/22781/run-report/69578996/
from operator import add, floordiv, mul, sub
from typing import List


class Calculator:
    def __init__(self):
        self.items = []
        self.operations = {'+': add, '-': sub, '*': mul, '/': floordiv}

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        return self.items.pop()

    def eval(self, expr: List[str]) -> None:
        for x in expr:
            if x in self.operations.keys():
                oper1, oper2 = self.pop(), self.pop()
                self.push(self.operations[x](oper2, oper1))
            else:
                self.push(int(x))
        print(self.pop())


def main() -> int:
    calc = Calculator()
    calc.eval(list(input().split()))
    return 0


if __name__ == '__main__':
    main()
