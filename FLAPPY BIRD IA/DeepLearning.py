import numpy as np

#REDE NEURAL ARTIFICIAL PROFUNDA 02/06/2020 03:43

#AUTOR = GUSTAVO ANDRE CORREIA DA SILVA

#EBAAA  
def tanh_derivative(x):
    return (1-np.square(x))

def tanh(x):
    return np.tanh(x)

class DeepNeuralNetwork():
    
    def __init__(self, matrix):
        
        self.synaptic_weights = []
        self.len_synaptic = 1
        self.score = 0
        for i in range(len(matrix)-1):
            weight = 2 * np.random.random((matrix[i], matrix[i+1])) -1 
            self.synaptic_weights.append(weight)
            self.len_synaptic += matrix[i]
        self.len_synaptic += matrix[i+1]
        
        self.matrix = matrix

    def train(self, training_inputs, training_outputs, training_iterations, learnig_rate=0.1):
        for iteration in range(training_iterations):
            outputs = []
            input = training_inputs
            outputs.append(input)
            for w in self.synaptic_weights:
                input = self.think(input, w)
                outputs.append(input)
            

            derivative = tanh_derivative(outputs[-1])
            error = training_outputs - outputs[-1]
            const_error = error * derivative
            gradient = []

            delta = const_error
            gradient.append(delta)

            for i in range(1,len(self.synaptic_weights)):
                if i ==1:
                    delta = np.dot(self.synaptic_weights[-i], delta.T)*(tanh_derivative(outputs[-i-1]).T)
                else:
                    delta = np.dot(self.synaptic_weights[-i], delta)*(tanh_derivative(outputs[-i-1]).T)
                gradient.append(delta)

            for i in range(2, len(outputs)+1):
                if(i == 2):
                    adjustment = np.dot(outputs[-i].T, const_error)
                else:
                    adjustment = np.dot(outputs[-i].T, gradient[i-2].T)
                self.synaptic_weights[-i+1] += adjustment* learnig_rate    

            n = iteration +1
            if n % 1000== 0: print("epochs: "+str(n))

    def think(self, inputs, weight):
        
        inputs = inputs.astype(float)
        output = tanh(np.dot(inputs, weight))
        return output

    def predict(self, training_inputs):
        input = training_inputs    
        for w in self.synaptic_weights:
            input = self.think(input, w)
        return input   



if __name__ == "__main__":
    layer  = [2]
    for i in range(8):
        layer.append(10)
    layer.append(1)

    print(layer)
    neural_network = DeepNeuralNetwork(layer)
    training_inputs = np.array([[0,0], [1,0], [0,1], [1,1]])
    training_outputs = np.array([[0,1,1,0]]).T
    
    print("INPUT")
    print(training_inputs)
    print("OUTPUT")
    print(training_outputs)
    print("\n")

    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 25000)
    index = 0
    c =0
    for x in training_inputs:
    
        t = neural_network.predict(x)
        print("esperado: "+ str(training_outputs[index]))
        print("predict: "+str(t))
        if(int(t > 0.5) == training_outputs[index]):
            c+=1
        print("\n")
        index+=1
    print("acertou: "+str(c))