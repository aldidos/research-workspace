import sys
sys.path.append('.')
from nltk.corpus import words
from src.text_processing.text_processing import TextProcessing
from src.text_processing.tokenize import Tokenizer

class NonEngWordFiltering(TextProcessing) : 

    def processing(self, word_list : list[str]) : 
        eng_words = set(words.words())    
        return [ word for word in word_list if word in eng_words or word.isalpha() ] 

def test_text() : 
    return '''
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
'''

if __name__ == '__main__' : 
    test_text = test_text()    
    text_proc = NonEngWordFiltering()
    words = text_proc.processing( Tokenizer().processing(test_text) )
    print(words)
