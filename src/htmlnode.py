class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, OtherNode):
        if type(OtherNode) != HTMLNode:
            raise Exception("Not valid TextNode")
        return (self.tag == OtherNode.tag and
           self.value == OtherNode.value and
           self.children == OtherNode.children and
           self.props == OtherNode.props)
    
    def to_html(self):
        # raise NotImplementedError()
        if self.tag is None:
            return self.value
        elif self.tag == 'p':
            return f'<p>{self.value}</p>'
        elif self.tag == 'a':
            for key, prop_value in self.props.items():
                return f'<a {key}="{prop_value}">{self.value}</a>'
        else:
            raise Exception("Something is wrong")
    
    def props_to_html(self):
        res = ' '
        for key, value in self.props.items():
            res = res + key + '="' + value + '" '
        return res
    
    def __repr__(self):
        return f'{self.tag}\n{self.value}\n{self.children}\n{self.props}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        return super().to_html()
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props=props)

    def to_html(self):
        if tag is None or tag == '':
            raise ValueError('Tag must be provided')
        if children is None or len(children) < 1:
            raise ValueError('Children must be provided')
        
        def recurse(self.tag, self.children):
            res = ''
            res += (f'<{self.tag}')

        return super().to_html()