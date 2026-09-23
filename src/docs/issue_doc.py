from src.text_processing.text_processor import TextProcessor

class IssueDoc : 

    def __init__(self, doc : dict, text_proc : TextProcessor) :  
        self.title = doc['title']
        self.labels = doc['labels']
        self.body_text = doc['body']
        self.text_proc = text_proc
    
    def get_title(self) : 
        return self.title

    def get_labels(self) : 
        return self.labels
    
    def get_body_text(self) : 
        return self.body_text
    
    def get_title_words(self) : 
        return self.text_proc.processing(self.title)
    
    def get_body_text_words(self) : 
        return self.text_proc.processing(self.body_text)