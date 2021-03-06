import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("train.csv")
df.head()

# Убираем целевой столбец:

X = df[['v.id', 'on road old', 'on road now', 'years', 'km', 'rating',
       'condition', 'economy', 'top speed', 'hp', 'torque']]
Y = df['current price']

# Разбиваем выборку на тренировочную и тестовую:

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# Создание:

Regr = LinearRegression()

# Тренировка на выбраных данных:

Regr.fit(X_train, Y_train)

# Смотрим коэфициенты:

print('Coeff: ', Regr.coef_)

predictions = Regr.predict(X_test)

# Предсказываем тестовую выборку Y test:

regr_graph = sns.scatterplot(x = Y_test, y = predictions, hue = predictions, legend=False, palette='viridis')
regr_graph.set(xlabel='Y Test', ylabel='Predicted Values')
