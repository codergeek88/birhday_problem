import numpy as np
import random
import matplotlib.pyplot as plt
#program to approximate the distribution of birthday cluster sizes
#through Monte Carlo methods

def shared(n):
    '''
    returns an array where index k denotes how many days have k birthdays
    '''
    max_shared = 0 #running maximum number of shared birthdays
    bdays = np.zeros(365, dtype=int) #array to keep track of birthdays
    for p in range(n):
        bday = random.randint(0, 364)
        bdays[bday] += 1
        max_shared = max(bdays[bday], max_shared)
    #freqs[k] denotes how many days contain k birthdays
    freqs = np.zeros(max_shared + 1)
    for b in bdays:
        freqs[b] += 1 #one more day with b birthdays
    return freqs

def prob(n, num_trials):
    '''
    approximate the distribution of birthday cluster sizes
    through Monte Carlo methods
    '''
    freqs = np.zeros(1)
    for t in range(num_trials):
        sample_freqs = shared(n)
        #resize vectors to equal length
        if len(freqs) < len(sample_freqs):
            freqs.resize(sample_freqs.shape)
        else:
            sample_freqs.resize(freqs.shape)
        freqs += sample_freqs
    return freqs / num_trials

def display(n, num_trials):
    '''
    display results of Monte Carlo birthday simulation
    '''
    freqs = prob(n, num_trials)
    #print results
    print("Birthday cluster size    " + "Instances (N = " + str(n) + ")")
    #show results starting at birthday cluster size = 1
    for k in range(1, len(freqs)):
        print(k, "                      ", freqs[k])
    #plot results
    plt.bar(range(1, len(freqs)), freqs[1:])
    plt.title("Frequencies of Shared Birthdays in a Sample of N = "
                + str(n) + " People")
    plt.xlabel("Birthday Cluster Size")
    plt.ylabel("Instances")
    plt.show()

#adjust parameters
n = 100
num_trials = 1000000
display(n, num_trials)
