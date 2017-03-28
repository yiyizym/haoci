import re
import jieba.posseg as pseg


def getcuts(words):
  s = [('%s_%s' % (word,flag)) 
        for word, flag in words]
  return ' '.join(s)

with open('buxiang_extracted.txt', 'r') as inputfile:
  with open('buxiang_splited.txt', 'w') as outputfile:
    for line in inputfile:
      sentences, tag = line.split('\t')
      words = pseg.cut(sentences)

      outputfile.write(getcuts(words) + '\t' + tag)
