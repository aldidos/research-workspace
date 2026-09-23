import sys
sys.path.append('.')
from src.text_processing.text_processing import TextProcessing
from src.task.proc_task_runner import ProcTaskRunner

class TextProcessor : 

    def __init__(self, methods : list[TextProcessing]) : 
        self.methods = methods

    def processing(self, text) : 
        processed_text = text
        for method in self.methods : 
            processed_text = method.processing(processed_text)
        return processed_text
    
    def run_processing(self, text_docs) : ####
        task_runner = ProcTaskRunner()
        results = task_runner.run(self.processing, text_docs)
        return results