import csv
#import flask
#app = flask(__name__)
#@app.route('/meterstand')
#def webpage():
#    return 'Hello world'


class meterstand():
    def gasmeter(float):
        gas = 0.0
        gas = float(input())
        pass
    def watermeter(float):
        water = 0.0
        water = float(input())
        pass
    def elemeter(float):
        ele = 0.0
        ele = float(input())
        pass
    def add_row(gas, water, ele):
        rij = [gas, water, ele]
        csv.writer(rij)


