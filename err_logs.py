import numpy as np
import pandas as pd 
import json
import openpyxl
from err_functions import get_merged_counts 

df = pd.read_json('data/no_apollo_logs.json')
df = df.fillna(value="None")

def set_df_by_message(message):
    return df[df['Message'] == message]

def set_df_by_regex(rgx):
    return df[df['Message'].str.contains(rgx, regex = True)]

def get_count_by_exception(amt=10):
    return df['Exception'].value_counts().head(amt)

def get_count_by_message(amt=10):
    return df['Message'].value_counts().head(amt)


def get_merged_counts(series, arr=None, amt=10, axis=1):
    loc_df = df[df['Message'].str.contains(series)]
    df_arr = []
    if arr is not None:
        for param in arr:
            df_arr.append(loc_df[param].value_counts().head(amt))
    return pd.concat(df_arr, axis=axis)

error = ''
params = ['Message', 'Exception', 'LogLevel', 'Host', 'UserId', 'InnerException', 'Flags', 'LogType']

df = get_merged_counts(error,params, 15)

# TODO: loop over error array to produce logs

# TODO: if error starts with Global then name differently 
df.to_excel(f'err_logs/error_log: {error[0:20]}.xlsx')
print(df)