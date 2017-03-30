import re
other_pattern = re.compile(r'|'.join(['[^不]像','似','一样','如','好比','成了','俨然']))
with open('weicheng_biyu_only.txt', 'r') as inputfile:
  with open('fang_extracted.txt', 'w') as outputfile:
    for line in inputfile:
      if re.search('仿', line) != None and re.search(other_pattern, line) == None:
        outputfile.write(line)