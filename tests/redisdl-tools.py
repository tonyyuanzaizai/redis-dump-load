#!/usr/bin/env python
# python 3.9.3

import redisdl


def tool_dump():
    with open('./dump0909.json', 'w') as f:
        # streams data
        redisdl.dump(f, host='0.0.0.0', port=6379, password='0', ssl=True)



def tool_load():
    with open('./dump0909.json') as f:
        # streams data if ijson or jsaone are installed
        redisdl.load_lump(f, host='1.1.1.1', port=6379, password='1', ssl=True)



tool_load()