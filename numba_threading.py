"""Module to test threading python"""
import timeit
import threading
import numpy as np
from numba import njit, prange

def strght_distribution(dots_number: 'int'):
    """Naive pi"""
    pi_sum = 0
    for i in prange(dots_number):
        cord_x, cord_y = np.random.random_sample(), np.random.random_sample()
        rad = ((0.5-cord_x)**2+(0.5-cord_y)**2)**0.5
        if rad < 0.5:
            pi_sum += 1
    return pi_sum*4/dots_number

@njit
def numba_distribution(dots_number: 'int'):
    """pi with numba boost"""
    pi_sum = 0
    for i in prange(dots_number,):
        cord_x, cord_y = np.random.random_sample(), np.random.random_sample()
        rad = ((0.5-cord_x)**2+(0.5-cord_y)**2)**0.5
        if rad < 0.5:
            pi_sum += 1
    return pi_sum*4/dots_number

def test_all():
    """Function to test threading boost"""
    t = threading.Thread(target=lambda : strght_distribution(1000000))
    t.start()
    strght_distribution(1000000)
    t.join()

if __name__ == '__main__':
    print(timeit.timeit('strght_distribution(1000000)','from __main__ import strght_distribution',
    number = 5), "pi = ",strght_distribution(1000000),"– без распараллеливания")
    print(timeit.timeit('numba_distribution(1000000)', 'from __main__ import numba_distribution',
    number = 5), "pi = ",numba_distribution(1000000), "– для njit")
    print(timeit.timeit(test_all,
    number = 5), "pi = ",strght_distribution(1000000),"– threading")
