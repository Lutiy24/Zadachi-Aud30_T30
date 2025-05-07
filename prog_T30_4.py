def char_to_digit(c, base):

    if '0' <= c <= '9':
        digit = ord(c) - ord('0')
    elif 'A' <= c.upper() <= 'F':
        digit = ord(c.upper()) - ord('A') + 10
    else:
        raise ValueError(f"Неприпустимий символ: '{c}'")

    # Перевірка належності цифри до основи
    assert 0 <= digit < base, f"Символ '{c}' не є допустимим у системі з основою {base}"
    return digit


def convert_to_decimal(s, base):
    
    result = 0
    for c in s:
        digit = char_to_digit(c, base)
        result = result * base + digit
    return result


def test_conversion():
    test_cases = [
        ("1011", 2),
        ("1A", 16),
        ("123", 10),
        ("77", 8),
        ("FACE", 16),
        ("19", 8),       # помилка: 9 не входить у систему з основою 8
        ("Z1", 16),      # помилка: Z не належить допустимим символам
        ("100", 2),
        ("A1", 11),
    ]

    for s, base in test_cases:
        try:
            print(f"Число '{s}' у системі {base} = {convert_to_decimal(s, base)}")
        except (AssertionError, ValueError) as e:
            print(f"Помилка при обробці '{s}' з основою {base}: {e}")

if __name__ == "__main__":
    test_conversion()
