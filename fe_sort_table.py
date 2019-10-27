#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:44:05 2019

@author: jamie
"""

import pandas as pd

## Part I - extract .xlxs to data frame
# code extracts Excel file to a data frame - linked to MASTER file for testing
# all tabs extracted into an array (not one big spreadsheet)
fe = '/Users/jamie/Dropbox/Data Science/CS5010/Semester Project - CS5010/Dataset-MASTER & WIP/data_Jamie/food_environment_jk.xlsx'
fe_dfs = pd.read_excel(fe, sheet_name=None) # sheet_name=None means all tabs imported

# this code counts the # times each state appears and uses that count to
# access the index via .iloc and capture the obesity values for that range
# the obesity values are summed and adde to a dictionary of obesity values per state
# our data frame does not have an index, so I am using the RangeIndex


## Part II - Iterate through state labels to count # occurances - use the # occurances
# with .iloc to select an index range, and sum values corresponding to each state's
# labels - state:value pairs are stored in dictionary dict_1

#u_st = ['AL','AK','AZ'] # this is a test list of 3 states
u_st = fe_dfs['HEALTH'].State.unique() #  list of unique states from 'State' column
loc_1 = 0 # starting value for first .iloc index #
dict_1 = {} # creates blank dictionary to store state:obesity pairs

for st in u_st: # uses for loop to iterate through the unique states list
    # loc_2 is ending value for range-remember .iloc actually stops at value before end value
    loc_2 = loc_1 + (len((fe_dfs['HEALTH'][fe_dfs['HEALTH']['State'] == st]))) 
    #print (loc_1, loc_2) # prints to check index range for each state
    sum_1 = fe_dfs['HEALTH']['PCT_OBESE_ADULTS13'].iloc[loc_1:loc_2].sum() # totals data for each state using index range
    #print (sum_1) # prints the sum of the values for each state
    loc_1 = loc_2 # moves the ending index to the starting index for next state
    dict_1[st] = round (sum_1, 1) # adds state key:state sum pair to dictionary

print (dict_1)  # print to see horizintal view of dictionary
dict_1          # run this to see columnar view of dictionary


## Part III - Sort values in dictionary dict_1 in ascending or descending order and
# create a 2nd dictionary dict_2 holding the top x obs-rows (top 5, 10, whatever),
# where x is picked by the
# containing the top 
# Lines below sort ascending (asc)/descending (des) - comment/uncomment
# Also comment/uncomment for loop below so set to match ascending/descending
StObesPairs_asc = sorted(dict_1.items(), key=lambda x: x[1]) # sort tuples in ascending order
#StObesPairs_des = sorted(dict_1.items(), reverse=True, key=lambda x: x[1]) # sort tuples in ascending order

count = 0
dict_2 = {}
top_num_obs = input('How many rows to show (ie top 5, 10) where max=51)?  ')

# comment/uncomment this code to extract results in ascendingdescending order
for elem in StObesPairs_asc:
#for elem in StObesPairs_des:
    print (elem[0], "     " , elem[1])
    dict_2[elem[0]] = elem[1]
    count += 1
    if count == int(top_num_obs):
        break

dict_2   #uncomment and run this code -the anme of the dictionary to see contents


## Part IV - screen & file output
# run this code to output to screen - lists # of rows selected and 2 columns data
print (('List of the top: ') + str(count))
print ('State', '% Obese')
for Table, PCT_OBESE_ADULTS13 in dict_2.items():
    print('  {}    {}'.format(Table, PCT_OBESE_ADULTS13))
    

# Findings to share - state columnin dict_2 is index - not sure of I did it or pandas
# this is different from df we started with: here .iloc will refer to state column,
# not the numeric index


# run this code to output to screen & to create df for export to Excel
# Converts dict_2 dictionary to data frame with columns as labeled
# Col 1-State is actually the index - header-label handled differently for index
# Col 2 is regular column and can be relabled using column code
# Note that index-column difference means each header outputs to a different line
# on screen - looks odd on screen - outputs correctly to Excel!
# Also note that if you are runing this alot, the dictionary object may need to 
# be cleared so it exports to Excel correctly-to clear, uncomment line below & run 1x
#sum_table_df = {}

sum_table_df = pd.DataFrame.from_dict(dict_2, orient='index')
sum_table_df.index.name = 'State' # relabels col 1 header, which is the index here
sum_table_df.columns = ['% Obese'] # relabels col 2 header
sum_table_df # run this line to see df object to confirm looks as intended

# outputs df to Excel file for use in our report
with pd.ExcelWriter('sum_table_out.xlsx') as writer: #create file for data frame
    sum_table_df.to_excel(writer) # export data frame to Excel

sum_table_df = {}


## Testing only ==> notqc'd - write dictionary to file not a table (that was goal)
# write ranked data to file-test <==check this code is writing dict multiple times
glfile = open('st_obtable.txt', 'w+') # test write w+ dictionary to txt file
for Table, PCT_OBESE_ADULTS13 in dict_2.items():
    print('{}     {}'.format(Table, PCT_OBESE_ADULTS13))
    glfile.write(str(dict_2))
glfile.close() 


## Testing only ==> do not use - install tabulate library
# print data out in pretty table<==TypeError: zip_longest argument #1 must support iteration
# this is a problem with index - zip() might solve
from tabulate import tabulate
print (tabulate(dict_2, headers=["State", "% Obese"]))


## Testing only ==> do not use - install tabulate library
sum_table_df = pd.DataFrame.from_dict(dict_2, orient='index', columns=['State' , '% Obese'])


## 2 different kinds of dictionaries ==> this is not working
# (1) something to discuss: dictionary with states as keys vs (2) a dictionary with
# 2 keys: a 'state' key with state names and a 'values' key which holds alll values
# the code below works with scenario #2
sum_table_df_1 = pd.DataFrame(dict_2).set_index('Index Title').rename_axis('State1', axis=1)
sum_table_df_1


print("\n>>> Dictionary printed to .txt file - now back to screen.<<<")

fe_dfs['HEALTH']['State'].columns() # how to access by column name
fe_dfs['HEALTH'].State.columns.values

    
StObesPairs_des = sorted(dict_1.items(), reverse=True, key=lambda x: x[1]) # sort tuples in ascending order

for elem in StObesPairs_des:
    print (elem[0], " ::" , elem[1])