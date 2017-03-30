import re
import numpy as np
from scipy.stats import pearsonr

inputs = []
result = []

with open('ru_to_fit.txt', 'r') as inputfile:
  for line in inputfile:
    i, r = line.split('\t')
    inputs.append(int(i))
    result.append(int(r))

inputs = np.array(inputs)

result = np.array(result)

r = pearsonr(inputs, result)

print(r)