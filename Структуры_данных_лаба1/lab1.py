import time
print("Оверчук Кирилл Николаевич")
def prime_factors(n):
    """ Возвращает словарь простых множителей числа n и их степеней. """
    factors = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors

def min_n(A, B):
    A_factors = prime_factors(A)
    B_factors = prime_factors(B)

    n = 0
    for p, a_count in A_factors.items():
        if p not in B_factors:
            return -1  # Если p не является простым множителем B, то B^n не может делиться на A
        b_count = B_factors[p]
        # Нам нужно, чтобы b_count * n >= a_count
        # Следовательно, n >= a_count / b_count
        required_n = (a_count + b_count - 1) // b_count  # Округляем вверх
        n = max(n, required_n)

    return n

# Чтение входных данных
A = int(input().strip())
B = int(input().strip())

# Измерение времени выполнения
start_time = time.perf_counter()  # Запоминаем время начала

# Вычисление и вывод результата
result = min_n(A, B)
print(result)

end_time = time.perf_counter()  # Запоминаем время окончания
execution_time = end_time - start_time  # Вычисляем время выполнения
print(f"Время выполнения: {execution_time:.6f} секунд")