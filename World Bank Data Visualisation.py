"""
Created on Fri Nov  4 23:35:01 2022

@author: Srinivas
"""

"""
1. Produce a line plot showing multiple lines with proper labels and legend. 
Describe what conclusions you can draw from this plot. 

2. Produce graphs using two other visualisation methods. 
Explain why you picked this type of graph and describe what conclusions you can draw.

"""
# Graphs only with   pyplot
# Read only data with   Pandas
# The code should make good use of   functions. 
# The minimum expected would be one for each visualisation method.
# Best, if you write the functions in a generalised way so that they can be used more than once. 
# Do not forget to put a short explanatory docstring at the beginning of the function.
# Repeated repo commitments 

import pandas as pd
import matplotlib.pyplot as plt

path1 = "C:/Users/Srinivas/Excel_FIles/API_EG.ELC.ACCS.ZS_DS2_en_excel_v2_4697534.xls"
path2 = "C:/Users\Srinivas\Excel_FIles\API_EG.ELC.RNWX.KH_DS2_en_excel_v2_4522821.xls"


electricity_access = pd.read_excel(path1)
renewable_electricity_excluding_hydro = pd.read_excel(path2)

#countries = ["USA", "DEU", "CHN", "CAN", "BRA", "JPN", "NPL", "IND", "IDN", "WLD"]

df1 = pd.DataFrame(electricity_access)
df2 = pd.DataFrame(renewable_electricity_excluding_hydro)

df1['country']
df2['year']



df = df1.merge(df2, on = "country")
df.coloumns = ["Electricity.acess (%)", "renewable_electricity_excluding_hydro (kWh)"]

plt.title("Electricity access rate in 2010")
plt.xlabel("countries")
plt.ylabel("Electricity access(%)")
plt.axis([0,0, 1,140])

df["Electricity access (%)"].plot(kind = "bar")

# plt.figure()

# plt.show()

