import unittest
from pydantic import ValidationError
from historical_data_model import HistoricalDataList
import json
from Coinbase import get_historical_data, get_available_products

class TestCoinbaseLoader(unittest.TestCase):
    def test_get_historical_data(self):
        data = get_historical_data('BTC-USD', '2024-01-01', '2024-01-02', 3600)
        self.assertIsNotNone(data)
    
    def test_get_available_products(self):
        products = get_available_products()
        self.assertIsInstance(products, list)
        self.assertTrue(len(products) > 0)
    
    def test_invalid_product(self):
        data = get_historical_data('INVALID-PRODUCT', '2024-01-01', '2024-01-02', 3600)
        self.assertIsNone(data)
    
    def test_valid_historical_data(self):
        with open('valid_historical_data.json') as f:
            data = json.load(f)
        try:
            HistoricalDataList(root=data)
        except ValidationError as e:
            self.fail(f"Validation failed for valid data: {e}")

    def test_invalid_historical_data(self):
        with open('invalid_historical_data.json') as f:
            data = json.load(f)
        with self.assertRaises(ValidationError):
            HistoricalDataList(root=data)

if __name__ == '__main__':
    unittest.main()
