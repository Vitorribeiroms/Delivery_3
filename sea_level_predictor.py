import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # ETAPA 1: Ler os dados do arquivo.
    # Primeiro, aqui eu carrego o arquivo 'epa-sea-level.csv' para o meu programa
    # usando a biblioteca pandas. Chamei a minha tabela de 'dados'.
    dados = pd.read_csv('epa-sea-level.csv')

    # Para garantir que meu gráfico fique com um bom tamanho, eu defino as dimensões da figura no seguinte comando abixo.
    plt.figure(figsize=(14, 7))
    

    # ETAPA 2: Criar o gráfico de dispersão.
    # Agora, aqui eu pego os meus 'dados' e crio um gráfico de pontos ('scatter plot').
    # No eixo X, eu coloco a coluna 'Year' e no eixo Y, a 'CSIRO Adjusted Sea Level'.
    plt.scatter(x=dados['Year'], y=dados['CSIRO Adjusted Sea Level'], label='Dados Históricos')


    # ETAPA 3: Criar a primeira linha de tendência.
    # Para fazer a previsão, aqui eu calculo a regressão linear de todos os dados.
    # A função 'linregress' me dá a inclinação (slope) e a intersecção (intercept) da reta.
    res_geral = linregress(x=dados['Year'], y=dados['CSIRO Adjusted Sea Level'])
    
    # Eu quero projetar o futuro, então crio uma lista de anos que vai do primeiro ano do meu dataset até 2050.
    anos_predicao_geral = range(dados['Year'].min(), 2051)
    
    # Já nesta parte, com a fórmula da reta (y = mx + b), eu calculo os valores previstos
    # para o nível do mar. 'm' é a inclinação e 'b' é onde a linha começa.
    nivel_predicao_geral = res_geral.intercept + res_geral.slope * pd.Series(anos_predicao_geral)
    
    # Por fim, eu desenho essa linha de previsão no meu gráfico, usando a cor vermelha e tracejada.
    plt.plot(anos_predicao_geral, nivel_predicao_geral, 'r--', label='Previsão (1880-2050)')
    

    # ETAPA 4: Criar a segunda linha de tendência.
    # Eu percebi que talvez a tendência de subida do mar tenha acelerado. Para verificar isso,
    # decidi criar uma nova linha de tendência usando apenas os dados a partir do ano 2000.

    # Primeiro, aqui eu vou filtrar minha tabela original para pegar somente as linhas com ano maior ou igual a 2000.
    dados_recentes = dados[dados['Year'] >= 2000]
    
    # Agora, eu repito o cálculo da regressão linear, mas dessa vez só com esses 'dados_recentes'.
    res_recente = linregress(x=dados_recentes['Year'], y=dados_recentes['CSIRO Adjusted Sea Level'])
    
    # A lista de anos para essa nova previsão vai de 2000 até 2050.
    anos_predicao_recente = range(2000, 2051)
    
    # E calculo novamente os valores previstos com base nesta nova tendência.
    nivel_predicao_recente = res_recente.intercept + res_recente.slope * pd.Series(anos_predicao_recente)
    
    # Já neste plot, eu desenho a segunda linha no gráfico, agora com a cor verde, para comparar com a primeira.
    plt.plot(anos_predicao_recente, nivel_predicao_recente, 'g', label='Previsão Acelerada (2000-2050)', linewidth=2)


    # ETAPA 5: Adicionar rótulos e título.
    # Para que meu gráfico seja fácil de entender, aqui eu adiciono um título principal,
    # e também nomes para os eixos X e Y.
    plt.title('Aumento do Nível do Mar', fontsize=16)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Nível do Mar Ajustado (polegadas)', fontsize=12)
    
    # E para finalizar, eu também adiciono uma legenda para explicar o que cada cor significa e uma grade.
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.5)
    
    
    # Salvar o gráfico e retornar os dados para teste (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()