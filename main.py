import pandas as pd

pd.options.display.max_columns = None

df1 = pd.read_csv("/Users/matthewuytioco/Downloads/school-districts_lea_directory.csv")
df2 = pd.read_csv("/Users/matthewuytioco/Downloads/districts_ccd_finance.csv")

df1 = df1[df1['year'] >= 2008]
df1 = df1[df1['state_mailing'].str.contains('CA', na=False, case=False)]

merged_data = []

for i, row1 in df1.iterrows():
    leaid = row1['leaid']
    year = row1['year']

    for j, row2 in df2.iterrows():
        if row2['leaid'] == leaid and row2['year'] == year:
            merged_row = {'leaid': leaid, 'year': year, 'lea_name': row1['lea_name'], 'phone': row1['phone'],
                          'urban_centric_locale': row1['urban_centric_locale'], 'number_of_schools':
                              row1['number_of_schools'], 'enrollment': row1['enrollment'],'teachers_total_fte':
                              row1['teachers_total_fte'], 'rev_total': row2['rev_total'],
                          'rev_fed_total': row2['rev_fed_total'], 'rev_state_total': row2['rev_state_total'],
                          'rev_local_total': row2['rev_local_total'], 'exp_total': row2['exp_total'],
                          'exp_current_instruction_total': row2['exp_current_instruction_total'],
                          'outlay_capital_total': row2['outlay_capital_total'],
                          'payments_charter_schools': row2['payments_charter_schools'],
                          'salaries_instruction': row2['salaries_instruction'],
                          'benefits_employee_total': row2['benefits_employee_total'],
                          'debt_interest': row2['debt_interest'],
                          'debt_longterm_outstand_end_FY': row2['debt_longterm_outstand_end_FY'],
                          'debt_shortterm_outstand_end_FY': row2['debt_shortterm_outstand_end_FY'],
                          }
            merged_data.append(merged_row)
            break

merged_df = pd.DataFrame(merged_data)
print(merged_df)
print("Selected Columns:", merged_df.columns.tolist())

