import math

def ln1x_series(x, epsilon=1e-6):
    """
    Обчислює ln(1 + x) як суму ряду:
    ln(1 + x) = x - x^2/2 + x^3/3 - x^4/4 + ... для |x| < 1
    Ряд обривається, коли абсолютне значення доданка менше epsilon
    """
    if abs(x) >= 1:
        raise ValueError("Ряд збігається лише при |x| < 1")

    term = x  # перший доданок
    result = term
    k = 2

    while abs(term) >= epsilon:
        term = ((-1) ** (k + 1)) * (x ** k) / k
        result += term
        k += 1

    return result


# Тестування для декількох значень x та ε
def test_ln1x_series():
    test_values = [-0.5, -0.1, 0.1, 0.5, 0.9]
    epsilon = 1e-6
    print(f"{'x':>8} | {'ln(1+x) ряд':>18} | {'ln(1+x) math':>18} | {'Різниця':>10}")
    print("-" * 60)
    for x in test_values:
        approx = ln1x_series(x, epsilon)
        actual = math.log(1 + x)
        diff = abs(approx - actual)
        print(f"{x:8.4f} | {approx:18.10f} | {actual:18.10f} | {diff:10.2e}")


if __name__ == "__main__":
    test_ln1x_series()
