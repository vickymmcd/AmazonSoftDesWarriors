'''
helper functions for super shoppers final product for softdes spring 2017
formats dates and times, and prepares data for machine learning process
'''

import time

t = time.gmtime()
print(t)
print(time.strftime("%x, %X", t))


def get_date(epoch_time):
    t = time.gmtime(epoch_time)
    return t

def add_day(epoch_time):
    return epoch_time + (3600 * 24)

t = time.time()
t = t + (3600 * 24)
for i in range(100):
    t = add_day(t)
    print(get_date(t))