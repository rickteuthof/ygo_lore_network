import json
import wget
import os.path
import string
from ygoprodeck import YGOPro

ygo = YGOPro()

json_object = ygo.get_cards()

def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.
 
Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.
 
"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    return filename

for card in json_object['data']:
    name = card['name']
    filename = format_filename(name)
    print()
    print(filename)
    filename = 'images/' + filename + '.jpg'
    if os.path.isfile(filename):
        continue
    url = card['card_images'][0]['image_url']
    wget.download(url, filename)

for card in json_object['data']:
    card_id = str(card['id'])
    print(card_id)
    filename = 'pics/' + card_id + '.jpg'
    if os.path.isfile(filename):
        continue
    url = card['card_images'][0]['image_url']
    wget.download(url, filename)
