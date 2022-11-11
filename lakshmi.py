#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 02:47:26 2022

@author: asus
"""
#imported modules
import pandas as pd
import matplotlib.pyplot as plt

# function for line plot
def line() :
    """
     Function for the line plot showing number of murders in 2014 and 2015. 
    """
# Plot the figure
    plt.figure(figsize = (10,12))
# plot the number of mrders in 2014 and 2015 and the difference.
    plt.plot(new_df["state"], new_df["2014_murders"], 
             label = "2014_murders")
    plt.plot(new_df["state"], new_df["2015_murders"], 
            label = "2015_murders")
    plt.plot(new_df["state"], new_df["change"], 
            label = "change")
   
# set labels and show the legend
    plt.xlabel("State")
    plt.ylabel("number of murders")
    plt.legend()
    plt.title("murders in 2014 and 2015")
# saving figure
    plt.savefig("linegraph.png")
    plt.show()
    

def bar() : 
    """
     Function for the bar with subplots showing changes in 2015 and 2016. 
    """
    new =df1[0:5]
    new_df =df[0:5]
    plt.figure(figsize = (10,13))
    
# subplot
    plt.subplot(2, 2, 1)
    plt.subplots_adjust(left=0.1, bottom= 0.1, right=0.9,top= 1.0,wspace=0.4,hspace=0.4)
    plt.bar(new["state"], new["change"], 
            label = "change", alpha = 1.0, color = 'orange')
    plt.xticks(rotation=90)
    plt.title("Bar graph showing changes in 2015 ")
    plt.xlabel("Station.City")
    plt.ylabel("Number of murders")
    plt.legend()
    
# subplot   
    plt.subplot(2, 2, 2)
    plt.bar(new_df["state"], new_df["change"], 
            label = "change", alpha = 1.0, color = 'green')
    plt.xticks(rotation=90)
    plt.xlabel("State")
    plt.ylabel("Number of murders")
    plt.title("Bar graph showing changes in 2016")
    plt.savefig("barchart_png")
    plt.legend()
    plt.show()



def box() :
    """
    Function for the box plot. It plots the number of murders n 2014 and 2015
    """
# plot the figure
    plt.figure(figsize = (8,9))
    plt.boxplot([new_df["2015_murders"],
                 new_df["2014_murders"],
                ], 
                labels = ["2014_murders",
                          "2015_murders",
                         ])
 
# set labels and show the legend
    plt.xlabel("State")
    plt.ylabel("Number of murders")
    plt.title("Box plot showing murders in 2014 and 2015")
    plt.savefig("boxfig_png")
    plt.legend()
    plt.show()

# read the data and print it
df = pd.read_csv("murder_2015_final.csv")
df1 = pd.read_csv("murder_2016_prelim.csv")
print(df1)
print(df)

# data selected from the dataset
new_df = df[0:10]
new = df1[0:10]

#calling the functions
box()
line()
bar()