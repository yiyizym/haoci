import re
with open('weicheng_sentences.txt', 'r') as inputfile:
    with open('weicheng_with_simple_tag.txt', 'w') as outputfile:
        pattern = re.compile(r'|'.join(['[^不]像','似的|似地','正如|譬如|宛如|正如','一样','仿佛','好比']))
        for line in inputfile:
            if pattern.search(line) != None:
                tag = '1'
            else:
                tag = '0'
            new_line = line.rstrip() + '\t' + tag
            outputfile.write(new_line + '\n')