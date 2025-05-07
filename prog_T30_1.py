def inverse_cube_series(x, epsilon=1e-6):
    """
    Обчислює 1 / (1 + x)^3 за допомогою розкладу в степеневий ряд.
    Розклад: y = ∑ [(-1)^k * (k+1)(k+2)/2 * x^k], для |x| < 1
    """
    if abs(x) >= 1:
        raise ValueError("Ряд збігається лише при |x| < 1")
    
    term = 1.0  # перший доданок при k = 0
    result = term
    k = 1
    
    while abs(term) >= epsilon:
        coef = ((k + 1) * (k + 2)) / 2
        term = ((-1) ** k) * coef * (x ** k)
        result += term
        k += 1
    
    return result

def test_inverse_cube_series():
    import math
    test_values = [-0.9, -0.5, -0.1, 0.1, 0.5, 0.9]
    epsilon = 1e-6
    print(f"{'x':>8} | {'Сума ряду':>15} | {'Точне знач.':>15} | {'Різниця':>10}")
    print("-" * 55)
    for x in test_values:
        approx = inverse_cube_series(x, epsilon)
        actual = 1 / ((1 + x) ** 3)
        diff = abs(approx - actual)
        print(f"{x:8.4f} | {approx:15.10f} | {actual:15.10f} | {diff:10.2e}")

if __name__ == "__main__":
    test_inverse_cube_series()
