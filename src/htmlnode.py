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
        raise NotImplementedError()
    
    def props_to_html(self):
        res = ' '
        for key, value in self.props.items():
            res = res + key + '="' + value + '" '
        return res
    
    def __repr__(self):
        return f'{self.tag}\n{self.value}\n{self.children}\n{self.props}'