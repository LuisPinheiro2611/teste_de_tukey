'''O código a baixo visa realizar o Teste  de Tukey para dados obtidos de um Delineamento em Blocos Casualizados (DBC)
de um experimento, criando um DataFrame da planilha contendo os dados (excel, mas pode ser usado para  arquivos CSV,
necessitando apenas substiutir a função read_excel() por read_csv()) e realizar o teste para cada variável presente na
planilha ()

Estrutura básica da planilha para o funcionamento do código:

  Parcela   Blocos  Tratamentos  Variavel
0    -        -         -           -
1    -        -         -           -
2    -        -         -           -
3
.
.
.  '''

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import matplotlib.pyplot as plt

# Abrir planilha
try:
    df = pd.read_excel('dados_exemplos.xlsx')
except FileNotFoundError:
    print('Arquivo não encontrado. Verifique o caminho e o nome do arquivo.')
    exit()

# Visualizar o DataFrame da planilha de excel
print(df.head())

# Criar uma lista contendo as variáveis a serem analisadas no teste
lista_variaveis = [coluna for coluna in df.columns if coluna not in ['Parcela', 'Blocos', 'Tratamentos']]

# Realiza-se então a ANOVA e o teste de Tukey para cada variável
for variavel in lista_variaveis:
    print(f'{variavel}'.center(50, '-'))

    # Criar modelo
    modelo = ols(f'{variavel} ~ C(Tratamentos) + C(Blocos)', df).fit()

    # Realizar a ANOVA
    tabela = sm.stats.anova_lm(modelo)
    print(tabela)

    # Obter o pvalor
    pvalor = tabela.loc['C(Tratamentos)', 'PR(>F)']

    # Análise pelo pvalor
    if pvalor >= 0.05:
        print('Não se rejeita H0, não há diferença estatística entre as médias')
    else:
        print('Rejeita-se H0, há alguma diferença entre as médias')

    # Teste de Tukey
    tukey = pairwise_tukeyhsd(groups=df['Tratamentos'], endog=df[variavel], alpha=0.05)
    print(tukey)

    # Gráficos
    tukey.plot_simultaneous()
    plt.title(f'Teste de Tukey - {variavel}')
    plt.show()
    plt.savefig(f'grafico_tukey_{variavel}.png')
