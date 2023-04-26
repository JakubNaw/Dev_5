import logging as log

def sub(a, b):
    return float(a - b)

def mul(a, b):
    return float(a * b)

def div(a, b):
    if b != 0:
        return a/b
    print("dividing by 0")
    return None

def avg():
    log.warning('warning')
