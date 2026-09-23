import marko

class TemplateNode : 
    
    def __init__(self, type) : 
        self.type = type 
        self.children = []
        self.text = []

    def add_child(self, node) : 
        self.children.append(node)

    def add_text(self, text) : 
        self.text.append(text)

    def get_type(self) : 
        return self.type

    def find_children(self, types : list) : 
        childs = []
        for child in self.children : 
            childs.extend( child.find_children(types) )
            if child.type in types : 
                childs.append(child)

        return childs
    
    def get_text(self) : 
        return ''.join(self.text)

    def get_entire_text(self) : 
        text = []
        for child in self.children : 
            text.extend( child.get_text() )
        text.extend( self.text )        
        return ''.join(text)

class TemplateNodeVisitor : 

    def __init__(self) : 
        self.node_stack = []  

    def visit(self, node) : 
        root_node = TemplateNode('ROOT')
        self.node_stack.append( (0, root_node) ) 

        for child in node.children : 
            if isinstance(child, marko.block.Heading) : 
                self.visit_heading(child) 
            if isinstance(child, marko.block.List) : 
                self.visit_list(child)
            if isinstance(child, marko.block.ListItem) : 
                self.visit_listitem(child) 
            if isinstance(child, marko.block.Paragraph) : 
                self.visit_paragraph(child)
            if isinstance(child, marko.inline.Emphasis) : 
                self.visit_emphasis(child)            
            if isinstance(child, marko.inline.RawText) : 
                self.visit_rawtext(child) 
            if isinstance(child, marko.inline.Link) : 
                self.visit_link(child)            
            if isinstance(child, marko.inline.CodeSpan) : 
                self.visit_codespan(child)
            if isinstance(child, marko.inline.StrongEmphasis) : 
                self.visit_strong_emp(child)

        return root_node

    def visit_children(self, node) : 
        for child in node.children : 

            if isinstance(child, marko.block.List) : 
                self.visit_list(child)
            if isinstance(child, marko.block.ListItem) : 
                self.visit_listitem(child) 
            if isinstance(child, marko.block.Paragraph) : 
                self.visit_paragraph(child)
            if isinstance(child, marko.inline.Emphasis) : 
                self.visit_emphasis(child)            
            if isinstance(child, marko.inline.RawText) : 
                self.visit_rawtext(child) 
            if isinstance(child, marko.inline.Link) : 
                self.visit_link(child)            
            if isinstance(child, marko.inline.CodeSpan) : 
                self.visit_codespan(child)
            if isinstance(child, marko.inline.StrongEmphasis) : 
                self.visit_strong_emp(child)

    def visit_heading(self, node : marko.block.Heading) : 

        while self.node_stack and self.node_stack[-1][0] >= node.level : 
            self.node_stack.pop()
        
        new_heading_node = TemplateNode('Heading')
        self.node_stack[-1][1].add_child(new_heading_node) 
        self.node_stack.append( ( node.level, new_heading_node ) ) 

        self.visit_children(node)

    def visit_list(self, node) : 
        new_list_node = TemplateNode('List')
        self.node_stack[-1][1].add_child( new_list_node ) 
        
        self.node_stack.append( ( self.node_stack[-1][0] + 1, new_list_node ) ) 
        self.visit_children(node)
        self.node_stack.pop()

    def visit_listitem(self, node : marko.block.ListItem) : 
        new_listitem_node = TemplateNode('ListItem')  
        self.node_stack[-1][1].add_child(new_listitem_node)
        
        self.node_stack.append( ( self.node_stack[-1][0] + 1, new_listitem_node) )
        self.visit_children(node)
        self.node_stack.pop()

    def visit_paragraph(self, node) : 
        new_paragraph = TemplateNode('Paragraph')
        self.node_stack[-1][1].add_child(new_paragraph)

        self.node_stack.append( ( self.node_stack[-1][0] + 1, new_paragraph) )
        self.visit_children(node)
        self.node_stack.pop()

    def visit_emphasis(self, node) : 
        self.visit_children(node)
    
    def visit_link(self, node) : 
        self.visit_children(node)

    def visit_codespan(self, node) : 
        self.node_stack[-1][1].add_text(node.children)
    
    def visit_strong_emp(self, node) : 
        self.visit_children(node)

    def visit_rawtext(self, node) :         
        self.node_stack[-1][1].add_text(node.children)

def parse_template(md_text) : 
    m_tree = marko.parse(md_text)

    visitor = TemplateNodeVisitor()
    root = visitor.visit( m_tree )

    return root

def print_nodes(node : TemplateNode) : 
    node_text = node.get_text()
    print(f'{node.type} : {node_text}')
    for child in node.children : 
        print_nodes(child)

if __name__ == '__main__' :     
    prt_text = '''
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
    m_tree = marko.parse(prt_text)
    print(m_tree)
    print()

    visitor = TemplateNodeVisitor()
    root = visitor.visit( m_tree )
    print_nodes(root)