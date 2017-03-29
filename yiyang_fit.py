with open('yiyang_splited.txt', 'r') as inputfile:
  with open('yiyang_to_fit.txt', 'w') as outputfile:
    for line in inputfile:
      temp,tag = line.split('\t')
      temp = temp.split(' ')
      i = temp.index('一样_r')
      temp = temp[:i]
      score = 0
      p = 0
      for index,string in enumerate(reversed(temp)):
        if string.endswith(('跟_p')):
          p = 1
        if string.endswith(('_v', '_n')):
          score = 1
        if index > 7:
          break

      score *= p

      outputfile.write('%s\t%s' %(score,tag))

