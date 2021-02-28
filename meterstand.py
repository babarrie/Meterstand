"""Python app om meterstanden op te volgen via manuele input"""

import pandas as pd
from flask import *
from datetime import date

app = Flask(__name__)

HEADER = ['Datum','Gas','Water','Electriciteit']
FILE_NAME = 'meterstanden.csv'

@app.route("/")
def show_readings():
    data = pd.read_csv('meterstanden.csv',";")
    data.set_index(HEADER, inplace=True)
    data.index.name=None
    return render_template('meterstand.html', table=[data.to_html(index=True)])

if __name__ == "__main__":
    app.run(debug=True)

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
        datastring = input("Geef meterstand in datum,gas,water,elec:")
        df = df.append({"Datum": [datum], "Gas": [gas], "Water": [water], "Electriciteit": [ele]},ignore_index=True)
        print(n)
    df.to_csv(FILE_NAME,mode='a', index=False)
