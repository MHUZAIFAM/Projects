def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def text_to_decimal(text):
    return ' '.join(str(ord(c)) for c in text)

def text_to_hex(text):
    return text.encode().hex()
