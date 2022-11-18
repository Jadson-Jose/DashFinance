import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
else:
    data_struture = {'valor': [],
                     'Efetuado': [],
                     'Fixo': [],
                     'Data': [],
                     'Categoria': [],
                     'Descricao': [],
                     }
    df_receitas = pd.DataFrame(data_struture)
    df_despesas = pd.DataFrame(data_struture)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")


if ("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_receitas = pd.read_csv("df_cat_receitas.csv", index_col=0)
    df_cat_despesas = pd.read_csv("df_cat_despesas.csv", index_col=0)
else:
    cat_receitas = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesas = {'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]}

    df_cat_receitas = pd.DataFrame(cat_receitas)
    df_cat_despesas = pd.DataFrame(cat_despesas)