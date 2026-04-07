def pluralize(noun):
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    else:
        return noun + 's'

words = ["cat", "bus", "baby", "box"]

for w in words:
    print(w, "->", pluralize(w))
