import re
import jieba.posseg as pseg


like = re.compile('好比')

def getcuts(words):
  s = [('%s_%s' % (word,flag)) 
        for word, flag in words
        if re.search(like,word)]
  return ' '.join(s)

with open('haobi_extracted.txt', 'r') as inputfile:
  with open('haobi_splited.txt', 'w') as outputfile:
    for line in inputfile:
      sentences, tag = line.split('\t')
      words = pseg.cut(sentences)

      outputfile.write(getcuts(words) + '\t' + tag)