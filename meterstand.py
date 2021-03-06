"""Python app om meterstanden op te volgen via manuele input"""

import pandas as pd
from flask import *
from datetime import date
import matplotlib.pyplot as plt

app = Flask(__name__)

HEADER = ['Datum','Gas','Water','Electriciteit']
FILE_NAME = '~/Projects/Meterstand/meterstanden.csv'

@app.route("/")
def show_readings():
    data = pd.read_csv(FILE_NAME,";")
    return render_template('index.html', tables=[data.to_html(header=True, index=False, table_id="table")], titles=[data.columns.values])

@app.route("/charts/<gwe>")
def show_graph(gwe):
    fig, axs = plt,plt.subplots()
    data = pd.read_csv(FILE_NAME,";", index_col=0, parse_dates=True)
    data.plot.area()
    axs.set_ylabel(gwe)
    plt.title(gwe)
    fig.savefig('~/Projects/Meterstand/static/img/graph.png')
    return render_template('charts.html',url='~/Projects/Meterstand/static/img/graph.png' ) #vind bestand niet


if __name__ == "__main__":
    app.run(debug=True)

#def ingave():
#    df = pd.DataFrame(
#        {
#            "Datum": [],
#            "Gas": [],
#            "Water": [],
#            "Electriciteit": []
#        }
#    )
#    n = 0
#    datum = date.today()
#    while n != 5:
#        datastring = input("Geef meterstand in datum,gas,water,elec:")
#        df = df.append({"Datum": [datum], "Gas": [gas], "Water": [water], "Electriciteit": [ele]},ignore_index=True)
#        print(n)
#   df.to_csv(FILE_NAME,mode='a', index=False)
