import re
like = re.compile('像_v')
with open('buxiang_splited.txt', 'r') as inputfile:
  with open('buxiang_to_fit.txt', 'w') as outputfile:
    for line in inputfile:
      temp,tag = line.split('\t')
      temp = temp.split(' ')
      length = len(temp)
      score = 0
      i = -1

      for index, item in enumerate(temp):
        if re.search(like, item):
          i = index
          break

      if i == -1 or length == 1:
        score = 0
      elif i == length - 1:
        score = 0
      elif i != 0:
        prev = 1 if temp[i-1].endswith('_n') else 0.5
        nex = 1 if temp[i+1].endswith('_n') else 0.5
        score = prev * nex
      else:
        nex = 0.5 if temp[i+1].endswith('_n') else 0
        score = nex

      outputfile.write('%s\t%s' %(score,tag))