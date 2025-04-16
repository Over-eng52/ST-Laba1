import time
import random
from collections import deque


# А) Реализация через массив
class CoinArray:
    def __init__(self, n, m):
        self.coins = [1] * n + [0] * m  # 1 - герб вверх, 0 - герб вниз
        random.shuffle(self.coins)

    def flip_coins(self, s, k):
        n = len(self.coins)
        index = 0
        for _ in range(k):
            for _ in range(s):
                index = (index + 1) % n
            self.coins[index] = 1 - self.coins[index]  # Переворот монеты

    def count_heads(self):
        return sum(self.coins)


# Б) Реализация через связанный список
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CoinLinkedList:
    def __init__(self, n, m):
        self.head = None
        for _ in range(n + m):
            new_node = Node(1 if _ < n else 0)
            new_node.next = self.head
            self.head = new_node

        # Перемешивание списка
        coins = []
        current = self.head
        while current:
            coins.append(current.value)
            current = current.next

        random.shuffle(coins)

        # Восстановление связанного списка после перемешивания
        self.head = None
        for value in coins:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def flip_coins(self, s, k):
        current = self.head
        length = 0

        # Подсчет длины списка
        while current:
            length += 1
            current = current.next

        index_to_flip = 0

        for _ in range(k):
            for _ in range(s):
                index_to_flip += 1

            index_to_flip %= length

            # Переворот монеты в связанном списке
            current = self.head
            for _ in range(index_to_flip):
                current = current.next

            current.value = 1 - current.value

    def count_heads(self):
        count = 0
        current = self.head

        while current:
            count += current.value
            current = current.next

        return count


# В) Реализация с использованием стандартной библиотеки (deque)
class CoinDeque:
    def __init__(self, n, m):
        self.coins = deque([1] * n + [0] * m)
        random.shuffle(self.coins)

    def flip_coins(self, s, k):
        n = len(self.coins)

        for _ in range(k):
            for _ in range(s - 1):  # Пропускаем первую монету (начинаем с герба)
                self.coins.append(self.coins.popleft())

            # Переворот монеты на позиции s-ой (после сдвига)
            flipped_coin = self.coins.popleft()
            self.coins.append(1 - flipped_coin)  # Переворот

    def count_heads(self):
        return sum(self.coins)


# Функция для тестирования всех реализаций и сравнения производительности
def test_flipping_coins(n, m, s, k):
    print(f"Тестирование с N={n}, M={m}, S={s}, K={k}")

    # Тестирование массива
    start_time = time.time()
    coin_array = CoinArray(n, m)
    coin_array.flip_coins(s, k)
    heads_array_count = coin_array.count_heads()
    array_time_taken = time.time() - start_time

    print(f"Массив: {heads_array_count} гербов вверх; Время: {array_time_taken:.6f} сек")

    # Тестирование связанного списка
    start_time = time.time()
    coin_linked_list = CoinLinkedList(n, m)
    coin_linked_list.flip_coins(s, k)
    heads_linked_count = coin_linked_list.count_heads()
    linked_time_taken = time.time() - start_time

    print(f"Связанный список: {heads_linked_count} гербов вверх; Время: {linked_time_taken:.6f} сек")

    # Тестирование deque
    start_time = time.time()
    coin_deque = CoinDeque(n, m)
    coin_deque.flip_coins(s, k)
    heads_deque_count = coin_deque.count_heads()
    deque_time_taken = time.time() - start_time

    print(f"Deque: {heads_deque_count} гербов вверх; Время: {deque_time_taken:.6f} сек")


# Пример использования функции тестирования с параметрами N=10 M=5 S=3 K=4
test_flipping_coins(10000, 9790, 5190, 500)