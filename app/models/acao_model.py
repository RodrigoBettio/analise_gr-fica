import yfinance as yf
import matplotlib
matplotlib.use('Agg')  # Usado para gerar gráficos em servidores (sem GUI)

import matplotlib.pyplot as plt
import io
import base64  # Para converter gráficos para formato base64


def obter_dados_acoes(acao, data_inicial, data_final):
    """ Obtém dados reais de ações usando a API do Yahoo Finance."""
    try:
        # Baixar dados da ação
        dados = yf.download(acao, start=data_inicial, end=data_final)
        
        if dados.empty:
            raise ValueError("Nenhum dado encontrado para o período especificado.")

        # Gerar gráfico
        fig, ax = plt.subplots()
        ax.plot(dados.index, dados['Close'], marker='o', linestyle='-', color='b')
        ax.set_title(f"Gráfico da Ação {acao}")
        ax.set_xlabel("Datas")
        ax.set_ylabel("Valor (USD)")
        
        # Converter gráfico para base64
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        grafico = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()
        plt.close(fig)

        return grafico
    except Exception as e:
        return f"Erro ao obter dados: {str(e)}"


def obter_dados_commoditys(commodity, data_inicial, data_final):
    """Obtém dados reais de commodities usando a API do Yahoo Finance."""
  
    try:
        # Baixar dados da commodity
        dados = yf.download(commodity, start=data_inicial, end=data_final)
        
        if dados.empty:
            raise ValueError("Nenhum dado encontrado para o período especificado.")

        # Gerar gráfico
        fig, ax = plt.subplots()
        ax.plot(dados.index, dados['Close'], marker='o', linestyle='-', color='g')
        ax.set_title(f"Gráfico da Commodity {commodity}")
        ax.set_xlabel("Datas")
        ax.set_ylabel("Valor (USD)")
        
        # Converter gráfico para base64
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        grafico = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()
        plt.close(fig)

        return grafico
    except Exception as e:
        return f"Erro ao obter dados: {str(e)}"
