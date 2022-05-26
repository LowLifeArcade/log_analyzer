import numpy as np
import pandas as pd 
import json
from tabulate import tabulate
import openpyxl

# json_data = []
# with open('test_logs.json') as f:
#     json_data = json.load(f)

df = pd.read_json('data/no_apollo_logs.json')
# df = pd.read_json('{"0":{"Product":"Desktop Computer","Price":700}}')
# df = pd.read_json('logs/test_logs.json')

# gives how many different messages are in list
# print(df['Message'].nunique()) 
# lists names of messages
# print(df['Message'].unique())
# lists names and count
# print(df['Message'].value_counts().head(20))
# df = df[['Message', 'Exception', 'LogLevel']]
# print(message['Message'].value_counts())
# print(message.info())
# print(message.describe())
# print(message)
# print(message['Exception'].value_counts())
# df = df[df['Message'] != None]

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


# error = 'Error loading report'
# df = set_df_by_message(error)
# df = get_count_by_exception()
# df = set_df_by_regex('Error')

# params = ['Message', 'Exception', 'LogLevel', 'Host', 'UserId', 'InnerException', 'Flags', 'LogType']
# df = get_merged_counts(error,params, 15)

# df = df1.describe()
# df = pd.merge()
# printMe = df['Exception'].value_counts()
# print(ex['Host'].value_counts())

error = "Global uncaught exception: TypeError:"
params = ['Message', 'Exception', 'LogLevel', 'Host', 'UserId', 'InnerException', 'Flags', 'LogType']

df = get_merged_counts(error, params, 30)

# df = set_df_by_regex('Global uncaught exception: TypeError')
# df = get_count_by_message(20)
# df.to_excel(f'{error}.xlsx')
df.to_excel('err_lists/global_type_errors_list.xlsx')
print(df)