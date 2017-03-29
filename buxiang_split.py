import re
import jieba.posseg as pseg

noun = re.compile('^n$')
verb = re.compile('v')
like = re.compile('.?像')

def getcuts(words):
  s = [('%s_%s' % (word,flag)) 
        for word, flag in words
        if re.search(noun,flag) or (re.search(verb, flag) and re.search(like, word))]
  return ' '.join(s)

with open('buxiang_extracted.txt', 'r') as inputfile:
  with open('buxiang_splited.txt', 'w') as outputfile:
    for line in inputfile:
      sentences, tag = line.split('\t')
      words = pseg.cut(sentences)

      outputfile.write(getcuts(words) + '\t' + tag)
