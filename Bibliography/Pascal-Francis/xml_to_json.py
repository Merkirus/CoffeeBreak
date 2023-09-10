import xmltodict, json
import os, sys

file = sys.argv[1]

file_basename = os.path.splitext(file)[0]

data = ''

with open(file) as f:
    lines = f.readlines()
    for line in lines:
        data += line

out = xmltodict.parse(data)

out = out['ListRecords']['metadata']

with open(f'{file_basename}.json', 'w+', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=4)
