import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import product
from Dice_Rolls import ideal, sum_ideal, unbiased, sum_unbiased, biased_c1, sum_biased_c1, biased_c2, sum_biased_c2





###############################################
#
# Reading Everything From Dice_Rolls_Data.txt
#
############################################### 


with open('Dice_Rolls_Data.txt') as f:

    contents = f.readlines()
    
    ideal = np.asarray(contents)[0]
    sum_ideal =  np.array(contents)[1] 
    
    unbiased = np.array(contents)[2] 
    sum_unbiased = np.array(contents)[3] 
        
    biased_c1 = np.array(contents)[4] 
    sum_biased_c1 = np.array(contents)[5] 
    
    biased_c2 = np.array(contents)[6] 
    sum_biased_c2 = np.array(contents)[7] 




###############################################
#
# Function For Analysis
#
###############################################        


same_numbers = []
all_even = []
all_odd = []
mixed = []


def even_odd_mixed(x):
    
    for i in range(len(x)):
        
        if x[i][0] == x[i][1] == x[i][2] == x[i][3]:
            same_numbers.append(x[i])
            
        if x[i][0]%2 == x[i][1]%2 == x[i][2]%2 == x[i][3]%2 == 0:
            all_even.append(x[i])  
            
        if x[i][0]%2 == x[i][1]%2 == x[i][2]%2 == x[i][3]%2 != 0:
            all_odd.append(x[i]) 
            
    for i in range(len(x)):  
        
        if x[i] not in all_even and x[i] not in all_odd:
            mixed.append(x[i])
            
     
    return(same_numbers, all_even, all_odd, mixed)
    




###############################################
#
# Plotting Function For Analysis
#
###############################################    
    
    
def Plot(sample, types):
    
    Dice1, Dice2, Dice3, Dice4 = [], [], [], []

    for i in range(len(sample)):
    
        Dice1.append(sample[i][0])
        Dice2.append(sample[i][1])
        Dice3.append(sample[i][2])
        Dice4.append(sample[i][3])

    D = [Dice1, Dice2, Dice3, Dice4]
    Dice = ['Dice1', 'Dice2', 'Dice3', 'Dice4']
       

    for i in range(4):  
    
        plt.hist(D[i], bins = 12, color = colors[i], alpha = 0.4, label = Dice[i])
        plt.suptitle(f'Distribution of Numbers in 4 Die Thrown {len(D[i])} Times: {types}') 
    
    plt.xlim(0, 7)
    plt.xlabel('Number on Four Dice')
    plt.ylabel('Counts')
    plt.legend(loc = 'upper center', ncol = 4, bbox_to_anchor = (0.5, 1.06), fontsize = 8)  
      
    plt.savefig(f'Distribution_For_{types}_Dice.pdf')
    plt.show()
    plt.close()
 

###############################################
#
# Plots
#
###############################################  
 
 
colors = ['r', 'b', 'g', 'm'] 
types = ['Hypothetical', 'Unbiased', 'Biased Case 1', 'Biased Case 2'] 
 
   
Plot(ideal, types[0]) 
Plot(unbiased, types[1])
Plot(biased_c1, types[2])
Plot(biased_c2, types[3])  

samples = [ideal, unbiased, biased_c1, biased_c2]
sums = [sum_ideal, sum_unbiased, sum_biased_c1, sum_biased_c2]

for i in range(4):
    plt.hist(np.asarray(sums[i]), weights = np.ones_like(np.asarray(sums[i]))/len(np.asarray(sums[i])), color = colors[i], alpha = 0.5, edgecolor = colors[i],  label = types[i])
    plt.legend(loc = 'upper center', ncol = 4, bbox_to_anchor = (0.5, 1.06), fontsize = 8)     
plt.xlabel('Sum of Numbers on Four Dice')
plt.ylabel('Probability')    
plt.savefig('Probabilities_For_Biased_Unniased_dice.pdf')    
plt.show()    


###############################################
#
# All Same, All Odd, All Even, Mixed
#
############################################### 


print('##################################################################################### \n\n')

all_same, all_even, all_odd, mixed = even_odd_mixed(ideal)
print('In a hypothetical sample:')
print('All faces have same number ', len(all_same), 'times')
print('All faces have even number only ', len(all_even), 'times')
print('All faces have odd number only ', len(all_odd), 'times')
print('All faces have mixture of even and odd numbers ', len(mixed), 'times')
 
all_same1, all_even1, all_odd1, mixed1 = even_odd_mixed(unbiased)
print('In an unbiased sample:')
print('All faces have same number ', len(all_same1), 'times')
print('All faces have even number only ', len(all_even1), 'times')
print('All faces have odd number only ', len(all_odd1), 'times')
print('All faces have mixture of even and odd numbers ', 12960 - (len(all_even1) + len(all_odd1)), 'times')


all_same, all_even, all_odd, mixed = even_odd_mixed(biased_c1)
print('In a biased case 1 sample:')
print('All faces have same number ', len(all_same), 'times')
print('All faces have even number only ', len(all_even), 'times')
print('All faces have odd number only ', len(all_odd), 'times')
print('All faces have mixture of even and odd numbers ', 12960 - (len(all_even) + len(all_odd)), 'times')


all_same, all_even, all_odd, mixed = even_odd_mixed(biased_c2)
print('In a biased case 2 sample:')
print('All faces have same number ', len(all_same), 'times')
print('All faces have even number only ', len(all_even), 'times')
print('All faces have odd number only ', len(all_odd), 'times')
print('All faces have mixture of even and odd numbers ', 12960 - (len(all_even) + len(all_odd)), 'times')

print('\n\n ##################################################################################### \n\n')




###############################################
#
# Liklihood Ratio, H1: Biased C1, H2: Unbiased
#
###############################################

Liklihood1 = np.asarray(sum_biased_c1)/1296
Liklihood2 = np.asarray(sum_unbiased)/1296

LR = Liklihood1/Liklihood2


H1_LLR = (np.log10(Liklihood1/Liklihood2))
H2_LLR = (np.log10(Liklihood2/Liklihood1))


w1 = np.ones_like(H1_LLR) / len(H1_LLR)
w2 = np.ones_like(H2_LLR) / len(H2_LLR)


plt.hist(H1_LLR, bins = 50, weights = w1, color = 'red', alpha = 0.5, label = r"$H_1$")
plt.hist(H2_LLR, bins = 50, weights = w2, color = 'blue', alpha = 0.5, label = r'$H_2$')
plt.legend(loc = 0)

plt.title('Log Likelihood Ratio Histograms of Two Hypotheses')
plt.xlabel(r'$\log [{{\cal L}_{\mathbb{H}_{2}}}/{{\cal L}_{\mathbb{H}_{1}}} ] $')
plt.ylabel('Probability')
#plt.yscale('log')
plt.savefig('LLR.pdf')
plt.show()


plt.hist(Liklihood1/Liklihood2, bins = 50, weights = w1, color = 'red', alpha = 0.5, label = r"$H_1$")
plt.hist(Liklihood2/Liklihood1, bins = 50, weights = w2, color = 'blue', alpha = 0.5, label = r'$H_2$')
plt.legend(loc = 0)

plt.title('Likelihood Ratio Histograms of Two Hypotheses')
plt.xlabel(r'$[{{\cal L}_{\mathbb{H}_{2}}}/{{\cal L}_{\mathbb{H}_{1}}} ]$')
plt.ylabel('Probability')
plt.savefig('Liklihood_Ratio.pdf')
plt.show()

