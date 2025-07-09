def hex_to_text(hex_str):
    return bytes.fromhex(hex_str.replace(" ", "")).decode()

def hex_to_binary(hex_str):
    return ' '.join(format(int(h, 16), '08b') for h in hex_str.split())

def hex_to_decimal(hex_str):
    return ' '.join(str(int(h, 16)) for h in hex_str.split())
