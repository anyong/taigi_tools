import codecs

class Hanji:
    DATFILE = 'TLHJ.DAT'
    
    def __init__(self):
        f = codecs.open(self.DATFILE, 'r', 'utf-8')
        self.lines = []
        for l in f:
            self.lines.append(l.rstrip())
        self.lines.sort(key=len, reverse=True)
        self.conversion_table = []
        for l in self.lines:
            self.conversion_table.append(l.split('\t'))

    def to_hanji(self, string):
        for x in self.conversion_table:
            string = string.replace(x[0], x[1])
        return string
    
    def to_tailo(self, string):
        for x in self.conversion_table:
            string = string.replace(x[1], x[0]+' ')
        return string
    