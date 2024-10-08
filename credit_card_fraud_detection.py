# -*- coding: utf-8 -*-
"""credit_card_fraud_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W8zLZkQY_rctgw6TvviWf3IFJTxFZckP
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#load the dataset in the pandas dataframe
credit_card_data = pd.read_csv('/content/creditcard.csv')

#showing the first 5 rows of the dataset
credit_card_data.head()

#showing the last 5 rows
credit_card_data.tail()

#dataset information
credit_card_data.info()

#checking for null values in the columns
credit_card_data.isnull().sum()

#distribution of legit transaction and fraud transaction
credit_card_data['Class'].value_counts()

#this dataset is unbalanced
# 0---> normal transaction
# 1---> fraud transaction

legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)

#statistical measure of the data
legit.Amount.describe()

fraud.Amount.describe()

#compare the values for both transactions
credit_card_data.groupby('Class').mean()

#undersampling
#build a sample dataset containing similar distribution of normal transaction and fraud transaction
#number of fraud transaction = 492
legit_sample = legit.sample(n=492)

#concatinating two dataframes
new_dataset = pd.concat([legit_sample, fraud], axis=0)

new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

#split data into target and features
X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

print(X)

print(Y)

#split the data into training and testing data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=3)

print(X.shape, X_train.shape, X_test.shape)

#model training using logistic regression
model = LogisticRegression()

#training the logistic regression with training data
model.fit(X_train, Y_train)

#model evaluation
#accuracy score
#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data: ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data: ', test_data_accuracy)

