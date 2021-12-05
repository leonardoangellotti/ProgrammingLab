my_file = open('shampoo_sales.csv', 'r')

lista = []

for line in my_file:
  elements = line.split(',')

  if elements[0] != 'Date':
    date = elements[0]
    sales = elements[1]

    lista.append(float(sales))

for elements in lista:
  print(elements)

somma = 0.0

for elements in lista:
  somma += elements

print('\nla somma è {}'.format(round(somma,2)))

my_file.close()