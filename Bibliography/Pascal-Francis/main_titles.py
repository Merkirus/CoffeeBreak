import re

reg = r'<dc:title>(.*?)</dc:title>'

output = ''

with open('titles') as f:
    lines = f.readlines()
    for line in lines:
        match = re.search(reg, line.rstrip())
        if match:
            output += match.group(1)
            output += '\n'

print(output)

with open('titles', 'w') as f:
    f.write(output)
