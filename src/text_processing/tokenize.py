import sys
sys.path.append('.')
import nltk
from src.text_processing.text_processing import TextProcessing

class Tokenizer(TextProcessing) : 

    def processing(self, text : str) : 
        return [ w.lower() for w in nltk.word_tokenize(text) ]
    

def test_text() :     
    return '''
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
'''

if __name__ == '__main__' : 
    test_text = test_text()
    text_proc = Tokenizer()
    words = text_proc.processing(test_text)
    print(words)