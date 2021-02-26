"""Python app om meterstanden op te volgen via manuele input"""

import csv

def gasmeter():
    gas = 0.0
    gas = float(input())

def watermeter():
    water = 0.0
    water = float(input())

def elemeter():
    ele = 0.0
    ele = float(input())

def add_row(gas, water, ele):
    rij = [gas, water, ele]
    csv.writer(rij)
