with open('weicheng_with_simple_tag.txt', 'r') as inputfile:
  with open('weicheng_biyu_only.txt', 'w') as outputfile:
    for line in inputfile:
      if line.endswith('1\n'):
        outputfile.write(line)