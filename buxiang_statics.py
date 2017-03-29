import re
import numpy as np
from scipy.stats import pearsonr

inputs = []
result = []

with open('buxiang_to_fit.txt', 'r') as inputfile:
  for line in inputfile:
    i, r = line.split('\t')
    inputs.append(float(i))
    result.append(int(r))

inputs = np.array(inputs)

result = np.array(result)

ra = pearsonr(inputs, result)

print(ra)