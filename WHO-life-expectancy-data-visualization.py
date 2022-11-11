# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:01:09 2022

@author: Srinivas
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

# Reading csv files using pandas and viewing dataframe
df = pd.read_csv("C:/Users\Srinivas\Documents\DataSets\WHO-LifeExpectancy_DataSet.csv")
df.info()

# # checking the null values in the dataset and describing the data
# df.isnull().sum() 
# df.describe()




df1 = df.groupby(by=["Country"]).sum()

print(df1)

# def lineplot(x):
#     return
    

# x = np.linspace(-10, 10, 100)
# x = df['Year'],df['Life expectancy']
plt.figure()

plt.plot(df1['Year'],df1['Life expectancy '], color='red')

plt.show()


# def lineplot():
#     #plt.plot(df1['Year'],df1['Life expectancy '], color='red')
#     df1.plot(x= "Country Name", y=['2019','2020','2021'],figsize = (15,5))
#     plt.suptitle("Primary completion rate, female (% of relevant age group)")
#     plt.xlabel("Country Name")    #xlabels asign the value year
#     plt.ylabel("2019 , 2020 , 2021")   #ylabels asign the value Sales
#     plt.legend()
    
# lineplot






