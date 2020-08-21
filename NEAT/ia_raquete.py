import pygame
import random, sys, os
from neural_network import NeuralNetwork
from genetic import Genetic

import numpy as np


genetic = Genetic()
geracao = 0

clock = pygame.time.Clock()
d = 50
delay = False
while True:

    x = 50
    y = 300
    errou = 0
    c = 0
    altura = 15
    largura = 50
    vel = 15
    run = True

    new_boll = True

    xs = []
    ys = []
    cor = []

    x_bola = int(random.randint(240,240))
    y_bola = 0
    for i in range(genetic.len_population):
        xs.append(x)
        ys.append(y)
        cor.append((random.randint(100,255),random.randint(100,255),random.randint(100,255)))

    def bola(x,y):
        pygame.draw.rect(win, (255,0,0), (x, y, 10, 10))

    win = pygame.display.set_mode((480, 350))
    valor =0    
    changeIndividual = []

    def update():
        global y_bola, x_bola, x_personagem, vida_valor, x, y, errou,c, delay
        valor = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.mod == pygame.K_UP:
                    delay = not delay
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            delay = not delay

        if(delay):
            pygame.time.delay(30)
        index = 0
        for nn in genetic.best_population:
            
            personagem = pygame.Rect(xs[index],ys[index],largura, altura)
            bola_ = pygame.Rect(x_bola, y_bola, 10,10)
            x_obj = np.array([x_bola, float(xs[index]+largura/2)]).astype(float)
            y_obj = np.array([y_bola]).astype(float)

            obj = np.hstack([x_obj,y_obj])
            valor = float(nn.predict(obj))
            valor = int(valor > 0.5)
            if(y_bola >= 350):
                errou += 1
                
                x_bola = 240
                y_bola = 0
                
            if valor == 0:
                xs[index] -= vel
            if valor == 1:
                xs[index] += vel

            if(xs[index] > 480 or xs[index] + largura < 0):
                pass
            
            
            if(personagem.colliderect(bola_)):
                
                nn.score += 1
                
                x_bola = 240
                y_bola = 0
                
            if(errou > 2 or len(genetic.best_population) < 1):
                c += 1
            index+= 1

        y_bola += 10

        for xx in xs:
            index = xs.index(xx)
            pygame.draw.rect(win, cor[index], (xx, ys[index] - 10, largura, altura))
            bola(x_bola,y_bola)
        pygame.display.flip()
        win.fill((0,0,0))
        

    while run:
        update()
        
        if(c >= 1):
            geracao += 1
            
            c = 0
            os.system("cls")
            print("GERACAO: "+str(geracao))
            print("ultimo valor: "+ str(valor))
            genetic.update()
            break
    
pygame.quit()
