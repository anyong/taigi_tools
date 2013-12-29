import pinyin
import unittest

class PinyinTests(unittest.TestCase):

    def test_unicode_tonemarks_to_numbers(self):
        s = u'pap pa\u0300p'
        self.failIf(pinyin.tailo_to_num(s) != u'pap pap3')

    def test_string_to_tonemarks(self):
        s = 'pap pap3 pap'
        self.failIf(pinyin.tailo_to_tonemark(s) != u'pap pa\u0300p pap')

    def test_unicode_syllable_to_tonemark(self):
        s = u'pap'
        t = u'3'
        self.failIf(pinyin.tailo_syl_to_tonemark(s, t) != u'pa\u0300p')
        
    def test_string_syllable_to_tonemark(self):
        s = 'pap'
        t = '3'
        self.failIf(pinyin.tailo_syl_to_tonemark(s,t) != u'pa\u0300p')
    

def main():
    unittest.main()

if __name__ == '__main__':
    main()
