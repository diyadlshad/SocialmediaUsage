# Load the necessary packages

import numpy as np
import pandas as pd

# Load the Cardio Dataset

mydata = pd.read_csv('socialmediausage.csv')

import matplotlib.pyplot as plt
#matplotlib inline

mydata.hist(figsize=(20,30))

import seaborn as sns

sns.boxplot(x="Gender", y="Age", data=mydata)

pd.crosstab(mydata['social media'],mydata['Gender'] )
sns.countplot(x="martial status", hue="Gender", data=mydata)

pd.pivot_table(mydata, index=['martial status', 'Gender'],
                     columns=[ 'Gender'], aggfunc=len)

pd.pivot_table(mydata,'Income', index=['martial status', 'Gender'],
                     columns=[ 'MaritalStatus'])

pd.pivot_table(mydata,'Age', index=['martial status', 'Usage'],
                     columns=[ 'education level'])


sns.pairplot(mydata)

mydata['Age'].mean()

sns.distplot(mydata['Age'])

mydata.hist(by='Gender',column = 'Age')

mydata.hist(by='Age',column = ' social media usage', figsize=(20,30))

corr = mydata.corr()

sns.heatmap(corr, annot=True)


