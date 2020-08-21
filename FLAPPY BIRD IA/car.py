import pygame, sys, random
import numpy as np
from genetic import Genetic

genetic = Genetic()

WIDTH = 400
HEIGHT = 500
PIPE_GAP = 150
PIPE_HEIGHT = 450
PIPE_WIDTH = 20
geracao = 0

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def get_random_pipe():
    y_random = random.randint(PIPE_GAP,WIDTH-19)
    #y_random = 250
    other_y = abs(y_random-PIPE_GAP) - PIPE_HEIGHT

    return np.array([WIDTH, y_random], dtype=object), np.array([WIDTH,other_y], dtype=object)


class Bird:
    def __init__(self, brain):
        self.pos = np.array([5, HEIGHT/2], dtype=object).astype(float)
        self.vel = np.zeros(2)
        self.acc = np.zeros(2)
        self.width = 15
        self.height = 10
        
        self.brain = brain

    def update(self):
        if(self.pos[1] > 500 or self.pos[1] < 0): return True
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.width, self.height)
        self.acc += np.array([0,0.5])
        self.vel += self.acc
        self.pos += self.vel
        self.acc = np.zeros(2)

    def bump(self):
        self.acc += np.array([0,-7])

    def collider(self, pipe):
        pos = self.pos.astype(int)
        pipe_pos = pipe.pos
        RECT_SELF = pygame.Rect(pos[0], pos[1], self.width, self.height)
        RECT_PIPE = pygame.Rect(pipe_pos[0], pipe_pos[1], pipe.width, pipe.height)
        if(RECT_SELF.colliderect(RECT_PIPE)):
            return True

    def show(self, win):
        pos = self.pos.astype(int)
        pygame.draw.rect(win, (255,255,255), [pos[0], pos[1], self.width, self.height])
        
class Pipe:
    def __init__(self, pos):
        self.pos = pos
        self.vel = np.array([-10, 0])
        self.width = PIPE_WIDTH
        self.height = PIPE_HEIGHT
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.width, self.height)

    def update(self):
        if((self.pos + self.width < 0)[0]): return True
        self.pos += self.vel
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.width, self.height)
    
    def show(self, win):
        pos = self.pos.astype(int)
        pygame.draw.rect(win, (255,255,255), [pos[0], pos[1], self.width, self.height])

delay = False

while True:
    win = pygame.display.set_mode((WIDTH,HEIGHT))
    frame = 0
    birds = []

    pipes = []
    bad = []

    for brain in genetic.best_population:
        bird = Bird(brain)
        birds.append(bird)
    
    a,b = get_random_pipe()
    pipes.append(Pipe(a))
    pipes.append(Pipe(b))
    gen = []
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    delay = not delay
            
        if(delay):
            pygame.time.delay(50)
        if(len(birds) == len(bad)):
            
            break
        for pipe in pipes:
            if(pipe.update()):
                
                a,b = get_random_pipe()
                pipes[0] = Pipe(a)
                pipes[1] = Pipe(b)    
                for b in birds:
                    b.brain.score += 1
                break

            pipe.show(win)
        center = pipes[0].pos - np.array([0, PIPE_GAP/2])
        
        for bird in birds:
                    
            DISTANCE = np.array([center[0]-bird.pos[0],center[1]-bird.pos[1], bird.vel[1]])
            predict = bird.brain.predict(DISTANCE)
            
            if(predict[0] > 0):
                bird.bump()
            if(bird.update()):
                index = birds.index(bird)
                birds.pop(index)
                gen.append(bird)
                
                continue
            bird.show(win)
            for pipe in pipes:
                if(bird.collider(pipe)):
                    index = birds.index(bird)
                    birds.pop(index)
                    gen.append(bird)
                    
                    break
                
                
        pygame.display.update()
        win.fill((0,0,0))
    print("GERACAO: "+ str(geracao))
    for b in gen:
        i = gen.index(b)
        genetic.best_population[i] = b.brain
    genetic.update()
    geracao+=1
