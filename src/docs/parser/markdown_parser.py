from src.tools.template_node_visitor import parse_template, TemplateNode

class MarkdownParser : 

    def __init__(self, md_text) : 
        self.md_text = md_text
        self.root = parse_template(md_text) 
        
    def get_headings(self) : 
        return self.root.find_children(['Heading'])
    
def test_text() : 
    return  '''
<!--- Provide a general summary of your changes in the Title above -->

## Description
<!--- Describe your changes in detail -->
this pull request represents changes.

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
    text = test_text()
    parser = MarkdownParser(text)
    headings = parser.get_headings()
    print( headings )