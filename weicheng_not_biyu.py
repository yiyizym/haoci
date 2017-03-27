with open('weicheng_with_simple_tag.txt', 'r') as inputfile:
  with open('weicheng_not_biyu.txt', 'w') as outputfile:
    for line in inputfile:
      if line.endswith('0\n'):
        outputfile.write(line)