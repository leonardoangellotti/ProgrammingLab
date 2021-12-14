
#modello previsione
class Model():

    def fit(self, data):

        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):

        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

#metodo fit e previsione
class IncrementModel(Model):

    #fit dei dati
    def fit(self, data):

        #inizializza variabili
        somma_incrementi = 0.0
        incremento = 0.0
        i = 0

        #calcola incremento medio
        for item in data:

            if i + 1 >= len(data):
                pass
            
            else:
                incremento = data[i+1]-data[i]

                somma_incrementi += incremento

            i = i + 1

        self.incremento_medio = somma_incrementi/(len(data)-1)
    
    #predict dei dati
    def predict(self, data): 

        #prevede il valore successivo
        prediction = self.incremento_medio + data[-1]

        #lo aggiunge alla lista
        data.append(prediction)  

        #ritorna il valore successivo previsto
        return prediction      

    def err_medio(self, data):

        #prendi un indice
        i = int(input('\ndove vuoi spezzare la lista?'))

        #lista_evaluation : dopo i sono evaluation dataset
        lista_evaluation = data[i:]

        #lista_fit : prima di i sono fit dataset
        lista_fit = data[:i]

        #lista_prev : fai la previsione su lista_fit il numero di volte pari alla lunghezza di lista_evaluation 
        volte = len(lista_evaluation)

        lista_prev = []

        previsone = 0

        for k in range(volte):

            previsione = int(self.predict(lista_fit))

            lista_prev.append(previsone)

            self.fit(lista_prev)
            
        #lista_err :fai valore assoluto della differenza tra l'elemento k di lista_evaluation e l'elemento k di lista_prev
        lista_err = []

        for k in range(volte):

            err = abs(lista_evaluation[k] - lista_prev[k])

            lista_err.append(err)

        #fai la media degli elementi lista_err, uguale al errore medio.
        errore_medio = sum(lista_err)/len(lista_err)

        print("\nl'errore medio partendo dalla posizione {} è {}".format(i, errore_medio))

        return errore_medio








##################################################
#programma

data = [8,19,5,98,7,5,60]

incremento = IncrementModel()

#volte = int(input('\nquanti valori vuoi predire? '))
#for i in range(volte): 

incremento.fit(data)
previsione = incremento.predict(data)

incremento.err_medio(data)

