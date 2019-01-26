""" Python challenge 1
"""

# Mapping strings
from string import ascii_lowercase as letters

mapping = letters[2:] + letters[:2]
trantab = str.maketrans(letters, mapping)


def run_translation(ipt):
    print(ipt.translate(trantab))


if __name__ == '__main__':
    to_translate = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq ' \
               'glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. ' \
               'lmu ynnjw ml rfc spj.'

    to_translate2 = 'http://www.pythonchallenge.com/pc/def/map.html'

    run_translation(to_translate)
    run_translation(to_translate2)

# http://www.pythonchallenge.com/pc/def/ocr.html
