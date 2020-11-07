import requests
from config import *
class Scanner:
    def __init__(self,url,data):
        self.url = url
        self.data = data
    def start(self):
        end = '\t'*8
        if self.url[-1] != '/':
            self.url+='/'
        for i in self.data:
            req = requests.get(self.url+i)
            if req.status_code not in DISCODE:
                print('[{}]=>{}'.format(req.status_code,i)+end)
            else:
                print('[{}]=>{}'.format(req.status_code,i)+end,end='\r')
        print(end)
