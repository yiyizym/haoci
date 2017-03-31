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


reg = re.compile(u'.*?(?:！|。|？|(?:：“)|(?:[！。？]”))')
output_string = ''

def predict(sentence):
  result = 0
  for index, handler in enumerate(handlers):
    result = handler.predict(sentence)
    if result != 0:
      break
  return result

with open('weicheng.txt', 'r') as inputfile:
  with open('weicheng_with_tag.txt', 'w') as outputfile:
    for line in inputfile:
      line = re.sub(r'\s', '', line)
      for sentence in re.findall(reg, line):
        if len(sentence) > 0:
          sentence = sentence + '\t' + str(predict(sentence)) + '\n'
          output_string += sentence
    outputfile.write(output_string)

