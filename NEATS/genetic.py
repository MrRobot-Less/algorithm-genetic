import numpy as np
import random, string
from neural_network import NeuralNetwork

#modelo = "sorvete galera"
        

#AUTOR = Gustavo Andre
#algoritmo genetico 22.05.2020

class Genetic:

    def __init__(self):
        
        self.len_population = 50
        self.len_dad = 1
        self.population = self.Population()
        self.best_population = self.population

    def Individual(self):
        return NeuralNetwork([2,20,1])


    def Population(self):
        return [self.Individual() for i in range(self.len_population)]

    
    def Selection(self):
        
        punctuations = [(i.score, i) for i in self.best_population]
        score = [punctuation[0] for punctuation in sorted(punctuations)]
        if(score.count(0) >= self.len_population):
            self.best_population = self.Population()
            print("OIEE")
            return self.best_population
        else:    
            punctuations = [punctuation[1] for punctuation in sorted(punctuations)]
            
            print(score[-3:])
            
            selected = punctuations[(self.len_population - self.len_dad):]
            dad = selected[0]                        
            for punctuations_list in punctuations[:(self.len_population - self.len_dad)]:
                punctuations_list = dad
                
            population = self.Mutation(punctuations)
            #population = punctuations
            return population

    def Mutation(self,populations, learning_mutation=1):
        for population in populations[:-self.len_dad]:
            if(random.random() <= learning_mutation):
                input, hidden, output = population.matrix
                if(random.random() > 0.5):
                    point = random.randint(0, input - 1)
                    population.synaptic_weights_input[point] = 2 * np.random.random((input, hidden))[0] -1 
                else:
                    
                    point = random.randint(0, output - 1)
                    population.synaptic_weights_output = 2 * np.random.random((hidden, output)) -1
                #print("MUTANTE CARAI")
        return populations
  
    def ResetScore(self):
        for i in self.best_population:
            i.score = 0


    def update(self):
        population = self.Selection()
        self.best_population = population        
        self.ResetScore()
        
        

if __name__ == "__main__":
    
    gen = Genetic()   
    print(gen.best_population)
    