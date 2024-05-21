import pandas as pd

def head_returner():
    df = pd.read_csv('Financial Allocations.csv')
    return str(df.head())