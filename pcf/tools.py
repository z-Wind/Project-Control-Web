'''
tools.py
'''
import pandas as pd


# sql to pandas
def sqltoDF(query):
    return pd.read_sql(query.statement, query.session.bind)
