# Data science | Project : "Second Hand Cars"

## Гайд по проекту

Перед началом:
- "README.txt" - Содержит сам проект с визуализациями. Предпологаеться что читатель и будет смотреть его как основной файл на входе.
- "DataFrames" - Содержит в себе все дата сеты.
- "Images" - Содержит в себе все картинки "README.txt".
- "Code_Visual" - Содержит в себе код для всего визуала.
- "Code_Regression" - Содержит в себе сам алгоритм регресии.

p.s. Во всём коде дополнительно были сделаны заметки для удобства чтения и понимания.

## Разделы

- Введение
- Задача
- Exploratory Data Analysis (Анализ данных, более подробно можно просмотреть в Code_Visuals.py)
  - Поиск корреляций
  - Визуализация
- Линейная регрессия (Более подробно можно просмотреть в Code_Regression.py)
  - Тренеровка модели
  - Предсказание
- Итог
- Источники

## Введение

Выборка Данных по Б/У машинам и их ценам с сайта Kaggle.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/Cars_picture.jpg)

## Задача

Проанализировать датасет и сделать предсказание выборки.

## EDA (Exploratory Data Analysis)

После чистки данных нужно было выделить основные зависимости и провести небольшой анализ взаимосвязей. Также нужно быть уверенным в том что они имеют смысл. Для начала анализа мною был выбран график для визуализации корреляций.

# Корреляции 

На этом графике сразу стоит отметить несколько интересных нам корреляций с "current price".

- "km"
- "on road now"
- "on road old"

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/Корреляции.png)

# Проверка 1 "current price" и "km"

Тут мы проверяем отрицательнаую корреляцию. На данном графике мы подтверждаем для себя прямую зависимость "current price" от "km" и чем второе значение больше, тем первое значение меньше.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/CPrice_km.png)

# Проверка 2 "current price" и "on road now"

Тум мы имеем не совсем очевидную корреляцию, между "current proce" и "on road now", но всё же она имеется. 

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/CPrice_on_road_now.png)

# Проверка 3 "current price" и "on road old"

Как и на предыдущем графике корреляция есть, но минимальная.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/CPrice_on_road_old.png)


## Линейная регрессия

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/Linear_Regression.png)

## Итог

## Источники

- Датасет : https://www.kaggle.com/datasets
- Seaborn документация : https://seaborn.pydata.org/introduction.html
