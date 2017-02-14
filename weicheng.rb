File.open('weicheng.txt', 'r') do |f|
  current = 0
  result = []
  regexp = Regexp.new(['[^不]像','似','如','一样','仿','好比','成了','俨然'].join('|'));
  f.each_line('。') do |line|
    line.gsub!(/[\t+\s+]/, '')
    if line.match(regexp)
      result << line
    end
  end

  puts result
  puts result.length

end

