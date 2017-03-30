import re
like = re.compile('好比_v')
with open('haobi_splited.txt', 'r') as inputfile:
  with open('haobi_to_fit.txt', 'w') as outputfile:
    for line in inputfile:
      score = 0
      temp,tag = line.split('\t')
      if temp == '':
        outputfile.write('%s\t%s' %(score,tag))
        continue

      score = 1 if re.search(like, temp) != None else 0
      
      outputfile.write('%s\t%s' %(score,tag))