#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:08:15 2018

@author: luoxue
"""

### ASSIGNMENT 3
# import codes to plot histogram
import sys
sys.path.append("/Users/luoxue/Desktop/HU/ANLY 545 Analytical Methods II/ThinkStats2-master/code/")
import thinkstats2 
import thinkplot  
import matplotlib.pyplot as plt
import numpy as np


# open file
F = open("/Users/luoxue/Desktop/HU/ANLY 545 Analytical Methods II/Assignments/Assignment 3/student-mat.csv", "r")
# set up new list
Mothereducation = list()
absences  = list()
familyrelationships= list()
finalmathgrade=list()
# read data by column

list2 = [1, 2, 3, 4, 5 ]
print(list)

for line in F:
    spLine = line.split(",")
    Mothereducation.append(spLine[6])# read the 7th column "Mother's education"
    absences.append(spLine[29])# read the 30th column "absences"
    familyrelationships.append(spLine[23])# read the 24th column "famrel"
    finalmathgrade.append(spLine[32])# read the 33rd column "G3"

 # excluding 1st item (column title)
Mothereducation = Mothereducation[1:len(Mothereducation)]   # len() means count total items
Mothereducation=map(int,Mothereducation)
absences= absences[1:len(absences)]  
absences=map(int,absences) # convert a list of strings to lisdt of integers
familyrelationships= familyrelationships[1:len(familyrelationships)] 
familyrelationships=map(int,familyrelationships) # convert a list of strings to lisdt of integers
finalmathgrade = finalmathgrade[1:len(finalmathgrade)] 
finalmathgrade=map(int,finalmathgrade) # convert a list of strings to lisdt of integers  
    

# histogram
hist1 = thinkstats2.Hist(Mothereducation)
print(hist1)
hist2= thinkstats2.Hist(sorted(absences))
print(sorted(absences))
print(hist2)
hist3= thinkstats2.Hist(familyrelationships)
print(hist3)
hist4= thinkstats2.Hist(finalmathgrade)
print(hist4)

# plot histogram
thinkplot.Hist(hist1)
thinkplot.Show(xlabel="Mother's education", ylabel="Frequency", main="Mother's education")

thinkplot.Hist(hist2)
thinkplot.Show(xlabel="absences", ylabel="Frequency", main="Number of days that the student was absent")

thinkplot.Hist(hist3)
thinkplot.Show(xlabel="family relationships", ylabel="Frequency", main="quality of family relationships")

thinkplot.Hist(hist4)
thinkplot.Show(xlabel="grade", ylabel="Frequency", main="final math grade")

plt.hist(absences)
