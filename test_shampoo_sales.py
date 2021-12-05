import unittest
from shampoo_sales import FileCSV

class TestCSVFIle(unittest.TestCase):

    def test_init(self):

        csv_file = FileCSV('shampoo_sales.csv')

        self.assertEqual(csv_file.self,'shampoo_sales.csv')