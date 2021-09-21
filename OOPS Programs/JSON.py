BOOK = {}

BOOK ['Fatha'] = {
    'name' == 'Fatha'
    'address' == 'Bangalore'
    'number' == 9898989898
}

BOOK ['Mohammad'] = {
    'name' == 'Mohammad'
    'address' == 'Pune'
    'number' == 9898967388
}

import json

s = json.dumps(BOOK)

print(s)
