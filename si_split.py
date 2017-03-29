import re
import jieba.posseg as pseg


f = re.compile('n|v|x')
like = re.compile('似的|似地')

def getcuts(words):
  s = [('%s_%s' % (word,flag)) 
        for word, flag in words
        if re.search(like,word) or re.search(f, flag)]
  return ' '.join(s)

with open('si_extracted.txt', 'r') as inputfile:
  with open('si_splited.txt', 'w') as outputfile:
    for line in inputfile:
      sentences, tag = line.split('\t')
      words = pseg.cut(sentences)

      outputfile.write(getcuts(words) + '\t' + tag)