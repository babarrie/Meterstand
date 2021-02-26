"""Meterstand unittest"""
import unittest
import Meterstand

class testMeterstand(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def add_gas(self):
        meter = Meterstand()
        meter.gasmeter(100.0)