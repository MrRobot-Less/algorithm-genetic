import numpy as np


#PERCEPTRON MULTI CAMADAS 18/05/2020

#AUTOR = GUSTAVO ANDRE CORREIA DA SILVA

#FODAAAAAAAA


class NeuralNetwork():
    
    def __init__(self, matrix):
        
        input, hidden, output = matrix
        self.synaptic_weights_input = 2 * np.random.random((input, hidden)) -1 
        self.synaptic_weights_layer = 2 * np.random.random((hidden, hidden)) -1 
        self.synaptic_weights_output = 2 * np.random.random((hidden, output)) - 1
        self.score = 0
        self.matrix = matrix

    def tanh_derivative(self, x):
        return (1-np.square(x))


    def tanh(self, x):
        return np.tanh(x)

    def sigmoid(self, x):
    
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations, learnig_rate=0.1):
        for iteration in range(training_iterations):
            
            output_input = self.think(training_inputs, self.synaptic_weights_input)
            output_layer = self.think(output_input, self.synaptic_weights_layer)
            output_hidden = self.think(output_layer, self.synaptic_weights_output)

            derivative = self.tanh_derivative(output_hidden)

            error = training_outputs - output_hidden
            const_error = error * derivative

            del4 = const_error

			# find 'errors' in each layer
            del3 = np.dot(self.synaptic_weights_output, del4.T)*(self.tanh_derivative(output_layer).T)
            del2 = np.dot(self.synaptic_weights_layer, del3)*(self.tanh_derivative(output_input).T)

            # get adjustments (gradients) for each layer
            adjustment3 = np.dot(output_layer.T, del4)
            adjustment2 = np.dot(output_input.T, del3.T)
            adjustment1 = np.dot(training_inputs.T, del2.T)

            # adjust weights accordingly
            self.synaptic_weights_input += adjustment1 * learnig_rate
            self.synaptic_weights_layer += adjustment2 * learnig_rate
            self.synaptic_weights_output += adjustment3 * learnig_rate

            n = iteration +1
            if n % 1000== 0: print("epochs: "+str(n))

    def think(self, inputs, weight):
        
        inputs = inputs.astype(float)
        output = self.tanh(np.dot(inputs, weight))
        condition = output < 0
        #print(output < 0)
        index = 0

        for row in range(condition[0].size -1):
            if(type(condition[row]) != bool):
                for col in range(condition[row].size):
                    #print(condition[row][col])
                    if(condition[row][col]):
                        output[row][col] = 0
            else:
                #print(condition[row][col])
                if(condition[row][col]):
                    output[row] = 0
            
        return output

    def predict(self, training_inputs):
        output_input = self.think(training_inputs, self.synaptic_weights_input)
        output_layer = self.think(output_input, self.synaptic_weights_layer)
        output_hidden = self.think(output_layer, self.synaptic_weights_output)
        return output_hidden



if __name__ == "__main__":
        
    neural_network = NeuralNetwork([2,5,1])
    training_inputs = np.array([[0,0], [1,0], [0,1], [1,1]])
    training_outputs = np.array([[0,1,1,0]]).T
    
    print("INPUT")
    print(training_inputs)
    print("OUTPUT")
    print(training_outputs)
    print("\n")

    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 2000)
    index = 0
    c =0
    for x in training_inputs[:10]:
    
        t = neural_network.predict(x)
        print("esperado: "+ str(training_outputs[index]))
        print("predict: "+str(t))
        if(int(t > 0.5) == training_outputs[index]):
            c+=1
        print("\n")
        index+=1
    print("acertou: "+str(c))