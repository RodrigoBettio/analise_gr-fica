import matplotlib
matplotlib.use('Agg')  #Usado para gerar os gráficos antes de subir na interface

import matplotlib.pyplot as plt
import io
import base64 #Para converter o gráfico em formato base64 (necessário para incorporá-lo em páginas HTML).
import random

def obter_dados_acoes(acao, data_inicial, data_final):
    #Simulação de dados para teste
    x = ["2024-11-20", "2024-11-21", "2024-11-22", "2024-11-23"]
    y = [random.uniform(20, 50) for _ in x]

    # Gerar gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='b')
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

def obter_dados_commoditys(commodity, data_inicial, data_final):
    #Simulação de dados para teste
    x = ["2024-11-20", "2024-11-21", "2024-11-22", "2024-11-23"]
    y = [random.uniform(1500, 1600) for _ in x]  

    # Gerar gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='g')
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
