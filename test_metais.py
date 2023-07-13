import unittest
from unittest.mock import patch
from consulta_metais import consulta_ouro
from consulta_metais import converte_dolar_peso_ouro

class TestGoldAPI(unittest.TestCase):

    @patch('consulta_metais.requests.get')
    def test_gold_price(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'price': 1800}  # Cotação atual do ouro em dólar

        result = consulta_ouro()
        self.assertEqual(result, 1800)

    @patch('consulta_metais.consulta_ouro')
    def test_convert_dollar_to_gold_value(self, mock_get_gold_price):
        mock_get_gold_price.return_value = 1800  # Cotação atual do ouro em dólar
        
        dollars = 100
        expected_gold_value = 0.0017279722222222223   # Valor esperado em quilogramas de ouro
        result = converte_dolar_peso_ouro(mock_get_gold_price, dollars)
        self.assertAlmostEqual(result, expected_gold_value, places=3)
    
    

if __name__ == '__main__':
    unittest.main()

