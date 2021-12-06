import unittest
from shampoo_sales import FileCSV
from shampoo_sales import NumericalCSVFile

class TestCSVFIle(unittest.TestCase):

    #guarda se il nome del file è shampoo_sales.csv
    def test_init(self):

        csv_file = FileCSV('shampoo_sales.csv')

        self.assertEqual(csv_file.name,'shampoo_sales.csv')

    #guarda se la somma è maggiore di 0
    def test_get_data(self):

        csv_file = FileCSV('shampoo_sales.csv')

        csv_file.sum_sales() > 0

    #guarda se la conversione è di tipo float
    def test_convert(self):

        csv_file = NumericalCSVFile('shampoo_sales.csv')

        self.assertEqual(csv_file.convert(), float)

        

