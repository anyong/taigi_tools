import unicodedata
import re

#Tailo with tone marks to tone numbers placed after each syllable
#Returns with specified type ('utf-8' for <unicode>, 'string' for <string>)
#Defaults to same as parameter
def tailo_to_num(string, encoding='default'):
    
    if (type(string) == str):
        string = string.decode(encoding='utf-8', errors='strict')
        if (encoding == 'default'):
            encoding = 'string'
    
    if encoding=='default':
        encoding = 'utf-8'
    
    ustring = unicodedata.normalize('NFD', string)
    newstr = ''
    tone = ''
    
    for i, c in enumerate(ustring):
        if (c==u'\u030d'):
            tone='8'
        elif (c==u'\u0304'):
            tone='7'
        elif (c==u'\u0301'):
            tone='2'
        elif (c==u'\u0300'):
            tone='3'
        elif (c==u'\u0302'):
            tone='5'
        else:
            if (re.search('[^A-Za-z]', c) != None):
                newstr+=tone
            newstr+=c
        if (i == len(ustring)-1 and tone != ''):
            newstr+=tone

    if encoding == 'utf-8':
        return newstr
    else:
        return str(newstr)

#Tailo with numbered tones converted to tone marks (with utf-8 encoding)
def tailo_to_tonemark(string):
    
    if (type(string) == str):
        string = string.decode(encoding='utf-8', errors='strict')
    
    syllable = ''
    result = ''
    for i, c in enumerate(string):
        if re.search('[A-Za-z]', c):
            syllable += c
        elif re.search('\d', c) and syllable != '':
            result += tailo_syl_to_tonemark(syllable, c)
            syllable = ''
        elif syllable != '':
            result += syllable + c
            syllable = ''
        else:
            result += c
    
    if syllable != '':
        result += syllable
    
    return result

# Find the highest-sonority vowel in a syllable
def get_marked_vowel(s):
    vowels = [u'a', u'A', u'oo', u'OO', u'e', u'E', u'o', u'O', u'i', u'I', u'u', u'U', u'n', u'N', u'm', u'M']
    for v in vowels:
        pos = s.find(v)
        if pos >= 0:
            return pos

#Converts one syllable of tailo without a tone mark into a (unicode) syllable with tone t (int)
def tailo_syl_to_tonemark(syl, t):
    if (type(syl) == str):
        syl = syl.decode(encoding='utf-8', errors='strict')

    tones = {
        '2': u'\u0301',
        '3': u'\u0300',
        '5': u'\u0302',
        '7': u'\u0304',
        '8': u'\u030d',
    }
    
    tonelist = ['2', '3', '5', '7', '8']
    
    if t not in tonelist:
        return syl
    else:
        pass
        
    tonepos = get_marked_vowel(syl)
    newsyl = u''
    if tonepos >= 0:
        for i, c in enumerate(syl):
            if tonepos == i:
                newsyl += c + tones[t]
            else:
                newsyl += c
    else:
        pass
                
    return newsyl