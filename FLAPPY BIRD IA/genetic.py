import numpy as np
import random, string
from DeepLearning import DeepNeuralNetwork

#modelo = "sorvete galera"
        

#AUTOR = Gustavo Andre
#algoritmo genetico 22.05.2020

class Genetic:

    def __init__(self):
        
        self.len_population = 20
        self.len_dad = 2
        self.population = self.Population()
        self.best_population = self.population

    def Individual(self):
        return DeepNeuralNetwork([3,3,3,1])


    def Population(self):
        return [self.Individual() for i in range(self.len_population)]

    
    def Selection(self):
        
        punctuations = [(i.score, i) for i in self.best_population]
        score = [punctuation[0] for punctuation in sorted(punctuations)]
        print(score[-3:])
        
        punctuations = [punctuation[1] for punctuation in sorted(punctuations)]
                
        selected = punctuations[(self.len_population - self.len_dad):]
        for punctuations_list in punctuations:   
            dad = random.sample(selected, 1)
            weight = dad[0].synaptic_weights
            punctuations_list.synaptic_weights = weight
        
        population = self.Mutation(punctuations)
        return population

    def Mutation(self,populations, learning_mutation=15):
        for population in populations[:-self.len_dad]:
            for j in range(population.len_synaptic):
                if(random.random() < learning_mutation):
                    weight = random.randint(0, len(population.synaptic_weights)-1)
                    index = random.randint(0, population.synaptic_weights[weight].T[0].size - 1)
                    i = population.synaptic_weights[weight][index].T.size-1
                    point = random.randint(0, i)
                    population.synaptic_weights[weight][index][point] = 2*np.random.random()-1
                    
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
    