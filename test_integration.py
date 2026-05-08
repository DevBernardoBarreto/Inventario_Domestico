# test_integration.py
import unittest
from unittest.mock import patch
from servicos import obter_cotacao_dolar

class TestAPIIntegration(unittest.TestCase):
    
    def test_obter_cotacao_dolar_sucesso(self):
        """Valida se a API externa está ativa e retornando um número válido"""
        cotacao = obter_cotacao_dolar()
        self.assertIsInstance(cotacao, float)
        self.assertGreater(cotacao, 0.0)

    @patch('requests.get')
    def test_obter_cotacao_dolar_falha(self, mock_get):
        """Valida se o seu código se comporta de forma segura caso a API caia"""
        mock_get.side_effect = Exception("Erro de conexão simulado")
        cotacao = obter_cotacao_dolar()
        # Deve retornar 1.0 (fallback de segurança) em vez de quebrar a aplicação
        self.assertEqual(cotacao, 1.0)

if __name__ == '__main__':
    unittest.main()