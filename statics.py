all_lines = 0
is_biyu_lines = 0
t = 0
with open('weicheng_biyu_only.txt', 'r') as inputfile:
  for line in inputfile:
    all_lines += 1
    if line.endswith('1\n'):
      is_biyu_lines += 1

print('all_lines %d' % all_lines)
print('is_biyu_lines %d' % is_biyu_lines)
print('rate  {0:.1%}'.format(is_biyu_lines / float(all_lines)))