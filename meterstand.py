"""Python app om meterstanden op te volgen via manuele input"""

import pandas as pd
from datetime import date

from pandas.core.frame import DataFrame

HEADER = ['datum','gas','water','electriciteit']
FILE_NAME = 'meterstanden.csv'

def ingave():
    datum = input("Datum ingave:")
    gas = float(input("Gas:"))
    water = float(input("Water:"))
    ele = float(input("Electriciteit:"))
    df = pd.DataFrame(
        {
            "Datum": [datum],
            "Gas": [gas],
            "Water": [water],
            "Electriciteit": [ele]
        }
    )
    df.to_csv(FILE_NAME,mode='a', index=False)
    
ingave()
