import difflib
import pandas as pd
import numpy as np

'''
df1 = pd.read_csv("eeducation portal data")
df2 = pd.read_csv("finance data")


add two columns to df1

for i in range(0, len(df1)):
    select target (lowercase)

    new df = df2 filtered for taget year
    for k in range(0, len(new df)):
        pull string from k (lowercase it)
        diff = difflib.SequenceMatcher(None, string1, string2)
        ratio = matcher.ratio()
        if(ratio >= 0.80):
            add the data from finance to df1
            break
'''

df1 = pd.read_csv('/Users/matthewuytioco/PycharmProjects/practicum_final_merge/testing_merge.csv')
df2 = pd.read_csv('/Users/matthewuytioco/PycharmProjects/practicum_final_merge/testing_merge_ca_state_cont.csv')

df1['secured_net taxable value'] = None
df1['unsecured_net taxable value'] = None

for i in range(0, len(df1)):
    target = df1.iloc[i]['lea_name']
    target = target.lower()
    target_y = df1.iloc[i]['year']

    new_df = df2[df2['fiscal year'] == int(target_y)]
    for k in range(0, len(new_df)):
        df2_name = target_y.iloc[k]['name of school district'].lower()
        diff = difflib.SequenceMatcher(None, target, df2_name)
        ratio = diff.ratio()

