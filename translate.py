#!/usr/bin/python

from sys import stdout
import fileinput
import codecs

E2T = {
    u'A': u'\u2206',
    u'B': u'\u0181',
    u'C': u'\u03fe',
    u'D': u'\u0189',
    u'E': u'\u0404',
    u'F': u'\u20a3',
    u'G': u'\u20b2',
    u'H': u'\u1fcc',
    u'I': u'\u1eca',
    u'J': u'J', # does not get translated
    u'K': u'\u041a',
    u'L': u'\u2c62',
    u'M': u'\u03fa',
    u'N': u'\u0418',
    u'O': u'\xd8',
    u'P': u'\u2c68',
    u'Q': u'Q', # does not get translated
    u'R': u'\u042f',
    u'S': u'\u03e8',
    u'T': u'\u20ae',
    u'U': u'\u1e72',
    u'V': u'V', # does not get translated
    u'W': u'\u0428',
    u'X': u'X', # does not get translated
    u'Y': u'\u03ab',
    u'Z': u'Z', # does not get translated
}

def translate_english(str):
    if not isinstance(str, basestring):
        raise TypeError
    return u''.join(map(lambda x: E2T[x] if x in E2T else x, unicode(str).upper()))


if __name__ == '__main__':
    stdout = codecs.getwriter('utf-8')(stdout)
    for line in fileinput.input():
        stdout.write(translate_english(line))