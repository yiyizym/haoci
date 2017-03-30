import re
like = re.compile('如_v')
with open('ru_splited.txt', 'r') as inputfile:
  with open('ru_to_fit.txt', 'w') as outputfile:
    for line in inputfile:
      score = 0
      temp,tag = line.split('\t')
      if temp == '':
        outputfile.write('%s\t%s' %(score,tag))
        continue

      score = 1 if re.search(like, temp) != None else 0
      
      outputfile.write('%s\t%s' %(score,tag))