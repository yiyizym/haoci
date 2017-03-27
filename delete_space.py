# File.open('weicheng.txt', 'r') do |f|
#   current = 0
#   result = []
#   regexp = Regexp.new(['[^不]像','似','[^不]如','一样','仿','好比','成了','俨然'].join('|'));
#   f.each_line('。') do |line|
#     line.gsub!(/[\t+\s+]/, '')
#     if line.match(regexp)
#       result << line
#     end
#   end

#   puts result
#   puts result.length

# end
import re

with open('weicheng.txt', 'r') as source, open('weicheng_no_space.txt', 'w') as target:
  for line in source:
    no_space_line = re.sub(r'\s', '', line)
    target.write(no_space_line)