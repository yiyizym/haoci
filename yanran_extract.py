import re
other_pattern = re.compile(r'|'.join(['[^不]像','似','一样','如','好比','仿']))
with open('weicheng_biyu_only.txt', 'r') as inputfile:
  with open('yanran_extracted.txt', 'w') as outputfile:
    for line in inputfile:
      if re.search('俨然', line) != None and re.search(other_pattern, line) == None:
        outputfile.write(line)