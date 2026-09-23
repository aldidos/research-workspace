import sys
sys.path.append('.')
from src.util.str_util import search_word_categories
from src.docs.html_doc import HtmlDoc
from src.tools.markdown_processiong import to_html_text
from src.text_processing.text_processor import TextProcessor
from src.text_processing.text_proc_factory import TextProcFactory

class MDDocFeatureExtractor : 

    def __init__(self, text_proc : TextProcessor) : 
        self.text_proc = text_proc

    def extract(self, md_text : str) : 
        html_doc = HtmlDoc(to_html_text(md_text), self.text_proc)

        num_tags = html_doc.num_tags()        
        num_tag_categories = html_doc.num_tag_categories()
        heading_titles = html_doc.get_heading_texts()
        head_tag_text = html_doc.get_head_tags_text()
        words = html_doc.get_words()
        n_comments = html_doc.num_comments()
        n_comment_size = len(html_doc.get_comment_words())  

        tag_names = list( map(lambda x : x, num_tag_categories.keys()) ) 

        return { 
            'num_tags' : num_tags, 
            'num_tag_categories' : num_tag_categories,
            'tag_names' : tag_names,
            'head_tag_text' : head_tag_text,
            'heading_titles' : heading_titles,            
            'n_words' : len(words),
            'n_comments' : n_comments, 
            'n_comment_size' : n_comment_size
        }
    
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
    extractor = MDDocFeatureExtractor(text_proc)
    features = extractor.extract(text)
    print(features)

if __name__ == '__main__' : 
    main()