import sys
sys.path.append('.')
from src.text_processing.text_processing import TextProcessing

class StrSplitter(TextProcessing) : 

    def __init__(self, delimiter : str) : 
        self.delimiter = delimiter

    def processing(self, text):
        return text.split(self.delimiter) 

if __name__ == '__main__' : 
    s = 'com-con.md'
    strSplitter = StrSplitter('.')
    res = strSplitter.processing(s)    
    print(res)
