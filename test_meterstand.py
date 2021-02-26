"""Meterstand unittest"""
import unittest
from Meterstand import meterstand

class testMeterstand(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def testIngave(self):
        meterstand.ingave()
