# Name:- Abhishikth Boda
# Roll Number:- S20210010044
# Subject:- Artificial Intelligence
# Section:- 1
# Assignment:- 1
# Date:- 15-03-2023

# this will import random function
from numpy import insert
import random

# this is not regarding the algorithm
# it will print the details of the assignment holder
print('\n****************************\n')
print('Name:- Abhishikth Boda')
print('Roll Number:- S20210010044')
print('Subject:- Artificial Intelligence')
print('Section:- 1')
print('Assignment:- 1')
print('Date:- 15-03-2023')
print('\n****************************\n')

# this will import insert function from numpy library

# now we will create variables and and take input from the user
p = int(input("Enter the Population size (P) :- "))
# the type of inputs accepted are clearly mentioned below in the print statements
c = int(input(
    "Enter the Crossover type (C) [0 for one point crossover and 1 for two point crossover]:- "))
m = int(
    input("Enter the Mutation type (M) [0 for bit flip and 1 for swap mutation]:- "))
t = int(input(
    "Enter the Iteration condition (T) [0 for no improvement for x iteration and 1 for predefined iterations]:- "))

# for different type of iteration condition we take different inputs
if (t == 0):
    x = int(input('Enter x [No improvement until this iteration] : '))
elif (t == 1):
    it = int(input('Enter i [number of iterations] : '))

# now we will create arrays and store inputs in those arrays
# first we will create population array
population = []
# now we will create array for population converted to binary
population_binary = []
# now we will create array for population fitness
population_fitness = []
# now we will create array for new population
population_new = []

# this is a function for converting decimal to binary


def DecimalToBinaryConverter(n):
    if (n == 0):
        return '00000'
    else:
        b = ""
        while (n > 0):
            a = int(n % 2)
            n = int(n/2)
            b = str(a) + b
        while (len(b) != 5):
            b = '0' + b
        return b

# this is a function for converting binary to decimal


def BinaryToDecimalConverter(b):
    num = 0
    for i in range(len(b)):
        num = num + int(b[i])*pow(2, 4-i)
    return num

# this will create random population


def RandomPopulationGenerator():
    for i in range(p):
        pop_var = random.randint(0, 31)
        population.append(pop_var)

# this will change the population from decimal to binary


def DecimalPopToBinaryPop(population):
    for i in range(p):
        population_binary.append(DecimalToBinaryConverter(population[i]))

# this will change the population from binary to decimal


def BinaryPopToDecimalPop():
    for i in range(p):
        population.append(BinaryToDecimalConverter(population_binary[i]))

# this will calculate the total fitness of a population


def FindTotalFitness():
    TotalFitness = 0
    for i in range(p):
        TotalFitness += population_fitness[i]
    return TotalFitness

# this will calculate fitness for a particular population input


def CalculateFitness(population):
    for i in range(p):
        population_fitness.append(population[i]**2)

# this will do two point crossover for offsprings


def TwoPointCrossover(seq1, seq2, crossover_point1, crossover_point2):
    crossover_popln = ''
    for i in range(0, crossover_point1-1):
        crossover_popln = crossover_popln + seq1[i]
    for i in range(crossover_point1-1, crossover_point2):
        crossover_popln = crossover_popln + seq2[i]
    for i in range(crossover_point2, 5):
        crossover_popln = crossover_popln + seq1[i]
    return crossover_popln

# this will do one point crossover for offsprings


def OnePointCrossover(seq1, seq2, crossover_point):
    Crossover_Popln = ''
    for i in range(0, crossover_point):
        Crossover_Popln = Crossover_Popln + seq1[i]
    for i in range(crossover_point, 5):
        Crossover_Popln = Crossover_Popln + seq2[i]
    return Crossover_Popln

# this will do crossover
# basically a crossover function


