from lib import Population
import sys

def main():
    tam_pop = 300
    mRate = 0.01
    if ( len(sys.argv) < 2 ):
        target = "To be or not be that is the question"
    else:
        target = sys.argv[1]
    p = Population.Population(tam_pop, mRate, target)
    cicle = 0

    while not p.isFinished():
        p.naturalSelection()
        p.generate()
        p.calcFitness()
        p.evaluate()
        print("Geracao -> {0} {1}".format(p.generations,p.getBest()))
if __name__ == '__main__':
    main()
