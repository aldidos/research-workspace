import sys
sys.path.append('.')
from src.extraction.extractor.md_doc_feature_extractor import MDDocFeatureExtractor
from src.text_processing.text_processor import TextProcessor
from src.docs.prt_doc import PRTDoc
from src.text_processing.text_proc_factory import TextProcFactory

class PRTFeatureExtractor(MDDocFeatureExtractor) : 

    def __init__(self, text_proc : TextProcessor) : 
        super().__init__(text_proc)        
    
    def extract(self, prt_text) : 
        features = super().extract(prt_text)
        prt_doc = PRTDoc(prt_text, self.text_proc)
        
        checklist_items = prt_doc.get_checklist_items()
        features['n_checklist_items'] = len(checklist_items)

        return features
    
def main() : 
    text = '''
<!--- Provide a general summary of your changes in the Title above -->

## Description
<!--- Describe your changes in detail -->

## Motivation and Context
<!--- Why is this change required? What problem does it solve? -->
<!--- If it fixes an open issue, please link to the issue here. -->

## How Has This Been Tested?
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->

## Screenshots (if appropriate):

## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Refactor (changes the way we code something without changing its functionality)
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)

## Checklist:
<!--- Review the list before submitting your pull request -->
<!--- Leave the list intact for the code reviewer's use -->
- [ ] Latest master code has been merged into this branch
- [ ] No commented out code (if required, place // TODO above with explanation)
- [ ] No linting issues
- [ ] Build is successful
- [ ] Updated the documentation
- [ ] Added tests to cover changes
- [ ] All new and existing tests passed
'''
    text_proc = TextProcFactory.create_default_proc([])
    extractor = PRTFeatureExtractor(text_proc)
    features = extractor.extract(text)
    print(features)

if __name__ == '__main__' : 
    main()