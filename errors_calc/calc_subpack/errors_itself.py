'''Module that includes find_mean method'''
from . import Variance_loc, mean_value_loc

def ran_err(studt_coef, values):
    '''Method that find random error based on values and student coefficient'''
    return (Variance_loc.find_variance(values)/(len(values)-1)**(1/2))*studt_coef

def tot_error(studt_coef, values, syst):
    '''Method that find total error based on values, student coefficient and system error'''
    return (ran_err(studt_coef, values)**2+syst**2)**(1/2)

def rel_error(studt_coef, values, syst):
    '''Method that find relative error based on values, student coefficient and system error'''
    return tot_error(studt_coef, values, syst)/mean_value_loc.find_mean(values)
