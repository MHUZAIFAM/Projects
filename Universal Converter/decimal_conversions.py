def decimal_to_text(decimal):
    return ''.join(chr(int(d)) for d in decimal.split())

def decimal_to_binary(decimal):
    return ' '.join(format(int(d), '08b') for d in decimal.split())

def decimal_to_hex(decimal):
    return ' '.join(hex(int(d))[2:] for d in decimal.split())
