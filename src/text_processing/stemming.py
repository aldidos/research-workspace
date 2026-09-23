import sys
sys.path.append('.')
from nltk.stem import PorterStemmer
from src.text_processing.text_processing import TextProcessing
from src.text_processing.tokenize import Tokenizer

class WordStemming(TextProcessing) : 

    def __init__(self) : 
        self.stem = PorterStemmer()

    def processing(self, word_list : list[str]) : 
        return [ self.stem.stem(word) for word in word_list  ] 

def test_text() : 
    return '''
running runs runner run describe description
'''

if __name__ == '__main__' : 
    test_text = test_text()    
    text_proc = WordStemming()
    words = text_proc.processing( Tokenizer().processing(test_text) )
    print(words)
