import re
other_pattern = re.compile(r'|'.join(['似','如','一样','仿','好比','成了','俨然']))
with open('weicheng_biyu_only.txt', 'r') as inputfile:
  with open('buxiang_extracted.txt', 'w') as outputfile:
    for line in inputfile:
      if re.search('[^不]像', line) != None and re.search(other_pattern, line) == None:
        outputfile.write(line)
