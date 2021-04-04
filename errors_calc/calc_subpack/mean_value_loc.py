'''Module that includes find_mean method'''
def find_mean(values):
    '''Method that find mean value of values'''
    tot_sum = 0
    for i in range (len(values)):
        tot_sum += values[i]
    return tot_sum / len(values)
