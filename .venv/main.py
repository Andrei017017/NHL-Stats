import os
import glob
import numpy as np
import pandas as pd
import openpyxl
import pyarrow
import duckdb
import timeit

def fill_df():
    path = os.path.join(os.getcwd(), 'players', '*.xlsx')
    xlsx_files = glob.glob(path)

    dfs: list = []
    for file in xlsx_files:
        dfs.append(pd.read_excel(file, sheet_name='QuantHockey', header=1))

    return pd.concat(dfs, ignore_index=True)

def df_to_feather():
    df = fill_df()
    new_df = df.drop(columns=df.iloc[:, 10:]) # only first 10 columns
    new_df.to_feather('NHL.feather')

df = pd.read_feather('NHL.feather')

print(df)

print(os.listdir())
