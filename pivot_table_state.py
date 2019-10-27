#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:53:16 2019

@author: jamie
"""
import pandas as pd

# data set to df
fe = '/Users/jamie/Dropbox/Data Science/CS5010/Semester Project - CS5010/Dataset-MASTER & WIP/data_Jamie/food_environment_jk.xlsx'
fe_dfs = pd.read_excel(fe, sheet_name=None) 

# how to link to columns
fe_dfs['HEALTH']['State']
fe_dfs['Supplemental Data - County']['Population Estimate, 2013']
fe_dfs.keys() # list of tabs to confirm

# .head works with string (that has commas)
# use pivot_table to sort top 10 - assumes top 10 are strings
fe_dfs['HEALTH'].pivot_table(index='State', values = 'PCT_OBESE_ADULTS13', aggfunc = \
      'sum').sort_values(by = 'PCT_OBESE_ADULTS13').head(10)

# use pivot_table to sort top 10 largest - assumes top 10 are intergers
fe_dfs['HEALTH'].pivot_table(index='State', values = 'PCT_OBESE_ADULTS13', aggfunc = \
      'sum').sort_values(by = 'PCT_OBESE_ADULTS13').nlargest(10, 'PCT_OBESE_ADULTS13')

# use pivot_table to sort top 10 smallest - assumes top 10 are intergers
fe_dfs['HEALTH'].pivot_table(index='State', values = 'PCT_OBESE_ADULTS13', aggfunc = \
      'sum').sort_values(by = 'PCT_OBESE_ADULTS13').nsmallest(10, 'PCT_OBESE_ADULTS13')


# pd.to_numeric(fe_dfs['Supplemental Data - County']['Population Estimate, 2011']) 
type(fe_dfs['Supplemental Data - County']['Population Estimate, 2014']) #type of data on column


# remove commas ==> confirm whether #1 or #2 is best - #2 seems best right now
# #1-use this convert to interger use .nslargest/.nssmallest<==do not use-use #2
#pd.to_numeric(fe_dfs['HEALTH']['PCT_OBESE_ADULTS13']) #convert

# #2-remove commas and convert to float <== sorts below will not work unless run #2
fe_dfs['Supplemental Data - County']['Population Estimate, 2015'] =\
fe_dfs['Supplemental Data - County']['Population Estimate, 2015'].str.replace(',', '').astype(float)

# #2-remove commas from string data so can convert to interger ==> data type problem
#fe_dfs['Supplemental Data - County']['Population Estimate, 2011'] = fe_dfs\
#['Supplemental Data - County']['Population Estimate, 2011'].str.replace(',', '')

# all 3 extract-sorts below work work after running comma replace convert to string
#num_obs = input('How many rows to show (ie top 5, 10) where max=51)?  ')
fe_dfs['Supplemental Data - County'].pivot_table(index='State', values = 'Population Estimate, 2015', aggfunc = \
      'sum').sort_values(by = 'Population Estimate, 2015').head(10)

fe_dfs['Supplemental Data - County'].pivot_table(index='State', values = 'Population Estimate, 2015', aggfunc = \
      'sum').sort_values(by = 'Population Estimate, 2015').nlargest(10, 'Population Estimate, 2015')

fe_dfs['Supplemental Data - County'].pivot_table(index='State', values = 'Population Estimate, 2015', aggfunc = \
      'sum').sort_values(by = 'Population Estimate, 2015').nsmallest(10, 'Population Estimate, 2015')


# use if need to output to file or Excel
x99=fe_dfs['Supplemental Data - County'].pivot_table(index='State', values = 'Population Estimate, 2015', aggfunc = \
      'sum').sort_values(by = 'Population Estimate, 2015').nsmallest(10, 'Population Estimate, 2015')
x99

# write to output file
pfile = open('st_table.txt', 'w+') # test write w+ dictionary to txt file
pfile.write(str(x99))
pfile.close() 

# outputs df to Excel file for use in our report
with pd.ExcelWriter('sum_tbl_out.xlsx') as writer: #create file for data frame
   x99.to_excel(writer) # export data frame to Excel


# this code is attempt to change data column to # with 0 decimal places & commas
#fe_dfs['Supplemental Data - County'].pivot_table(index='State', values = 'Population Estimate, 2015', aggfunc = \
#      'sum').sort_values(by = 'Population Estimate, 2015').style.format("{:,.0f}")




# WIP - do not use
# 3d pivot table
fe_dfs['HEALTH'].pivot_table(index='State', columns = x_1, values = 'PCT_OBESE_ADULTS13', aggfunc = \
      'sum').head(10)


x_1 = pd.cut(fe_dfs['HEALTH']['PCT_DIABETES_ADULTS13'],5, labels = ['Top 20%', 'Top 40', "Top 60" , 'Top 80', 'Top 100'])
x_1


pd.to_numeric(fe_dfs['Supplemental Data - County']['Population Estimate, 2013']) 
pd.to_numeric(list(x1))
x1.style.format("{:,.0f}")

# this works after removing comma
pd.to_numeric(fe_dfs['Supplemental Data - County']['Population Estimate, 2012'])#, errors='coerce')#.astype('int') # float = f

pd.astype(fe_dfs['Supplemental Data - County']['Population Estimate, 2013']) 

# remove commas from string data so can convert to interger
fe_dfs['Supplemental Data - County']['Population Estimate, 2013'] = fe_dfs\
['Supplemental Data - County']['Population Estimate, 2013'].str.replace(',', '')

# remove $ from string data so can convert to interger
#fe_dfs['Supplemental Data - County']['Population Estimate, 2013'] = fe_dfs\
#['Supplemental Data - County']['Population Estimate, 2013'].str.replace('$', '')

# convert column to interger - don't use changes 1st value in col 2 to NaN
fe_dfs['Supplemental Data - County']['Population Estimate, 2013'] = \
fe_dfs['Supplemental Data - County']['Population Estimate, 2013'].astype('int')

# to add commas to #'s in column
fe_dfs['Supplemental Data - County']['Population Estimate, 2013'].style.format("{:,.0f}")
# .style.format('${0:,.2f}'))  # add dollar signs