def CrossoverFunction(population):
    population_result = []
    if (c == 0):
        point = random.randint(1, 4)
        x = 1
        while (x < p):
            par1 = population_binary[x-1]
            par2 = population_binary[x]
            child1 = OnePointCrossover(str(par1), str(par2), int(point))
            child2 = OnePointCrossover(str(par2), str(par1), int(point))
            population_result.append(child1)
            population_result.append(child2)
            x = x+2
        if (x == p):
            population_result.append(OnePointCrossover(
                str(population_binary[0]), str(population_binary[p-1]), int(point)))

    elif (c == 1):
        point1 = random.randint(1, 4)
        point2 = random.randint(point1+1, 5)
        x = 1
        while (x < p):
            par1 = population_binary[x-1]
            par2 = population_binary[x]
            child1 = TwoPointCrossover(par1, par2, point1, point2)
            child2 = TwoPointCrossover(par2, par1, point1, point2)
            population_result.append(child1)
            population_result.append(child2)
            x = x+2
        if (x == p):
            population_result.append(TwoPointCrossover(
                population_binary[0], population_binary[p-1], point1, point2))
    population.clear()
    return population_result

# this will do mutation
# basically a mutation function


def Mutation():
    num = random.randint(1, p)
    n_par = ''
    par = population_binary[num-1]
    if (m == 0):
        for i in range(5):
            if (par[i] == '0'):
                n_par = n_par + '1'
                break
            else:
                n_par = n_par + par[i]
        for i in range(len(n_par), 5):
            n_par = n_par + par[i]
    elif (m == 1):
        bit = random.randint(1, 4)
        bit1 = random.randint(bit, 5)
        for i in range(len(par)):
            if (i == bit-1):
                n_par = n_par + par[bit1-1]
            elif (i == bit1-1):
                n_par = n_par + par[bit-1]
            else:
                n_par = n_par + par[i]
    population_binary.clear()
    population_fitness.clear()
    population.pop(num-1)
    population.append(BinaryToDecimalConverter(n_par))
    population.sort(reverse=True)
    DecimalPopToBinaryPop(population)
    CalculateFitness(population)

# this will do iteration of the genetic algorithm


def Iterate():
    population_new = CrossoverFunction(population)
    population_binary = population_new
    population.clear()
    BinaryPopToDecimalPop()
    population_new.clear()
    population.sort(reverse=True)
    population_binary.clear()
    DecimalPopToBinaryPop(population)
    Mutation()
    PrintPopulationValues()
    print('Total fitness value is : ', FindTotalFitness())

# this will print the population along with its binary value and fitness value


def PrintPopulationValues():
    print('\n')
    print('\n***************************************************\n')
    print('Population     Binary-string        Fitness')
    for i in range(p):
        print(population[i], '        -      ', population_binary[i],
              '      -      ', population_fitness[i])


# this code basically does the genetic algorithm until the termination condition is met
def Genetic():
    if (t == 1):
        for i in range(it):
            Iterate()
    elif (t == 0):
        counter = 0
        temp = FindTotalFitness()
        while (counter < x):
            Iterate()
            temp1 = FindTotalFitness()
            if (temp1 <= temp):
                counter += 1
            else:
                counter = 0
            temp = temp1
    print('\n***************************************************\n')
    print('Highest fitness value achieved :- ', population_fitness[0])
    print('Binary value of the population with highest fitness :- ',
          population_binary[0])
    print('Decimal value of the population with highest fitness :- ',
          population[0])
    print('Total fitness of all population when termination condition is met :- ',
          FindTotalFitness())
    print('\n\n\n\nCode is Executed succesfully for the given input\n')
    print('***************************************************\n')


# now we will be calling each function step by step to implement the algorithm
# it will generate random population
RandomPopulationGenerator()
# this will sort the code
population.sort(reverse=True)
# this will change  the population from decimal to binary
DecimalPopToBinaryPop(population)
# this will calculate the fitness for the given population
CalculateFitness(population)
# this will print the population along with its binary value and fitness value
PrintPopulationValues()
# this will print the fitness total of the iteration
print('Total fitness value for this iteration is : ', FindTotalFitness())
# this will invoke the algorithm
Genetic()

# Name:- Abhishikth Boda
# Roll Number:- S20210010044
# Subject:- Artificial Intelligence
# Section:- 1
# Assignment:- 1
# Date:- 15-03-2023

# <-----------------THE END-------------------->
