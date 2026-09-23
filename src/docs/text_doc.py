from src.text_processing.text_processor import TextProcessor

class TextDoc : 
    ''' This class represents a text document '''

    def __init__(self, text : str, text_proc : TextProcessor) : 
        self.text = text
        self.text_proc = text_proc

    def get_text(self) : 
        return self.text
    
    def get_words(self) : 
        return self.text_proc.processing(self.text)