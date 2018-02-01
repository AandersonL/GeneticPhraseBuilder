import string
from random import randint, random
from math import floor

class DNA(object):
    def __init__(self, length):
        self.genes = []
        self.fitness = 0
        for gene in range(length):
            try:
                strrand = string.ascii_letters[randint(0, len(string.ascii_letters))]
            except:
                strrand = " "
            self.genes.append(strrand)
        
    def getPhrase(self):
        return "".join(self.genes)

    def calcFitness(self, target):
        score = 0.0
        for i,x in enumerate(self.genes):
            if x == target[i]:
                score += 1.0
        self.fitness = score/len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = floor(randint(0, len(self.genes)-1))
        for i,gene in enumerate(self.genes):
            if ( i > midpoint ): child.genes[i] = self.genes[i]
            else: child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutationRate):
        for i,gene in enumerate(self.genes):
            if random() < mutationRate:
                try:
                    strrand = string.ascii_letters[randint(0, len(string.ascii_letters))]
                except:
                    strrand = " "
                self.genes[i] = strrand



