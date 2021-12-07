from Model import IncrementModel

#classe CVS file
class FileCSV():

  #inizializzo
  def __init__(self, name):

    self.name = name

    #cerca se c'è un file da aprire
    try:
        my_file = open(self.name, 'r')
    #se non c'è restituisce l'errore
    except Exception as err:
        print('il file non è leggibile')
        print('tipo di errore: \n{}'.format(err))

  #prende data e sales e li mette in una lista
  def get_data(self, start = None, end = None):

    #apre il file 
    my_file = open(self.name, 'r')

    lista = []

    #divide gli elementi nel file e li aggiune ad una lista
    for lines in my_file:
        line = lines.split(',')

        lista.append(line)
        
    #chiude il file
    my_file.close()

    #stampa lunghezza lista voluta
    print(lista[start:end])
  
  #somma tutti i valori sales
  def sum_sales(self):

    my_file = open(self.name, 'r')

    lista_sum = []

    #legge le linee del file
    for line in my_file:
      elements = line.split(',')

      #salta la prima riga
      if elements[0] != 'Date':
          
        #prende il primo elemento: data, secondo elemento: sales
        date = elements[0]
        sales = elements[1]

        #aggiunge alla lista i valori sales convertii in float
        try:
            lista_sum.append(float(sales))
        #se non li può convertire li setta 0.0
        except:
            if isinstance(sales, str) or sales == None:
                print('converto il valore {} in 0.0, errore di conversione in float'.format(sales))
                sales = 0.0
                lista_sum.append(float(sales))

    #stampa tutti gli elementi nella lista
    for elements in lista_sum:
      print(elements)

    #variabile somma inizializzata a 0.0
    somma = 0.0

    #conferisce a var. somma la somma di tutti gli elementi della lista
    for elements in lista_sum:
      somma += elements

    #stampa la somma
    print('\nla somma è {}'.format(round(somma,1)))

    return somma

    #chiude il file in modalità lettura
    my_file.close()

#classe converte tutte le colonen tranne la prima in float
class NumericalCSVFile(FileCSV):

    def convert(self):
        
        #apre il file in lettura
        my_file = open(self.name, 'r')

        lista = []

        #legge ogni riga del file e ne fa lo split
        for lines in my_file:
            line = lines.split(',')

            #prende tutte le colonne tranne la prima
            except_the_1_column = line[1:]

            #le aggiunge formato float a lista
            try: 
                for item in except_the_1_column:
                    lista.append(float(item))

            #se è un errore di tipo value
            except ValueError as err:
                print("\nc'è stato un errore nella conversione")
                print('tipo di errore trovato:\n{}'.format(err))
                print('converto il valore in float 0.0\n')
                
                #per ogni elemento nelle successive colonne...
                for item in except_the_1_column:
                    print('{} convertito in: '.format(item))
                    #...se non è un intero o float lo setta a 0.0
                    if type(item) != 'int' or 'float':
                        item = 0.0
                    print(item)
                    #aggiunge in una lista
                    lista.append(float(item))

            #se è un'altro tipo di errore
            except Exception as err:
                print("\nc'è stato un errore nella conversione")
                print('tipo di errore trovato:\n{}\n'.format(err))

        #chiude il file in lettura
        my_file.close()

        #stampa la lista
        print(lista)

        return lista



#attribuisco alla classe FileCSV il file shampoo_sales.csv 
file = NumericalCSVFile('shampoo_sales.csv')

#richiamo le funzioni definite
file.get_data(20,30)
file.sum_sales()
file.convert()