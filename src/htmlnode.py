class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        for attr, value in self.props.items():
            html += f' {attr}="{value}"'
        return html

    def __repr__(self):
        children = ""
        for child in self.children:
            children += f"{child}\n"
        output = f"HTMLNode({self.tag}, {self.value})"
        if children:
            output = output[:-1] + f", children: {children})"
        if self.props:
            output = output[:-1] + f", props: {self.props})"
        return output
