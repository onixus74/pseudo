from pseudon.code_generator import CodeGenerator


class PythonGenerator(CodeGenerator):
    '''Python code generator'''

    def body(self, node, indent):
        if node.body:
            return self.render_nodes(node.body, indent)
        else:
            return '%spass\n' % self.offset(indent)

    def methods(self, node, indent):
        if node.methods:
            return self.render_nodes(node.methods, indent)
        else:
            return '%spass\n' % self.offset(indent)

    def to_boolean(self, node, indent):
        if node.value == 'true':
            return self.offset(indent) + 'True'
        else:
            return self.offset(indent) + 'False'

    templates = {
        'module': "%<code>",

        'function': '''
                    def %<name>(%<args:join ','>):
                        %<#body>
                    ''',

        'class':  '''
                  class %<name>%?<(%<parent>)>:
                      %<#methods>
                  ''',

        'local': '%<name>',
        'typename': '%<name>',
        'int': '%<value>',
        'float': '%<value>',
        'string': safe_single,
        'boolean': to_boolean,
        'null':   'None'
    }
