import re
from collections import defaultdict
m = defaultdict(int)
total = 0
is_biyu = 0
with open('buxiang_splited.txt', 'r') as inputfile:
  for line in inputfile:
    total += 1
    words, tag = line.split('\t')
    if tag == '1\n':
      is_biyu += 1
    words = words.split(' ')
    for word in (words):
      if re.search(r'\b像_v', word) != None:
        key = word + tag.rstrip()
        m[key] += 1

print(total) # 446
print(is_biyu) # 279
for key, value in m.items():
  print('%s %d' % (key, value))

# 正像_v 5
# 相像_v 3
# 像_v 367
# 有点像_v 1
# 活像_vn 6
# 倒像_v 7
# 想像_v 2
# 促像_v 1
# 好像_v 69
# 准像_v 1