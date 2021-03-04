import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={"figure.figsize":(10,8)})

sns.set(style="ticks", context="talk")

df = pd.read_csv("train.csv")
df.head()

# Визуализация корреляций

clean_train = df.drop(['v.id'], axis=1)
sns.heatmap(clean_train.corr(), annot = True, cmap= 'viridis', annot_kws={"size":12})
