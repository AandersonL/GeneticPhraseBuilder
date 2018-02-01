from lib import DNA
from random import randint
from math import floor

def map(n, start1, stop1, start2,stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

class Population(object):
    def __init__(self,tam_pop,mRate, target):
        self.population   = []
        self.matingPol    = []
        self.generations  = 0
        self.finished     = False
        self.target       = target
        self.mutationRate = mRate
        self.perfectScore = 1
        self.bext = ""
        
        for x in range(tam_pop):
            self.population.append(DNA.DNA(len(target)))
        self.calcFitness()

    def calcFitness(self):
        for dna in self.population:
            dna.calcFitness(self.target);
    
    def naturalSelection(self):
        self.matingPol = []
        maxFitness = 0.0
        for dna in self.population:
            if dna.fitness > maxFitness:
                maxFitness = dna.fitness
        for dna in self.population:
            fitness = map(dna.fitness, 0, maxFitness, 0, 1)
            n = floor(fitness*100)
            for m in range(n):
                self.matingPol.append(dna)  

    def generate(self):
        for i,dna in enumerate(self.population):
            a = floor(randint(0,len(self.matingPol) - 1))
            b = floor(randint(0,len(self.matingPol) - 1))
            partnerA = self.matingPol[a]
            partnerB = self.matingPol[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child
        self.generations += 1

    def getBest(self):
        return self.best
    
    def evaluate(self):
        worldRecord = 0.0
        index = 0
        for i,dna in enumerate(self.population):
            if dna.fitness > worldRecord:
                index = i
                worldRecord = dna.fitness

        self.best = self.population[index].getPhrase()
        if worldRecord == self.perfectScore:
            self.finished = True
    
    def isFinished(self):
        return self.finished

if __name__ == '__main__':
    print('wrong place fella')
