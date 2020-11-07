from lib.scan import Scanner
from lib.genFiles import GenFiles
import requests
import random
import string

class Init:
    def __init__(self,url):
        self.url = url
    def start(self):
        gen = GenFiles()
        req1 = requests.get(self.url+''.join(random.sample(string.ascii_letters, 8)))
        req2 = requests.get(self.url)
        req3 = requests.get(self.url+''.join(random.sample(string.ascii_letters, 8))+'.asdfsdav')
        req4 = requests.get(self.url + ''.join(random.sample(string.ascii_letters, 8)) + '.php')
        if req1.content.decode('utf-8') == req2.content.decode('utf-8') and req1.status_code == req2.status_code:
            if req3.content.decode('utf-8') == req2.content.decode('utf-8') and req3.status_code == req2.status_code:
                if req4.content.decode('utf-8') == req2.content.decode('utf-8') and req4.status_code == req2.status_code:
                    print("扫描失败")
                    exit(0)
                else:
                    data = gen.getphp()
            else:
                data = gen.getf()
        else:
            data = gen.get()
        scan = Scanner(self.url,data)
        scan.start()