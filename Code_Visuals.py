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

# Проверка корреляции 1

graph_km = sns.scatterplot(data = df, x = 'current price',y = 'km', hue='current price',
                                    legend=False,palette='viridis')
graph_km.set(xlabel='Current price', ylabel='Km')

# Проверка корреляции 2

graph_on_road_now = sns.scatterplot(data = df, x = 'current price',y = 'on road now', hue='current price',
                                    legend=False,palette='viridis')
graph_on_road_now.set(xlabel='Current price', ylabel='On road now')

# Проверка корреляции 3

graph_on_road_old = sns.scatterplot(data = df, x = 'current price',y = 'on road old', hue='current price',
                                    legend=False,palette='viridis')
graph_on_road_old.set(xlabel='Current price', ylabel='On road old')
