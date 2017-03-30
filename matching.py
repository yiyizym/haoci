import re
import jieba.posseg as pseg

class Match_ru(object):
  noun = re.compile('n')
  raw = re.compile('正如|譬如|宛如|正如')
  spec = re.compile('如_v')

  def __init__(self):
    pass

  def predict(self, sentence):
    words = pseg.cut(sentence)
    words = self.filteredcuts(words)
    score = 0
    if words == '':
      return score
    if re.search(self.spec, words) != None:
      score = 1
    return score


  def filteredcuts(self, words):
    s = [('%s_%s' % (word,flag)) 
          for word, flag in words
          if re.search(self.raw,word) or re.search(self.noun, flag)]
    return ''.join(s)


class Match_si(object):
  feature = re.compile('n|v|x')
  raw = re.compile('似的|似地')

  spec = re.compile('似的_u|似地_d')
  verb_noun = re.compile('_n|_v')
  punctuation = re.compile('x')

  def __init__(self):
    pass

  def predict(self, sentence):
    words = pseg.cut(sentence)
    words = self.filteredcuts(words)
    score = 0
    i = -1

    for index, item in enumerate(words):
      if re.search(self.spec, item):
        i = index
        break

    if i == -1:
      return score

    words = words[:i]
    for index, item in enumerate(reversed(words)):
      if re.search(self.verb_noun, item):
        score = 1
        break
      elif re.search(self.punctuation, item):
        break

    return score


  def filteredcuts(self, words):
    s = [('%s_%s' % (word,flag)) 
          for word, flag in words
          if re.search(self.raw,word) or re.search(self.feature, flag)]
    return s


class Match_xiang(object):
  noun = re.compile('^n$')
  verb = re.compile('v')
  raw = re.compile('.?像')

  spec = re.compile('像_v')

  def __init__(self):
    pass

  def predict(self,sentence):
    words = pseg.cut(sentence)
    words = self.filteredcuts(words)
    length = len(words)
    score = 0
    i = -1

    for index, item in enumerate(words):
      if re.search(self.spec, item):
        i = index
        break

    if i == -1 or length == 1:
      score = 0
    elif i == length - 1:
      score = 0
    elif i != 0:
      prev = 1 if words[i-1].endswith('_n') else 0.5
      nex = 1 if words[i+1].endswith('_n') else 0.5
      score = prev * nex
    else:
      nex = 0.5 if words[i+1].endswith('_n') else 0
      score = nex

    return score

  def filteredcuts(self, words):
    s = [('%s_%s' % (word,flag)) 
          for word, flag in words
          if re.search(self.noun,flag) or (re.search(self.verb, flag) and re.search(self.raw, word))]
    return s    

class Match_fang(object):
  """docstring for Match_fang"""
  noun = re.compile('n')
  raw = re.compile('仿佛')
  spec = re.compile('仿佛_d')

  def __init__(self):
    pass

  def predict(self, sentence):
    words = pseg.cut(sentence)
    words = self.filteredcuts(words)
    score = 0
    if words == '':
      return score
    if re.search(self.spec, words) != None:
      score = 1
    return score


  def filteredcuts(self, words):
    s = [('%s_%s' % (word,flag)) 
          for word, flag in words
          if re.search(self.raw, word) or re.search(self.noun, flag)]
    return ''.join(s)


class Match_hao(object):
  raw = re.compile('好比')
  spec = re.compile('好比_v')

  def __init__(self):
    pass

  def predict(self, sentence):
    words = pseg.cut(sentence)
    words = self.filteredcuts(words)
    score = 0
    if words == '':
      return score
    if re.search(self.spec, words) != None:
      score = 1
    return score

  def filteredcuts(self, words):
    s = [('%s_%s' % (word,flag)) 
          for word, flag in words
          if re.search(self.raw, word)]
    return ''.join(s)

class Match_yiyang(object):
  raw = re.compile('^[nvapcr]$')

  def __init__(self):
    pass

  def predict(self, sentence):
    words = pseg.cut(sentence)
    words = self.filteredcuts(words)
    score = 0
    try:
      i = words.index('一样_r')
    except Exception as e:
      return score
    
    words = words[:i]
    p = 0
    for index,string in enumerate(reversed(words)):
      if string.endswith(('跟_p')):
        p = 1
      if string.endswith(('_v', '_n')):
        score = 1
      if index > 7:
        break

    score *= p
    return score

  def filteredcuts(self, words):
    s = [('%s_%s' % (word,flag)) 
          for word, flag in words
          if re.search(self.raw, word)]
    return s
