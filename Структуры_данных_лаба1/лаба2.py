import numpy as np
import time
from scipy.linalg import blas

# Размер матриц
n = 1024

# Генерация случайных матриц с элементами типа single complex
A = np.random.rand(n, n).astype(np.complex64) + 1j * np.random.rand(n, n).astype(np.complex64)
B = np.random.rand(n, n).astype(np.complex64) + 1j * np.random.rand(n, n).astype(np.complex64)
print("Матрицы A и B созданы.")
# Оценка сложности
c = 2 * (n ** 3)

# Вариант 1: Перемножение с использованием NumPy
start_time = time.time()
C1 = np.dot(A, B)  # Используем встроенную функцию NumPy
end_time = time.time()
t1 = end_time - start_time
MFlops1 = c / (t1 * 10**6)
print(f"Вариант 1 (NumPy): Время: {t1:.6f} сек, MFlops: {MFlops1:.2f}")

# Вариант 2: Перемножение с использованием cblas_cgemm из библиотеки BLAS
start_time = time.time()
C2 = blas.cgemm(1.0, A, B)
end_time = time.time()
t2 = end_time - start_time
MFlops2 = c / (t2 * 10**6)
print(f"Вариант 2 (BLAS): Время: {t2:.6f} сек, MFlops: {MFlops2:.2f}")

# Вариант 3: Оптимизированный алгоритм (блоковое умножение)
def block_matrix_multiply(A, B, block_size=32):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.complex64)
    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            for k in range(0, n, block_size):
                # Умножаем блоки A и B и добавляем к C
                C[i:i+block_size, j:j+block_size] += np.dot(A[i:i+block_size, k:k+block_size], B[k:k+block_size, j:j+block_size])
    return C

start_time = time.time()
C3 = block_matrix_multiply(A, B)
end_time = time.time()
t3 = end_time - start_time
MFlops3 = c / (t3 * 10**6)
print(f"Вариант 3 (Блоковое умножение): Время: {t3:.6f} сек, MFlops: {MFlops3:.2f}")

# Сравнение результатов
print("\nСравнение результатов:")
print(f"C1 == C2? {np.allclose(C1, C2)}")
print(f"C1 == C3? {np.allclose(C1, C3)}")