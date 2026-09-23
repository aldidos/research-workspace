import sys
sys.path.append('.')
from src.text_processing.text_proc_factory import TextProcFactory
from src.docs.md_doc import MDDoc
from src.docs.parser.prt_parser import PRTParser
from src.text_processing.text_processor import TextProcessor
from src.util.entropy import compute_entropy

class PRTDoc(MDDoc) : 
    ''' This class represents a Pull Request Template document '''

    def __init__(self, prt_text : str, text_proc : TextProcessor) : 
        super().__init__(prt_text, text_proc)
        self.prt_text = prt_text
        self.prt_parser = PRTParser(prt_text) 

    def get_prt_text(self) : 
        return self.prt_text
    
    def get_checklist_items(self) :
        return self.prt_parser.get_checklist_items()
    
    def compute_info_features(self) : ####
        prt_words = self.text_proc.processing(self.prt_text)
        word_entropy = compute_entropy(prt_words)        
        word_entropy = float(word_entropy)
        size_checklist = len(self.prt_parser.get_checklist_items())
        n_headings = len(self.prt_parser.get_heading_titles() )
        return (word_entropy, n_headings, size_checklist)
    
if __name__ == '__main__' : 
    prt_text = '''
# Description
<i>Add your description here!</i>

# Checklist

To ensure a quick review and merge, please ensure:
- [ ] The PR has a understandable title and description explaining the _why_ and _what_.
- [ ] The PR is opened in draft if not ready for review yet.
   - If opened in draft, please allocate sufficient time (24 hours) after moving out of draft for review
- [ ] The branch is recent enough to not have merge conflicts upon creation.

# Ready to Land?
- [ ] Build is completely green
   - Submissions with test failures require tracking issue and approval of a CODEOWNER
- [ ] At least one +1 review by a CODEOWNER
- [ ] All -1 reviews are confirmed resolved by the reviewer 
   - Override/Marking reviews stale must be discussed with CODEOWNERS first
'''
    methods = TextProcFactory.create_default_proc([]) ####    
    text_proc = TextProcessor(methods)
    info_features = PRTDoc(prt_text, text_proc).compute_info_features()
    print(info_features)