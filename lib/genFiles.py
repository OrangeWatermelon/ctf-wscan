import re
import config
class GenFiles:
    def get(self):
        with open('dict/default.txt') as fp:
            data = fp.read()
            data = data.split()
        return list(set(data))
    def getf(self):
        r = []
        with open('dict/default.txt') as fp:
            data = fp.read()
            data = data.split()
            for i in data:
                cmp = re.compile(r'(.*/)?(.*\.[a-zA-Z]*$)')
                res = cmp.findall(i)
                if len(res) > 0:
                    r.append(i)
        return list(set(r))
    def getphp(self):
        r = []
        with open(config.path+'\dict\default.txt') as fp:
            data = fp.read()
            data = data.split()
            for i in data:
                if i[-3:] == 'php':
                    r.append(i)
        return list(set(r))