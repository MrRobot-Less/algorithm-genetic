from genetic import Genetic
import numpy as np
from dataset import training_inputs,training_outputs


genetic = Genetic()

training_inputs = np.array([[0,0], [1,0], [0,1], [1,1]])
training_outputs = np.array([[0,1,1,0]]).T

print("INPUT")
print(training_inputs)
print("OUTPUT")
print(training_outputs)
print("\n")

# Train the neural network

def generation():
    for neural_network in genetic.best_population:
        index = 0
        for x in training_inputs:
            t = neural_network.predict(x)
            #print("esperado: "+ str(training_outputs[index]))
            #print("predict: "+str(t))
            if(int(t > 0.5) == training_outputs[index]):
                neural_network.score += 1
            #print("\n")
            index+=1
        
        #print("acertou: "+str(neural_network.score))
        if(neural_network.score >= training_outputs.size): 
            
            genetic.update()        
            return False
    genetic.update()
    genetic.ResetScore()
    return True


run = True
gen = 0
while run:
    run = generation()
    print("GERACAO: "+str(gen))
    gen+= 1    


