import re

with open('weicheng_biyu_only.txt', 'r') as inputfile:
  with open('buxiang_extracted.txt', 'w') as outputfile:
    for line in inputfile:
      if re.search('[^不]像', line) != None:
        outputfile.write(line)
