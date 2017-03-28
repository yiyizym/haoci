import re

with open('weicheng_biyu_only.txt', 'r') as inputfile:
  with open('yiyang_extracted.txt', 'w') as outputfile:
    for line in inputfile:
      if re.search('一样', line) != None:
        outputfile.write(line)
