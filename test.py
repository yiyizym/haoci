import re

s = r'又有人叫她“真理”，因为据说“真理”是赤裸裸的”。鲍小姐并未一丝不挂，所以他们修正为“局部的真理”。'
reg = u'.*?(?:！|。|？|(?:：“)|(?:[！。？]”))'
setences = re.findall(u'.*?(?:！|。|？|(?:：“)|(?:[！。？]”))', s)

print(setences)
print(len(setences))