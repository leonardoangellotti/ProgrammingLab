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
  def get_data(self, start = None, end = None):

    my_file = open(self.name, 'r')

    lista = []

    for lines in my_file:
      line = lines.split(',')

      lista.append(line)
      
    my_file.close()

    #stampa lunghezza lista voluta
    print(lista[start:end])
  
  #somma tutti i valori sales
  def sum_sales(self):

    my_file = open(self.name, 'r')

    lista_sum = []

    for line in my_file:
      elements = line.split(',')

      #salta la prima riga
      if elements[0] != 'Date':
          
        #prende il primo elemento: data, secondo elemento: sales
        date = elements[0]
        sales = elements[1]

        try:
            lista_sum.append(float(sales))
        except:
            if isinstance(sales, str) or sales == None:
                print('converto il valore {} in 0.0, errore di conversione in float'.format(sales))
                sales = 0.0
                lista_sum.append(float(sales))


    for elements in lista_sum:
      print(elements)

    somma = 0.0

    for elements in lista_sum:
      somma += elements

    print('\nla somma è {}'.format(round(somma,1)))

    my_file.close()

#classe converte tutte le colonen tranne la prima in float
class NumericalCSVFile(FileCSV):

    def convert(self):
        
        my_file = open(self.name, 'r')

        lista = []

        for lines in my_file:
            line = lines.split(',')

            #prende tutte le colonne tranne la prima
            except_the_1_column = line[1:]

            #le aggiunge formato float a lista
            try: 
                for item in except_the_1_column:
                    lista.append(float(item))

            #errore
            except ValueError as err:
                print("\nc'è stato un errore nella conversione")
                print('tipo di errore trovato:\n{}'.format(err))
                print('converto il valore in float 0.0\n')
                
                for item in except_the_1_column:
                    print('{} convertito in: '.format(item))
                    if type(item) != 'int' or 'float':
                        item = 0.0
                    print(item)
                    lista.append(float(item))


            except Exception as err:
                print("\nc'è stato un errore nella conversione")
                print('tipo di errore trovato:\n{}\n'.format(err))


        my_file.close()

        print(lista)



#attribuisco alla classe FileCSV il file shampoo_sales.csv 
file = NumericalCSVFile('shampoo_sales.csv')

#richiamo le funzioni definite
file.get_data(20,30)
file.sum_sales()
file.convert()