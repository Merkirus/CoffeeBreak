import pycurl
import random

nums = "0123456789"

random_id = "".join(random.choices(nums, k = 7))

url = 'https://pascal-francis.inist.fr/vibad/index.php?action=export'
post_data = f'selection%5B%5D={random_id}&exportType=exportListSelected&exportFormat=xmlDC&via=expertSearch'
output_filename = f'{random_id}.txt'

with open(output_filename, 'wb') as f:
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, post_data)
    c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
    c.setopt(pycurl.WRITEDATA, f)
    c.perform()
    c.close()
