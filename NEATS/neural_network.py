import numpy as np

#AUTOR = GUSTAVO ANDRE
#05/05/2020

#REDE NEURAL ARTIFICIAL - PERCEPTRON MULTI CAMADAS

class NeuralNetwork():
    
    def __init__(self, matrix):
        self.matrix = matrix
        input, hidden, output = self.matrix
        self.score = 0
        self.synaptic_weights_input = 2* np.random.random((input,hidden)) -1
        self.synaptic_weights_output =2* np.random.random((hidden,output)) -1

        self.synaptic_weights_bias_hidden = 2* np.random.random((1,hidden)) -1
        self.synaptic_weights_bias_output = 2* np.random.random((1,output)) -1

    def tanh(self, x):
        return np.tanh(x)
        


    def sigmoid(self, x):
    
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def think(self, inputs, weight):
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, weight))
        return output

    def predict(self, training_inputs):
        output_input = self.think(training_inputs, self.synaptic_weights_input)+self.synaptic_weights_bias_hidden
        
        output_hidden = self.think(output_input, self.synaptic_weights_output)+self.synaptic_weights_bias_output
        
        return output_hidden

        


if __name__ == "__main__":
   
    neural_network = NeuralNetwork([2,5,1])
    training_inputs = np.array([[0,0],[1,0],[0,1],[1,1]])
    training_outputs = np.array([[0,1,1,0]]).T
    
    print("INPUT")
    print(training_inputs)
    print("OUTPUT")
    print(training_outputs)
    print("\n")

    # Train the neural network
    index = 0
    c=0
    for x in training_inputs:
    
        t = neural_network.predict(x)
        
        print("ESPERADO: "+ str(training_outputs[index]) + " -> SAIDA: "+str(t))

        index+=1
    
    print("acertou: "+str(c))