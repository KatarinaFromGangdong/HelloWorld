#import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#create a function to measure the turbidity of water
def measure_turbidity(water):
    #convert the water sample to a numpy array
    water_sample = np.asarray(water)
    
    #calculate the turbidity of the water sample
    turbidity = np.sum(np.abs(water_sample))
    
    #return the turbidity level
    return turbidity

#create a list of water samples
water_samples = [10, 20, 30, 40, 50]

#create an empty list to store the turbidity of each sample
turbidity_levels = []

#loop through each sample and measure the turbidity
for sample in water_samples:
    turbidity = measure_turbidity(sample)
    turbidity_levels.append(turbidity)

#create a dataframe to store the data
data = {'Water Sample': water_samples, 'Turbidity': turbidity_levels