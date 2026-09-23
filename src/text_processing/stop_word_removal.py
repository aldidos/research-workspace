import sys
sys.path.append('.')
from src.text_processing.text_processing import TextProcessing
from src.text_processing.tokenize import Tokenizer

class StopwordRemoval(TextProcessing) : 

    def __init__(self, stop_words) : 
        self.stop_words = stop_words

    def processing(self, words : list[str]) : 
        return [ word for word in words if word not in self.stop_words ]    
    
def test_text() : 
    return '''
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
'''

if __name__ == '__main__' : 
    test_text = test_text()    
    stop_words = set(['please', 'describe'])
    text_proc = StopwordRemoval(stop_words)
    words = text_proc.processing( Tokenizer().processing(test_text) )
    print(words)