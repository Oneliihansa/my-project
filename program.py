def triangular_numbers(n):
    for i in range(1, n + 1):
        print(f"Triangular number {i}: {i * (i + 1) // 2}")