import csv
from sys import argv

import pandas as pd
import seaborn as sns

# extraindo colunas hora e taxa
df = pd.read_csv('./taxa-cdi.csv')

# salvando no grafico, usando os dados de df
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
grafico.get_figure().savefig(f'{argv[1]}.png')
