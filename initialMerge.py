import pandas as pd
import difflib
import numpy as np


columns_to_keep = ['leaid', 'year', 'lea_name', 'phone', 'urban_centric_locale', 'number_of_schools', 'enrollment',
                   'teachers_total_fte', 'race', 'rev_total', 'rev_fed_total', 'rev_state_total', 'rev_local_total',
                   'exp_total', 'exp_current_instruction_total', 'outlay_capital_total', 'payments_charter_schools',
                   'salaries_instruction', 'benefits_employee_total', 'debt_interest', 'debt_longterm_outstand_end_fy',
                   'debt_shortterm_outstand_end_fy', 'est_population_5_17_poverty_pct']


# Read all of the CSV files
##Education Data Portal
'''
df1 = pd.read_csv("/Users/matthewuytioco/Downloads/school-districts_lea_directory.csv")

df1 = df1[df1['year'] >= 2008]
df1 = df1[df1['state_mailing'].str.contains('CA', na=False)]
print(df1['state_mailing'])

df1.columns = df1.columns.str.lower()

df1 = df1.filter(columns_to_keep)

df1['leaid'] = df1['leaid'].astype(str)

df1['year'] = df1['year'].astype(int)

print(len(df1))

#df1.to_csv('education_1.csv', index=False)

df2 = pd.read_csv("/Users/matthewuytioco/Downloads/districts_ccd_finance (1).csv")
df2 = df2[df2['year'] >= 2008]
df2.columns = df2.columns.str.lower()
df2 = df2.filter(columns_to_keep)
df2['leaid'] = df2['leaid'].astype(str)
df2['year'] = df2['year'].astype(str)
print(len(df2))
df2.to_csv('education_2.csv', index=False)

'''

df1 = pd.read_csv("/Users/matthewuytioco/PycharmProjects/practicum_final_merge/education_1.csv")
df2 = pd.read_csv("/Users/matthewuytioco/PycharmProjects/practicum_final_merge/education_2.csv")

df1['leaid'] = df1['leaid'].astype(str)
df2['leaid'] = df2['leaid'].astype(str)



#df1['secured_net taxable value'] = None
#df1['unsecured_net taxable value'] = None
counter = 0
columns = df1.columns.tolist() + df2.columns.tolist()
merged_df = pd.DataFrame(columns=columns)
for i in range(0, len(df1)):
    target = df1.iloc[i]['leaid']
    #target = target.lower()
    target_y = df1.iloc[i]['year'].astype(str)
    print(i, target_y,  target)
    new_df = df2[df2['year'] == int(target_y)]
    best_match = None
    best_ratio = 0
    for k in range(0, len(new_df)):
        df2_name = new_df.iloc[k]['leaid']
        diff = difflib.SequenceMatcher(None, target, df2_name)
        ratio = diff.ratio()
        if (ratio >= 0.92):
            counter += 1
            print(i, target, df2_name, counter, target_y)

            if ratio > best_ratio:
                best_ratio = ratio
                best_match = new_df.iloc[k].copy()
    if best_match is not None:
        new_row = pd.concat([df1.iloc[[i]].reset_index(drop=True),
                             best_match.to_frame().T.reset_index(drop=True)], axis=1)
        merged_df = pd.concat([merged_df, new_row], ignore_index=True)

merged_df.to_csv('education_test_final.csv', index=False)






'''
df2 = pd.read_csv("/Users/matthewuytioco/Downloads/districts_ccd_finance (1).csv")
df3 = pd.read_csv("/Users/matthewuytioco/Downloads/districts_saipe.csv")
#df4 = pd.read_csv()


##State Controller
df5 = pd.read_csv("/Users/matthewuytioco/Downloads/PropertyTax_DataSet_2019-20_to_2023-24_20240421_V1.csv")
df6 = pd.read_csv("/Users/matthewuytioco/Downloads/PropertyTax_DataSet_20190513.csv")
print(df2.columns)


#Cleaning Education Data Portal Data
df1 = df1[df1['year'] >= 2008]
df1 = df1[df1['state_mailing'].str.contains('CA', na=False)]
print(df1['state_mailing'])

df2 = df2[df2['year'] >= 2008]
#df2 = df2[df2['state_mailing'].str.contains('CA', na=False)]

df3 = df3[df3['year'] >= 2008]
#df3 = df3[df3['state_mailing'].str.contains('CA', na=False)]

#df4 = df[df['year'] >= 2008]
#df4 = df[df['state_mailing'].str.contains('CA', na=False)]

#Remove
df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()
df3.columns = df3.columns.str.lower()
#df4.columns = df4.columns.str.lower()





df1 = df1.filter(columns_to_keep)
df2 = df2.filter(columns_to_keep)
df3 = df3.filter(columns_to_keep)
#df4 = df1.filter(columns_to_keep)


df1['leaid'] = df1['leaid'].astype(str)
df2['leaid'] = df2['leaid'].astype(str)
df3['leaid'] = df3['leaid'].astype(str)
#df4['leaid'] = df4['leaid'].astype(str)



df1['year'] = df1['year'].astype(str)
df2['year'] = df2['year'].astype(str)
df3['year'] = df3['year'].astype(str)
#df4['year'] = df4['year'].astype(str)
print(len(df1))

df_merged1 = pd.merge(df1, df2, on=['leaid', 'year'], how='inner')
print(len(df_merged1))
df_merged2 = pd.merge(df_merged1, df3, on=['leaid', 'year'], how='inner')
#df_merged3 = pd.merge(df_merged2, df4, on=['leaid', 'year'], how='inner')


df_merged2.to_csv('testing_merge.csv', index=False)





#outline which variables to keep
columns_to_keep2 = ['fiscal year', 'name of school district', 'secured_net taxable value',
                    'unsecured_net taxable value']

#lowercase all text
df5.columns = df5.columns.str.lower()
df6.columns = df6.columns.str.lower()


df5 = df5.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
df5 = df5.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)

#rename columns in second data set
df6 = df6.rename(columns= {'school district name': 'name of school district',
                           'secured - net taxable value_school districts property taxes': 'secured_net taxable value',
                            'unsecured - net taxable value_school districts property taxes': 'unsecured_net taxable '
                                                                                             'value'})

#filter data sets to only include key variables
df5 = df5.filter(columns_to_keep2)
df6 = df6.filter(columns_to_keep2)

df5['fiscal year'] = df5['fiscal year'].astype(str)
df6['fiscal year'] = df6['fiscal year'].astype(str)


#concatenate both data sets
df_merged3 = pd.concat([df5, df6], ignore_index=True)
#drop unnecceasry duplicates
df_merged3 = df_merged3.drop_duplicates(subset=['fiscal year', 'name of school district'], keep='first')


df_merged3.to_csv('testing_merge_ca_state_cont.csv', index=False)

'''






