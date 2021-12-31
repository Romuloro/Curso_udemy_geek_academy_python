"""
Pickle

A função do Pickle é realizar um seguinto processo:

Objeto python - Binarização
Binarização - Objeto Python


JSON - Javascript objetic notation

API - meios de comunicação oferecidos por empresas e tercieros (desenvolvedores).
"""

import json

ret = json.dumps(['produto', {'Play 4': ('2TB', 'Novo', '220V', 4000)}])
print(type(ret))
print(ret)

