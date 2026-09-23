import sys
sys.path.append('.')
from bs4.element import Comment, NavigableString, Tag
from src.tools.markdown_processiong import to_html

class HTMLParser : 
    
    def __init__(self, html_text : str) : 
        self.comments = []
        self.tags = []
        self.soup = to_html(html_text)
        self.parse()

    def parse(self) : 
        for element in self.soup : 
            self.parse_element(element)

    def parse_element(self, element) : 
        if isinstance( element, Comment ) : 
            self.comments.append( element )
        elif isinstance( element, Tag ) : 
            self.tags.append(element)            
            if hasattr(element, 'children') : 
                for child in element.children : 
                    self.parse_element( child)

    def get_comments(self) :
        return self.comments
    
    def get_tags(self) : 
        return self.tags
    
    def get_head_tags(self) : 
        head_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        return [ tag for tag in self.tags if tag.name in head_tags ]
    
    def get_head_texts(self) : 
        head_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        return [ { 'head_tag' : tag.name, 'text' : tag.text } for tag in self.tags if tag.name in head_tags ]
    
    def get_paragraphs_text(self) : 
        return [ tag.text for tag in self.tags if tag.name == 'p' ] 
    
def test_prt_text() : 
    return  '''
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
    
if __name__ == '__main__' :  
    text = test_prt_text()
    parser = HTMLParser(text)
    # comments = parser.get_comments()
    # print( comments )

    para_texts = parser.get_paragraphs_text()
    print(para_texts)