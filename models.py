class Model():

    def fit(self, data):

        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
        
    def predict(self, data):

        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data): 

            somma_incrementi = 0.0

            incremento = 0.0

            i = 0


            for item in data:

                if i + 1 >= len(data):
                    pass
                
                else:
                    incremento = data[i+1]-data[i]

                    somma_incrementi += incremento

                i = i +1


            incremento_tot = somma_incrementi/(len(data)-1)

            prediction = incremento_tot + data[-1]

            return prediction
        

data = [50,52,60]

predizione = IncrementModel().predict(data)

print(predizione)