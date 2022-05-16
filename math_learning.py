import math as m
import matplotlib.pyplot as plt
import numpy as np
import time

a = np.arange(0,10000000)

start = time.time()
np.power(a,7)
end = time.time()

print(end-start)
