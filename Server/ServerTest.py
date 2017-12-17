# This is the test file for the server, currently only testing if the dataset array is not null
# Author: Sheldon McGrath
# Last Updated: 17-12-2017
import unittest
from OpenFile import OpenFile


class ServerTest(unittest.TestCase):
    def test(self):
        # print my glorious name
        print("Sheldon McGrath")
        # open given dataset file
        oFile = OpenFile()
        file = oFile.open("00010014-eng.csv", "r+")
        # test for not null array
        self.assertIsNotNone(oFile.StripEST(file))
