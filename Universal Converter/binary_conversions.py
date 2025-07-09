def binary_to_text(binary):
    return ''.join(chr(int(b, 2)) for b in binary.split())

def binary_to_decimal(binary):
    return ' '.join(str(int(b, 2)) for b in binary.split())

def binary_to_hex(binary):
    return ' '.join(hex(int(b, 2))[2:] for b in binary.split())
