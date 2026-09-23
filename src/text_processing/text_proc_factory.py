import sys
sys.path.append('.')
from nltk.corpus import stopwords
from src.text_processing.tokenize import Tokenizer
from src.text_processing.non_english_word_filtering import NonEngWordFiltering
from src.text_processing.stop_word_removal import StopwordRemoval
from src.text_processing.issue_body_filtering import IssueBodyFiltering
from src.text_processing.text_processor import TextProcessor
from src.text_processing.strsplitter import StrSplitter

class TextProcFactory : 

    def create_default_proc(stop_word_list) : 
        stop_words = set( stopwords.words('english') ).union( stop_word_list )
        methods = [ 
            Tokenizer(), 
            NonEngWordFiltering(),
            StopwordRemoval(stop_words)
        ]
        return TextProcessor(methods)
    
    def create_issue_body_proc(stop_word_list) : 
        methods = TextProcFactory.create_default_proc(stop_word_list)
        methods.insert(0, IssueBodyFiltering())
        return TextProcessor(methods)

    def create_file_name_proc(stop_word_list, delimiter) : 
        methods = [ 
            StrSplitter(delimiter), 
            StopwordRemoval(stop_word_list)
         ]
        return TextProcessor(methods)

def test_text() : 
    return '''
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
'''

if __name__ == '__main__' : 
    pass