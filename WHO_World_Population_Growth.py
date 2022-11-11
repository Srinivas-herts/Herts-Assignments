"""
Created on Fri Nov 11 11:09:00 2022

@author: Srinivas
"""

""" Comparing the Resuls of world population data between the countries and year wise. 
Below is the code written for reading data sets using pandas and plotting graphs using matplotlib.
Python Functions used for calling them frequently to plot the graphs """

# World Population Growth

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading csv files using pandas
df = pd.read_csv("C:/Users\Srinivas\Documents\DataSets\Population_growth.csv")
df.head(8)

data = df.head(8)


# PLOT 1: Coding for Line Plot
#Creating dataframs 
df1 = data['Years']
df2 = data['Population']
df3 = data['Deaths']


""" Plotted graph below is the lineplot which visualises the data between year vs population and
Year vs Death """

#Defining lineplot function to plot the graph

def lineplot():
    line_graph = plt.plot(df1,df2,df1,df3)
    plt.grid(True)

    l1, l2 = line_graph # split lines  
    
    #Setting more than one property
    plt.setp(l1, linewidth=1, color='r', marker='*') # set function 1 linestyle
    plt.setp(l2, linewidth=1, color='b', marker='*') # set function 2 linestyle
    
    # Labelling the x-axis and y-axis
    plt.ylabel("Population in Billions")
    plt.xlabel("Population growth by year")
    plt.title("Population Growth (Yearly)")
    
    legend_drawn_flag = True
    plt.legend(["Years-Population", "Years-Deaths"], loc=0, frameon = legend_drawn_flag)

lineplot() # Plots the lineplot and displays



""" Plotted graph below is the barplot which visualises the data of 
countries for years vs population """

# PLOT 2: Coding for plot 2

def barplot(): # Defining bar plot

# Accessing columns from Dataset
    alb = data['Countries'] == 'Albania'
    algr = data['Countries'] == 'Algeria'
    astrl = data['Countries'] == 'Australia'
    blrs = data['Countries'] == 'Belarus'
    blgm = data['Countries'] == 'Belgium'
    brz = data['Countries'] == 'Brazil'
    cnd = data['Countries'] == 'Canada'
    chn = data['Countries'] == 'China'

# Defining Data Frames    
    alb_years = data[alb].Years
    alb_pop = data[alb].Population
    
    algr_years = data[algr].Years
    algr_pop = data[algr].Population

    astrl_years = data[astrl].Years
    astrl_pop = data[astrl].Population

    blrs_years = data[blrs].Years
    blrs_pop = data[blrs].Population

    blgm_years = data[blgm].Years
    blgm_pop = data[blgm].Population

    brz_years = data[brz].Years
    brz_pop = data[brz].Population

    cnd_years = data[cnd].Years
    cnd_pop = data[cnd].Population

    chn_years = data[chn].Years
    chn_pop = data[chn].Population

# Plotting the figure and adding axes    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

# Coding for bar Graph  using axis bar method   
    ax.bar(alb_years, alb_pop, color = 'b', width = 0.25)
    ax.bar(algr_years, algr_pop, color = 'g', width = 0.25)
    ax.bar(astrl_years, astrl_pop, color = 'r', width = 0.25)
    ax.bar(blrs_years, blrs_pop, color = 'b', width = 0.25)
    ax.bar(blgm_years, blgm_pop, color = 'g', width = 0.25)
    ax.bar(brz_years, brz_pop, color = 'r', width = 0.25)
    ax.bar(cnd_years, cnd_pop, color = 'b', width = 0.25)
    ax.bar(chn_years, chn_pop, color = 'g', width = 0.25)
    
    # Labelling the x-axis and y-axis
    plt.ylabel("Population in Billions")
    plt.xlabel("Population growth by year")
    plt.title("Population Growth Hike")
    
    # Plotting Legend for the bar graph
    legend_drawn_flag = True
    plt.legend(["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008"],
               loc=0, frameon = legend_drawn_flag)

 
# PLotting Bar Graph 
barplot()



""" Plotted graph below is the Pie Chart which visualises the data of 
countries vs population percentage"""

# PLOT 3: Coding for Pie Chart
df_cntrs = data['Countries'] 
df_pop = data['Population']
 
 
# Creating explode data
explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0, 0.2, 0.0)
 
# Creating color parameters
colors = ( "orange", "cyan", "brown",
          "grey", "indigo", "beige")
 
# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "green" }


# Defining Function and Creating autocpt arguments

def piechart(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(df_pop,
                                  autopct = lambda pct: piechart(pct, df_pop),
                                  explode = explode,
                                  labels = df_cntrs,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, df_cntrs,
          title ="Population Growth (&) by Countries",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Country wise Population Growth (%)")
 
# show plot
plt.show()

