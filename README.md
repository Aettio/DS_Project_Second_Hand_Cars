# Data science | Project : "Second Hand Cars"

## Project guide

Before the beginning:
- "README.txt" - Contains the project itself with visualizations. It is assumed that the reader will view it as the main input file.
- "DataFrames" - Contains all data sets.
- "Images" - Contains all the pictures "README.txt".
- "Code_Visual" - Contains the code for the entire visual.
- "Code_Regression" - Contains the regression algorithm itself.

p.s. Additional notes have been made throughout the code for ease of reading and understanding.

## Sections

- Introduction
- A task
- Exploratory Data Analysis (Data analysis, more details can be viewed in Code_Visuals.py)
  - Search for correlations
  - Visualization
- Linear Regression (More details can be viewed in Code_Regression.py)
  - Model training
  - Prediction
- Total
- Sources

## Introduction

A selection of data on used cars and their prices from the Kaggle website.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/Cars_picture.jpg)

## A task

Analyze the dataset and make a prediction of a random sample.

## EDA (Exploratory Data Analysis)

After cleaning the data, it was necessary to highlight the main dependencies and conduct a small analysis of the relationships. You also need to be sure that they make sense. To start the analysis, I chose a graph to visualize correlations.

# Correlations

On this chart, we should immediately note several interesting correlations with the "current price".

- "km"
- "on road now"
- "on road old"

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/Корреляции.png)

# Check 1 "current price" and "km"

Here we test for negative correlation. On this chart, we confirm for ourselves the direct dependence of "current price" on "km" and the larger the second value, the smaller the first value.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/CPrice_km.png)

# Check 2 "current price" and "on road now"

Further, we have a not entirely obvious correlation between "current price" and "on road now", but still it exists.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/CPrice_on_road_now.png)

# Check 3 "current price" and "on road old"

As in the previous graph, there is a correlation, but minimal.

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/CPrice_on_road_old.png)


## Linear regression

After splitting the sample into training and test, we train on the selected data. Then we predict our test sample "Y test".

![alt text](https://github.com/Aettio/DS_Project_Second_Hand_Cars/blob/main/Images/Linear_Regression.png)

## Total

Our linear regression is able to predict a random sample of used car data. We also determined that the distance traveled by it has the greatest influence on the cost of the car.

## Sources

- Dataset : https://www.kaggle.com/mayankpatel14/second-hand-used-cars-data-set-linear-regression
- Seaborn documentation : https://seaborn.pydata.org/introduction.html
- Sklearn documentation : https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
