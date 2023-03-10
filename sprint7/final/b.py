# -- ПРИНЦИП РАБОТЫ --

# «Задача разбиения» (Partition problem). Задано множество элементов
# arr = {x₀, ..., xₙ₋₁}. Выяснить, существует ли способ разбить его на
# два подмножества, так чтобы сумма значений всех элементов в каждом
# из подмножеств была одинаковой?

# 1. Массив dp размером n на m, где n - число элементов, а m -
# половина суммы значений исходного множества. dp[i][j] принимает
# значение True, если среди {x₀, ..., xᵢ₋₁} существует такое
# подмножество, элементы которого в сумме дают j.

# 2. Базовыми случаями являются: dp[0][0] = True, в первом столбце
# dp[i][0] = True, в первой строке dp[0][j] = False.

# 3. Рекуррентная формула: dp[i][j] = True, если dp[i-1][j] = True или
# dp[i-1][j-arr[i-1]] = True, иначе False.

# 4. Чтобы посчитать значение в клетке dp[i][j], нужно знать значения
# предыдущей строки. Это получится, если обходить матрицу сначала по
# строкам, потом по столбцам.

# 5. Искомое значение будет содержаться в ячейке dp[n][m], то есть в
# нижней правой клетке матрицы.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Существует некоторое подмножество arr, сумма которого равна j для чисел
# {x₀, ..., xᵢ₋₁} тогда и только тогда, когда одно из двух верно:
# • существует подмножество {x₀, ..., xᵢ₋₂}, дающее сумму j;
# • существует подмножество {x₀, ..., xᵢ₋₂}, дающее сумму j − xᵢ₋₁,
# поскольку xᵢ₋₁ + сумма этого подмножества = j.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Основной цикл повторяется n * m раз. Таким образом, временная
# сложность алгоритма O(nm).


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Программа хранит только предыдущую строку dp, то есть потребление
# памяти снижено до O(m).


# https://contest.yandex.ru/contest/25597/run-report/73662797/
from typing import List


def is_partition(n: int, arr: List[int]) -> None:
    arr_sum = sum(arr)
    if arr_sum % 2:
        print('False')
        return
    m = arr_sum // 2
    dp_curr = [True] + [False] * m
    for i in range(1, n + 1):
        dp_prev, dp_curr = dp_curr, [True] + [False] * m
        for j in range(m + 1):
            if j - arr[i - 1] >= 0:
                dp_curr[j] = dp_prev[j] or dp_prev[j - arr[i - 1]]
            else:
                dp_curr[j] = dp_prev[j]
    print(dp_curr[m])


def main() -> int:
    is_partition(int(input()), list(map(int, input().split())))
    return 0


if __name__ == '__main__':
    main()
