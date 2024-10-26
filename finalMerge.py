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

df1 = pd.read_csv('/Users/matthewuytioco/PycharmProjects/practicum_final_merge/education_test_final.csv')
df2 = pd.read_csv('/Users/matthewuytioco/PycharmProjects/practicum_final_merge/testing_merge_ca_state_cont.csv')

df1['secured_net taxable value'] = None
df1['unsecured_net taxable value'] = None
columns = df1.columns.tolist() + df2.columns.tolist()
merged_df = pd.DataFrame(columns=columns)
counter = 0
ignore_words = ["unified"]

for i in range(0, len(df1)):
    target = df1.iloc[i]['lea_name'].lower()
    target = target.lower()
    target_y = df1.iloc[i]['year']
    #print(i, target_y,  target)
    for word in ignore_words:
        target = target.replace(word, "").strip()
    new_df = df2[df2['fiscal year'] == int(target_y)]

    best_match = None
    best_ratio = 0

    for k in range(0, len(new_df)):
        df2_name = new_df.iloc[k]['name of school district'].lower()
        for word in ignore_words:
            df2_name = df2_name.replace(word, "").strip()
        diff = difflib.SequenceMatcher(None, target, df2_name)
        ratio = diff.ratio()
        if (ratio >= 0.92):
            counter += 1
            print(i, new_df.iloc[k]['fiscal year'], df2_name, counter)
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = new_df.iloc[k].copy()
    if best_match is not None:
        new_row = pd.concat([df1.iloc[[i]].reset_index(drop=True),
                            best_match.to_frame().T.reset_index(drop=True)], axis=1)
        merged_df = pd.concat([merged_df, new_row], ignore_index=True)

merged_df.to_csv('final_data.csv', index=False)
#print(counter)
