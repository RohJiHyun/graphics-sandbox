import numpy as np  
#Using the Box-Müller method:
#see https://stackoverflow.com/questions/45991419/how-do-i-implement-the-probability-density-function-of-a-gaussian-distribution

def sample(mu, sig, s):
    """
        mu : mean
        sig : std
        s : size
    """
    r = np.zeros(s)
    for i in range(s):
        x = np.random.uniform(0,1,[2])
        z = np.sqrt(-2*np.log(x[0]))*np.cos(2*np.pi*x[1])
        r[i] = z*sig+mu
    return r



def sample_vae(mu, sig, s):
    """
        what about VAE Params trick?
        it seems to be same.
        mu : mean
        sig : std
        s : size
    """
    r = np.zeros(s)
    for i in range(s):
        x = np.random.normal(0,1)
        z = z
        r[i] = z*sig+mu
    return r


#https://stackoverflow.com/questions/11641629/generating-a-uniform-distribution-of-integers-in-c
def uniform_distribution(low,high, s) :
    """
    low : low range
    high high range
    s : size
    """
    import random
    import sys 
    RAND_MAX = sys.maxsize
    myRand = random.random()/(1.0 + RAND_MAX); 
    range_r = high - low + 1;
    myRand_scaled = (myRand * range_r) + low;
    return myRand_scaled