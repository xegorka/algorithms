# -- ПРИНЦИП РАБОТЫ --

# Считывается карта дорог в списки смежности единого графа, где дороги
# являются ребрами, а города вершинами. Для дорог типа B ориентация
# ребра изменяется на противоположную, то есть от вершины с большим
# номером к вершине с меньшим. Из каждой вершины выполняется обход
# графа по алгоритму DSF. Если при проверке смежных по исходящим дугам
# вершин очередная вершина окажется серой, в графе гарантировано есть
# цикл. При обнаружении цикла программа завершает работу с выводом
# «NO», иначе после обхода графа из всех вершин выводится сообщение
# «YES», то есть карта оптимальная. Таким образом выясняется, является
# ли данная карта оптимальной.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Если существует пара городов A и B такая, что от A до B можно
# добраться как по дорогам типа R, так и по дорогам типа B, тогда
# карта неоптимальная. Принцип работы основывается на том, что если
# поменять направление одного из двух типов дорог на противоположное,
# то карта неоптимальная в случае, если можно добраться как от A до B,
# так и от B до A. При этом тип дороги не имеет значения, а путь A ->
# B -> A является циклом. Таким образом, если в едином графе дорог,
# где один из типов дорог с измененным направлением, не существует
# цикла, то карта оптимальная.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Граф представлен списками смежности, поэтому перебрать все смежные
# вершины можно за время, пропорциональное числу этих вершин.
# Поскольку алгоритм обрабатывает все вершины, ему придётся пройтись
# по всем спискам смежности. Это эквивалентно тому, чтобы пройти по
# каждому ребру по одному разу, что займёт O(E). Итоговая сложность
# алгоритма O(E + V).


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Для хранения списков смежности потребуется O(E + V), под массив с
# цветом вершин и стек O(V) + O(V). В общей сумме программа
# затрачивает O(E + V) памяти.


# https://contest.yandex.ru/contest/25070/run-report/71899063/
from typing import List


def dsf(s: int, adj: List[int], color: List[int]) -> bool:
    stack = [s]
    while len(stack):
        v = stack.pop()
        if color[v] == 0:
            color[v] = 1
            stack.append(v)
            for w in adj[v]:
                if color[w] == 0:
                    stack.append(w)
                elif color[w] == 1:
                    return False
        elif color[v] == 1:
            color[v] = 2
    return True


def main() -> int:
    n = int(input())
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        x = str(input())
        for j in range(n - i - 1):
            if x[j] == 'R':
                adj[i].append(j + i + 1)
            elif x[j] == 'B':
                adj[j + i + 1].append(i)
    color = [0] * n
    for s in range(n):
        if not dsf(s, adj, color):
            print('NO')
            return 0
    print('YES')
    return 0


if __name__ == '__main__':
    main()
