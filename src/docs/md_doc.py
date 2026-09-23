from src.docs.text_doc import TextDoc
from src.docs.parser.markdown_parser import MarkdownParser
from src.text_processing.text_processor import TextProcessor

class MDDoc(TextDoc) : 
    ''' This class represents a Markdown(MD) document '''
    def __init__(self, markdown_text : str, text_proc : TextProcessor) : 
        super().__init__(markdown_text, text_proc)
        self.markdown_text = markdown_text
        self.parser = MarkdownParser(self.markdown_text) 

    def get_md_text(self) : 
        return self.markdown_text
    
    def get_heading_titles(self) : 
        return self.parser.get_headings() 
    