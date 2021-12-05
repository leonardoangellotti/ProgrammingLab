
#classe CVS file
class FileCSV():

  #inizializzo
  def __init__(self, name):

    self.name = name

    try:
        my_file = open(self.name, 'r')
    except Exception as err:
        print('il file non è leggibile')
        print('tipo di errore: \n{}'.format(err))

  #prende data e sales e li mette in una lista
  def get_data(self):

    my_file = open(self.name, 'r')

    lista = []

    for lines in my_file:
      line = lines.split(',')

      lista.append(line)

    my_file.close()

    print(lista)
  
  #somma tutti i valori sales
  def sum_sales(self):

    my_file = open(self.name, 'r')

    lista_sum = []

    for line in my_file:
      elements = line.split(',')

      if elements[0] != 'Date':
        date = elements[0]
        sales = elements[1]

        lista_sum.append(float(sales))

    for elements in lista_sum:
      print(elements)

    somma = 0.0

    for elements in lista_sum:
      somma += elements

    print('\nla somma è {}'.format(round(somma,1)))

    my_file.close()

class NumericalCSVFile(FileCSV):

    def convert(self):
        
        my_file = open(self.name, 'r')

        lista = []

        for lines in my_file:
            line = lines.split(',')

            except_the_1_column = line[1:]

            try: 
                for item in except_the_1_column:
                    lista.append(float(item))


            except ValueError as err:
                print("\nc'è stato un errore nella conversione")
                print('tipo di errore trovato:\n{}'.format(err))
                print('converto il valore in float 0.0\n')
                for item in except_the_1_column:
                    print('{} convertito in: '.format(item))
                    if type(item) != 'int' or 'float':
                        item = 0.0
                    print(item)

            except Exception as err:
                print("\nc'è stato un errore nella conversione")
                print('tipo di errore trovato:\n{}\n'.format(err))


        my_file.close()

        print(lista)



#attribuisco alla classe FileCSV il file shampoo_sales.csv 
file = NumericalCSVFile('shampoo_sales.csv')

#richiamo le funzioni definite
file.get_data()
file.sum_sales()
file.convert()