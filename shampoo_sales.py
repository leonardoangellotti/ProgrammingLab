
class FileCSV():

  def __init__(self, name):

    self.name = name

  def get_data(self):

    my_file = open(self.name, 'r')

    lista = []

    for lines in my_file:
      line = lines.split(',')

      lista.append(line)

    my_file.close()

    print(lista)
  
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


file = FileCSV('shampoo_sales.csv')

file.get_data()
file.sum_sales()