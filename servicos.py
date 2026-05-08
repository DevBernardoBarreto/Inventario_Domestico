# servicos.py
import requests

def obter_cotacao_dolar():
    """
    Consome a API pública AwesomeAPI para obter a cotação atual do USD em BRL.
    Retorna o valor flutuante da cotação ou 1.0 como fallback em caso de falha.
    """
    try:
        response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL", timeout=5)
        if response.status_code == 200:
            dados = response.json()
            # Retorna o valor de compra (bid) do Dólar convertido para float
            return float(dados['USDBRL']['bid'])
        return 1.0
    except Exception:
        # Se a internet cair ou a API estiver fora do ar, o sistema não trava
        return 1.0