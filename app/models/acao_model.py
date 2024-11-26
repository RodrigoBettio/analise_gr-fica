import yfinance as yf
import matplotlib
matplotlib.use('Agg')  # Usado para gerar gráficos em servidores (sem GUI)

import matplotlib.pyplot as plt
import io
import base64  # Para converter gráficos para formato base64
from matplotlib.dates import DateFormatter, YearLocator, MonthLocator

def configurar_eixo_temporal(ax, dados, intervalo):
    """
    Configura o eixo X (tempo) do gráfico para exibir marcações anuais ou mensais.
    
    - `ax`: O eixo do gráfico.
    - `dados`: DataFrame com os dados de preços.
    - `intervalo`: 'ano' para marcações anuais ou 'mes' para mensais.
    """
    if intervalo == 'ano':
        ax.xaxis.set_major_locator(YearLocator())  # Marcar cada ano
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))  # Formatar como ano
        
    elif intervalo == 'mes':
        ax.xaxis.set_major_locator(MonthLocator())  # Marcar cada mês
        ax.xaxis.set_major_formatter(DateFormatter('%b %Y'))  # Formatar como mês e ano
    ax.tick_params(axis='x', rotation=45)  # Rotaciona os rótulos para melhor visualização

def obter_dados_acoes(acao, data_inicial, data_final, intervalo):
    """ Obtém dados reais de ações usando a API do Yahoo Finance."""
    try:
        # Baixar dados da ação
        dados = yf.download(acao, start=data_inicial, end=data_final)
        
        if dados.empty:
            raise ValueError("Nenhum dado encontrado para o período especificado.")
        
        if intervalo == 'ano':
            dados_intervalo = dados.resample('A').last() 
        else:
            dados_intervalo = dados.resample('M').last() 


        # Gerar gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(dados_intervalo.index, dados_intervalo['Close'], marker='o', linestyle='-', color='b')
        configurar_eixo_temporal(ax, dados, intervalo)
        
        ax.set_title(f"Gráfico da Ação {acao}")
        ax.set_xlabel("Datas")
        ax.set_ylabel("Valor (USD)")
        ax.legend()

        # Converter gráfico para base64
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        grafico = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()
        plt.close(fig)

        return grafico
    except Exception as e:
        return f"Erro ao obter dados: {str(e)}"

def obter_dados_commoditys(commodity, data_inicial, data_final, intervalo):
    """Obtém dados reais de commodities usando a API do Yahoo Finance."""

    try:
        # Baixar dados da commodity
        dados = yf.download(commodity, start=data_inicial, end=data_final)

        if dados.empty:
            raise ValueError("Nenhum dado encontrado para o período especificado.")

        if intervalo == 'ano':
            dados_intervalo = dados.resample('A').last()
        else:
            dados_intervalo = dados.resample('M').last()

        # Gerar gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(dados_intervalo.index, dados_intervalo['Close'], marker='o', linestyle='-', color='g')
        configurar_eixo_temporal(ax, dados, intervalo)

        ax.set_title(f"Gráfico da Commodity {commodity}")
        ax.set_xlabel("Datas")
        ax.set_ylabel("Valor (USD)")
        ax.legend()

        # Converter gráfico para base64
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        grafico = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()
        plt.close(fig)

        return grafico
    except Exception as e:
        return f"Erro ao obter dados: {str(e)}"

