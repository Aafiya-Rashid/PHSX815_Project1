import numpy as np
import random
import matplotlib.pyplot as plt
from itertools import product



#########################################################
#                                                       #
#           Generating Random Numbers                   #
#                                                       #
#########################################################

def discrete_distribution():
    
    """
    This distribution will generate numbers from 
    1 to 6 randomly from the numpy.random.uniform() 
    distribution
    
    """
     
    six_numbers = []
    
    for i in range(1, 7):
        n = np.int(np.random.uniform(i, i + 1))
        six_numbers.append(n)
    
    return(six_numbers) 



#########################################################
#                                                       #
#          Simulating An Unbiased Dice                  #
#                                                       #
#########################################################   
    
    
def unbiased_dice():
    
    dice1 = discrete_distribution()
    dice2 = discrete_distribution()
    dice3 = discrete_distribution()
    dice4 = discrete_distribution()
    
    return((random.choice(dice1), random.choice(dice2), random.choice(dice3), random.choice(dice4)))   
    
    

#########################################################
#                                                       #
#          Simulating A Biased Dice (Case 1)            #
#                                                       #
#########################################################   


def biased_dice_c1():
    
    dice1 = discrete_distribution() + [1, 3, 5] 
    dice2 = discrete_distribution() + [1, 3, 5]
    dice3 = discrete_distribution() + [2, 4, 6]
    dice4 = discrete_distribution() + [2, 4, 6]
    
    return((random.choice(dice1), random.choice(dice2), random.choice(dice3), random.choice(dice4)))  



#########################################################
#                                                       #
#          Simulating A Biased Dice (Case 2)            #
#                                                       #
#########################################################     
    
    
def biased_dice_c2():
    
    dice1 = discrete_distribution() + [1, 3, 5] 
    dice2 = discrete_distribution() + [1, 3, 5]
    dice3 = discrete_distribution() + [1, 3, 5]
    dice4 = discrete_distribution() + [1, 3, 5]
    
    return((random.choice(dice1), random.choice(dice2), random.choice(dice3), random.choice(dice4)))    



#########################################################
#                                                       #
#     Comparisions of Unbiased and Biased Samples       #        
#             with Hypothetical Sample                  #
#                                                       #
######################################################### 


def summ(test_tuple):

    tup = list(test_tuple)
    add = 0
    
    for i in tup:
        add += i
    return add




ideal = list(product(range(1, 7), repeat = 4))
sum_ideal = []

unbiased, sum_unbiased = [], []
biased_c1, sum_biased_c1 = [], []
biased_c2, sum_biased_c2 = [], []

for i in range(1296):
    
    sum_ideal.append(summ(ideal[i]))

for i in range(12960):

    unbiased.append(unbiased_dice())
    sum_unbiased.append(summ(unbiased_dice()))
    
    biased_c1.append(biased_dice_c1())
    sum_biased_c1.append(summ(biased_dice_c1()))
    
    biased_c2.append(biased_dice_c2())
    sum_biased_c2.append(summ(biased_dice_c2()))    
    



########################################################
#                                                      #
#      Writing Everything in Dice_Rolls_Data.txt       #
#                                                      #
########################################################

f = open("Dice_Rolls_Data.txt", "w+")
f.write(str(ideal)+'\n'+str(sum_ideal)+'\n'+str(unbiased)+'\n'+str(sum_unbiased)+'\n'+str(biased_c1)+'\n'+str(sum_biased_c1)+'\n'+str(biased_c2)+'\n'+str(sum_biased_c2))  


'''
with open('test.txt', 'w') as f:
    for tuple1, tuple2 in zip(ideal, sum_ideal):
        f.write('%s %s %s %s\n' % tuple1)           
'''
        
  
