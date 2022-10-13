# This script is designed to validate the group code tables in both PAR and PARXL. That is,
# we check for differences in group codes. We will acheive this by first copying and 
# pasting the views from PAR and PARXL respectively into an excel file.
# Then create a helper function that will store PAR's group codes in a hash map for O(1) lookup.
# Finally we create a function that checks whether the group in PARXL are in PAR
# and return the ones that aren't.

import pandas as pd

group_code_df = pd.read_excel(r'C:\Users\l676907\OneDrive - Cargill Inc\Desktop\PAR_XL\validation\group_codes\group_codes.xlsx')

def create_hash(df):
    '''Create hash table of group codes from PAR'''
    dict = {}
    for row in df.iterrows():
        dict[row[1][0]] = True
    return dict

# print(create_hash(group_code_df))

def spot_difference(df):
    '''Check for differences in group codes between PAR and PARXL'''
    diff = []
    par_hash = create_hash(group_code_df)
    for row in df.iterrows():
        if row[1][2] not in par_hash.keys():
            diff.append([row[1][2], row[1][3]])
    return diff

# print(spot_difference(group_code_df))

result = spot_difference(group_code_df)
export_excel = pd.DataFrame(result, columns=['group code', 'group code description'])
file_name = 'group_code_validation.xlsx'
export_excel.to_excel(file_name, index=False)
print('DataFrame is successfully exported as an excel file!')

# Differences are largely due to codes getting deleted from PAR but not PARXL.
# New group codes get appended to PARXL instead of deleting and inserting each time.