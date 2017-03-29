import re
like = re.compile('似的_u|似地_d')
f = re.compile('_n|_v')
x = re.compile('x')
with open('si_splited.txt', 'r') as inputfile:
  with open('si_to_fit.txt', 'w') as outputfile:
    for line in inputfile:
      temp,tag = line.split('\t')
      temp = temp.split(' ')
      score = 0
      i = -1

      for index, item in enumerate(temp):
        if re.search(like, item):
          i = index
          break

      if i == -1:
        outputfile.write('%s\t%s' %(score,tag))
        continue

      temp = temp[:i]
      for index, item in enumerate(reversed(temp)):
        if re.search(f, item):
          score = 1
          break
        elif re.search(x, item):
          break

      outputfile.write('%s\t%s' %(score,tag))