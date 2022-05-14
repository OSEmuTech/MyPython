import math as m
import matplotlib.pyplot as plt
import numpy as np
import time

a = np.arange(0,100000000)
start = time.time()
a*a*a
end = time.time()
print(end-start)
