all_lines = 0
bingo_lines = 0
t = 0
with open('weicheng_with_improved_tag.txt', 'r') as inputfile:
  for line in inputfile:
    all_lines += 1
    if line.endswith('1\n'):
      bingo_lines += 1

print('all_lines %d' % all_lines)
print('bingo_lines %d' % bingo_lines)
print('rate  {0:.1%}'.format(bingo_lines / float(all_lines)))