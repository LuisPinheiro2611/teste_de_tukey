# Teste de Tukey para DBC com Python

Este script realiza análise estatística (ANOVA e Teste de Tukey) com dados de um Delineamento em Blocos Casualizados (DBC)

## Requisitos
-Python 3.x
-pandas
-statsmodels
-matplotlib

# Como usar
1. Coloque a planilha .xlsx ( ou seu caminho) com os dados do experimento em read_excel, com a planilha contendo a seguinte estrutura:
   | Parcela | Blocos | Tratamentos | Variável |
   |---------|--------|-------------|----------|
2. Rode o script:
   '''bash python teste_de_tukey.py
