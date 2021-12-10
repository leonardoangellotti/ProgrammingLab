#per disegnare il grafico
from matplotlib import pyplot

class Model():

    def fit(self, data):

        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):

        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def fit(self, data):

        somma_incrementi = 0.0

        incremento = 0.0

        i = 0

        for item in data:

            if i + 1 >= len(data):
                pass
            
            else:
                incremento = data[i+1]-data[i]

                somma_incrementi += incremento

            i = i + 1

        self.incremento_medio = somma_incrementi/(len(data)-1)
    
    def predict(self, data): 

        prediction = self.incremento_medio + data[-1]

        data.append(prediction)  

        return prediction      



#programma

data = [8,19,5,98,7,5,60]

incremento = IncrementModel()

#volte = int(input('\nquanti valori vuoi predire? '))

#for i in range(volte): 
incremento.fit(data)
previsione = incremento.predict(data)
incremento.fit(data)
previsione = incremento.predict(data)
incremento.fit(data)
previsione = incremento.predict(data)

pyplot.plot(data + [previsione], color='tab:red')
pyplot.plot(data, color='tab:blue')
pyplot.show()