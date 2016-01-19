from pseudon.types import *
from pseudon.api_translator import ApiTranslator


class CSharpTranslator(ApiTranslator):
    '''C# api translator'''

    api = {
        'List': {
            'Add': '#push',
            'Remove': {
                (-1, (t)): '#pop',
                (Int, (t)): '#remove'
            },
            '.Count': '#length'
        },
        'Dictionary': {
            '.Count': '#length'
        }
    }