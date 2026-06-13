import unittest
from unittest.mock import patch, Mock

from servicos import obter_cotacao_dolar


class TestAPIIntegration(unittest.TestCase):

    @patch("requests.get")
    def test_obter_cotacao_dolar_sucesso(self, mock_get):
        """Valida a conversão quando a API retorna uma resposta correta."""
        resposta_mock = Mock()
        resposta_mock.status_code = 200
        resposta_mock.json.return_value = {"USDBRL": {"bid": "5.25"}}
        mock_get.return_value = resposta_mock

        cotacao = obter_cotacao_dolar()

        self.assertIsInstance(cotacao, float)
        self.assertEqual(cotacao, 5.25)

    @patch("requests.get")
    def test_obter_cotacao_dolar_falha(self, mock_get):
        """Valida se o código usa fallback seguro caso a API caia."""
        mock_get.side_effect = Exception("Erro de conexão simulado")

        cotacao = obter_cotacao_dolar()

        self.assertEqual(cotacao, 1.0)


if __name__ == "__main__":
    unittest.main()
