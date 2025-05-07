import requests

BASE_URL = "http://127.0.0.1:5000"  # Локальний сервер

def test_get_currencies():
    response = requests.get(f"{BASE_URL}/currencies")
    assert response.status_code == 200
    currencies = response.json()
    print("✔ Список валют:", currencies)
    assert any(c["code"] == "USD" for c in currencies)

def test_get_rates():
    response = requests.get(f"{BASE_URL}/rates")
    assert response.status_code == 200
    rates = response.json()
    print("✔ Курси валют:", rates)
    assert any(rate["Currency1"] == "USD" and rate["Currency2"] == "UAH" for rate in rates)

def test_conversion():
    data = {
        "currency_from": "USD",
        "currency_to": "UAH",
        "amount": 100
    }
    response = requests.post(f"{BASE_URL}/convert", json=data)
    assert response.status_code == 200
    result = response.json()
    print(f"✔ Конверсія: {data['amount']} {data['currency_from']} = {result['converted']} {data['currency_to']}")
    assert result['converted'] > 0

def test_add_and_delete_currency():
    # Додавання
    new_rate = {"Currency1": "GBP", "Currency2": "UAH", "Rate": 47.1}
    response = requests.post(f"{BASE_URL}/add_currency", json=new_rate)
    assert response.status_code in [200, 201]
    print("✔ Валюта GBP додана")

    # Перевірка наявності, чи є
    response = requests.get(f"{BASE_URL}/rates")
    assert any(rate["Currency1"] == "GBP" for rate in response.json())

    # Видалення
    response = requests.delete(f"{BASE_URL}/delete_currency", json={
        "Currency1": "GBP",
        "Currency2": "UAH"
    })
    assert response.status_code == 200
    print("✔ Валюта GBP видалена")

def run_all_tests():
    print("=== Тестування API сервера обміну валют ===")
    test_get_currencies()
    test_get_rates()
    test_conversion()
    test_add_and_delete_currency()
    print("=== Усі тести пройдено успішно ===")

if __name__ == "__main__":
    run_all_tests()

