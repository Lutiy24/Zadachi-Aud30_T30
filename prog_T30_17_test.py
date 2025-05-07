import unittest
from unittest.mock import patch, MagicMock
from prog_T30_17 import get_weather, save_to_excel

class TestWeatherParser(unittest.TestCase):

    @patch("prog_T30_17.requests.get")
    def test_get_weather_mocked(self, mock_get):
        # Завантажуємо фейкову HTML-сторінку
        with open("sample_sinoptik.html", "r", encoding="utf-8") as f:
            mock_get.return_value.text = f.read()
            mock_get.return_value.encoding = 'utf-8'
        
        data = get_weather("kyiv")
        self.assertEqual(len(data), 5)
        for day in data:
            self.assertIn("date", day)
            self.assertIn("min", day)
            self.assertIn("max", day)

    @patch("prog_T30_17.Workbook")
    def test_save_to_excel_mocked(self, mock_wb):
        mock_ws = MagicMock()
        mock_wb.return_value.active = mock_ws

        test_data = [
            {"date": "2025-05-07", "min": 10, "max": 20},
            {"date": "2025-05-08", "min": 11, "max": 21},
        ]
        save_to_excel(test_data, filename="mocked.xlsx")

        self.assertEqual(mock_ws.append.call_count, 3)  # header + 2 дні

if __name__ == '__main__':
    unittest.main()
