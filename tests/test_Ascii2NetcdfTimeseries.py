import os
import unittest
import numpy as np

import pyaro
import pyaro.timeseries

EBAS_URL = file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "testdata", "NILU"
)


class TestAscii2NetcdfTimeSeriesReader(unittest.TestCase):
    engine = "ascii2netcdf"

    def test_0engine(self):
        self.assertIn(self.engine, pyaro.list_timeseries_engines())

    def test_1open(self):
        with pyaro.open_timeseries(
            self.engine, EBAS_URL, resolution="daily", filters=[]
        ) as ts:
            self.assertGreater(len(ts.variables()), 70)
            self.assertGreater(len(ts.stations()), 300)

    def test_2read(self):
        with pyaro.open_timeseries(
            self.engine, EBAS_URL, resolution="daily", filters=[]
        ) as ts:
            data = ts.data("sulphur_dioxide_in_air")
            self.assertIn("AM0001", data.stations)
            self.assertGreater(np.sum(data.values), 10000)
            self.assertEqual(data.units, "ug")
