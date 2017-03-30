import re
from matching import Match_xiang
from matching import Match_ru
from matching import Match_fang
from matching import Match_si
from matching import Match_hao
from matching import Match_yiyang


handlers = [
  Match_xiang(),
  Match_ru(),
  Match_fang(),
  Match_si(),
  Match_hao(),
  Match_yiyang()
]

def predict(line):
  result = 0
  for index, handler in enumerate(handlers):
    result = handler.predict(line)
    if result != 0:
      break
  return result

with open('weicheng_sentences.txt', 'r') as inputfile:
  with open('weicheng_with_improved_tag.txt', 'w') as outputfile:
    for line in inputfile:
      new_line = line.rstrip() + '\t' + str(predict(line))
      outputfile.write(new_line + '\n')

