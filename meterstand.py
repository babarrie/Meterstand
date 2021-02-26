"""Python app om meterstanden op te volgen via manuele input"""

import pandas as pd
from datetime import date


HEADER = ['Datum','Gas','Water','Electriciteit']
FILE_NAME = 'meterstanden.csv'

def main():

    ingave()
    return "Done"

def ingave():
    df = pd.DataFrame(
        {
            "Datum": [],
            "Gas": [],
            "Water": [],
            "Electriciteit": []
        }
    )
    n = 0
    datum = date.today()
    while n != 5:
        datum = input("Datum ingave:")
        gas = float(input("Gas:"))
        water = float(input("Water:"))
        ele = float(input("Electriciteit:"))
        df = df.append({"Datum": [datum], "Gas": [gas], "Water": [water], "Electriciteit": [ele]},ignore_index=True)
        n = n + 1
        print(n)
    df.to_csv(FILE_NAME,mode='a', index=False)

    

if __name__ == "__main__":
    main()
