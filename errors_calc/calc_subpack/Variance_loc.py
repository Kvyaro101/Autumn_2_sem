'''Module that includes find_variance method'''
from . import mean_value_loc

def find_variance(values):
    '''Method that find variance of values'''
    avg = float(mean_value_loc.find_mean(values))
    tot_sum = 0
    for i in range (len(values)):
        tot_sum += (values[i] - avg)**2
    return (tot_sum/len(values))**(1/2)
