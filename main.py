import pandas as pd


columns_to_keep = ['leaid', 'year', 'lea_name', 'phone', 'urban_centric_locale', 'number_of_schools', 'enrollment',
                   'teachers_total_fte', 'race', 'rev_total', 'rev_fed_total', 'rev_state_total', 'rev_local_total',
                   'exp_total', 'exp_current_instruction_total', 'outlay_capital_total', 'payments_charter_schools',
                   'salaries_instruction', 'benefits_employee_total', 'debt_interest', 'debt_longterm_outstand_end_fy',
                   'debt_shortterm_outstand_end_fy', 'est_population_5_17_poverty_pct']


# Read all of the CSV files
##Education Data Portal
df1 = pd.read_csv("/Users/matthewuytioco/Downloads/school-districts_lea_directory.csv")
df2 = pd.read_csv("/Users/matthewuytioco/Downloads/districts_ccd_finance.csv")
df3 = pd.read_csv("/Users/matthewuytioco/Downloads/districts_saipe.csv")
#df4 = pd.read_csv()


##State Controller
df5 = pd.read_csv("/Users/matthewuytioco/Downloads/PropertyTax_DataSet_2019-20_to_2023-24_20240421_V1.csv")
df6 = pd.read_csv("/Users/matthewuytioco/Downloads/PropertyTax_DataSet_20190513.csv")
print(df2.columns)


#Cleaning Education Data Portal Data
df1 = df1[df1['year'] >= 2008]
df1 = df1[df1['state_mailing'].str.contains('CA', na=False)]

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

#df1 = df1.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
#df2 = df2.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
#df3 = df3.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
#df4 = df4.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)



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


df_merged1 = pd.merge(df1, df2, on=['leaid', 'year'], how='inner')
df_merged2 = pd.merge(df_merged1, df3, on=['leaid', 'year'], how='inner')
#df_merged3 = pd.merge(df_merged2, df4, on=['leaid', 'year'], how='inner')

#df_merged2 = df_merged2.drop_duplicates(subset=['leaid', 'year'], keep='first')

df_merged2.to_csv('testing_merge.csv', index=False)
#df3.to_csv('testing_merge3.csv', index=False)











columns_to_keep2 = ['fiscal year', 'name of school district', 'secured_net taxable value',
                    'unsecured_net taxable value']

df5.columns = df5.columns.str.lower()
df6.columns = df6.columns.str.lower()

df5 = df5.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
df5 = df5.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)

df6 = df6.rename(columns= {'school district name': 'name of school district',
                           'secured - net taxable value_school districts property taxes': 'secured_net taxable value',
                            'unsecured - net taxable value_school districts property taxes': 'unsecured_net taxable '
                                                                                             'value'})

df5 = df5.filter(columns_to_keep2)
df6 = df6.filter(columns_to_keep2)

df5['fiscal year'] = df5['fiscal year'].astype(str)
df6['fiscal year'] = df6['fiscal year'].astype(str)


df_merged3 = pd.concat([df5, df6], ignore_index=True)
df_merged3 = df_merged3.drop_duplicates(subset=['fiscal year', 'name of school district'], keep='first')



df_merged3.to_csv('testing_merge_ca_state_cont.csv', index=False)




'''
df5['name of school district'] = df5['name of school district'].str.lower()
df2['lea_name'] = df2['lea_name'].str.lower()

df5 = df5.rename(columns={'fiscal year': 'year'})
df2 = df2.rename(columns={'lea_name': 'name of school district'})

df_merged = pd.merge(df2, df5, on=['name of school district', 'year'], how='inner')



print(len(df5))
print(len(df2))
print(len(df_merged))
print(df_merged)

df_merged.to_csv('final_merged.csv', index=False)
'''


