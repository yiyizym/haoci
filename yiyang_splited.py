import re
# import thulac
# thu = thulac.thulac()
import jieba.posseg as pseg


def getcuts(words):
  s = [('%s_%s' % (word,flag)) 
        for word, flag in words
        if re.search('^[nvapcr]$',flag)]
  return ' '.join(s)

with open('yiyang_extracted.txt', 'r') as inputfile:
  with open('yiyang_splited.txt', 'w') as outputfile:
    for line in inputfile:
      sentences, tag = line.split('\t')
      words = pseg.cut(sentences)

      outputfile.write(getcuts(words) + '\t' + tag)
