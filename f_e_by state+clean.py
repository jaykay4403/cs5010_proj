#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:39:07 2019

@author: jamie
"""

import pandas as pd

fe = '/Users/jamie/Dropbox/Data Science/CS5010/Semester Project - CS5010/Dataset-MASTER & WIP/data_Jamie/food_environment_jk.xlsx'
fe_dfs = pd.read_excel(fe, sheet_name=None) # sheet_name=None means all tabs imported

# this code counts the # times each state appears and uses the count to
# access the index via .iloc and capture the obesity values for that range
# the obesity values are summed and adde to a dictionary of obesity values per state
# our data frame does not have an index, so I am using the RangeIndex

#u_st = ['AL','AK','AZ'] # this is a test list of states
u_st = fe_dfs['HEALTH'].State.unique() # creates a list of states from 'State' column
loc_1 = 0 # starting value for forst .iloc index #
dict_1 = {} # creates blank dictionary to store state_obesity pairs

for st in u_st: # uses for loop to iterate through the states
    # loc_2 is ending value for range-remember .iloc actually stops at value before end value
    loc_2 = loc_1 + (len((fe_dfs['HEALTH'][fe_dfs['HEALTH']['State'] == st]))) 
    #print (loc_1, loc_2) # prints to check index range for each state
    sum_1 = fe_dfs['HEALTH']['PCT_OBESE_ADULTS13'].iloc[loc_1:loc_2].sum() # totals data for each state using index range
    #print (sum_1) # prints the sum of the values for each state
    loc_1 = loc_2 # moves the ending index to the starting index for next state
    dict_1[st] = sum_1 # adds state key:state sum pair to dictionary

print (dict_1)


# More on using pandas

fe_dfs.keys() # list of tabs in our data frame
fe_dfs['HEALTH'].head() # shows the data from first 5 rows of 'tab' = HEALTH
fe_dfs['HEALTH'].State.unique() # lists the unique values in the column State
len(fe_dfs['HEALTH'].State.unique()) # # states in list = 51 (all states + DC)

# accessing the data
# can use slice notation to access/slice specific data: [5] or [5:12] or [5:] or [:12]
fe_dfs['HEALTH'] # how to show/access an entire tab
fe_dfs['HEALTH']['State'] # how to access by column name
fe_dfs['HEALTH'].State #how to access via dot notation (also called attribute access)


# ['State'] is regular by column name (pandas refers to ['State'] as column name
print (fe_dfs['HEALTH'][fe_dfs['HEALTH']['State'] == 'AL']) # prints rows with AL

print (fe_dfs['HEALTH'][fe_dfs['HEALTH']['State'] == 'AL'].shape[0]) #returns tuple with fame dimensionality
print (len((fe_dfs['HEALTH'][fe_dfs['HEALTH']['State'] == 'AL']))) # print # rows with AL

# .State =  column selection with dot notation (also called attribute access)
print (fe_dfs['HEALTH'][fe_dfs['HEALTH'].State == 'AL']) # prints rows with AL
print (len((fe_dfs['HEALTH'][fe_dfs['HEALTH'].State == 'AL']))) # print # rows with AL

