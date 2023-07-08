"""
Create a 4 x 4 ndarray that only contains consecutive even numbers
from 2 to 32 (inclusive) and use boolean indexing to pick out the values that are
within 1/2 standard deviations of the mean
"""
import numpy as np
y = np.ndarray(shape=(4,4),dtype=int,buffer=np.arange(2,33,2))
mean_ = np.mean(y)
sd_ = np.std(y)
bool_mask = (y > (mean_ - 0.5*sd_)) & (y < (mean_ + 0.5*sd_))
print(y[bool_mask])
