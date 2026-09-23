from src.docs.text_doc import TextDoc
from src.docs.parser.html_parser import HTMLParser
import numpy as np
from src.text_processing.text_processor import TextProcessor

class HtmlDoc(TextDoc) : 
    ''' This class represents an HTML document '''

    def __init__(self, html_text : str, text_proc : TextProcessor) :
        super().__init__(html_text, text_proc)
        self.html_text = html_text
        self.html_parser = HTMLParser(html_text)
        self.text_proc : TextProcessor = text_proc

    def get_html_text(self) : 
        return self.html_text

    def get_html_tags(self) : 
        return self.html_parser.get_head_tags()

    def get_head_tags_text(self) : 
        return self.html_parser.get_head_texts()
    
    def get_heading_texts(self) : 
        return [ h['text']  for h in self.html_parser.get_head_texts()]
    
    def get_tag_list(self) : 
        return np.unique( [ tag.name for tag in self.tags ] ).tolist()

    def get_comments(self) : 
        return self.html_parser.get_comments()
    
    def get_comment_words(self) : 
        comment_text = ' '.join(self.get_comments())
        return self.text_proc.processing(comment_text) ####

    def num_comments(self) : 
        return len( self.get_comments() )        

    def num_tags(self) : 
        temp_tags = [ tag.name for tag in self.html_parser.get_tags() ]
        return {
            name : temp_tags.count(name) for name in temp_tags
        }

    def num_tag_categories(self) : 
            temp_tags = [ to_tag_category(tag.name) for tag in self.html_parser.get_tags() ]
            return {
                name : temp_tags.count(name) for name in temp_tags
            }
   
def to_tag_category(tag_name : str) : 
    if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] : 
        return 'heading'
    if tag_name in ['ol', 'ul'] : 
        return 'list'
    if tag_name == 'a' : 
        return 'link'
    if tag_name == 'li' : 
        return 'listitem'  
    if tag_name == 'img' : 
        return 'image'
    if tag_name == 'code' : 
        return 'code'
    
    return tag_name 
    