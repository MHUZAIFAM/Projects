from text_conversions import text_to_binary, text_to_decimal, text_to_hex
from binary_conversions import binary_to_text, binary_to_decimal, binary_to_hex
from decimal_conversions import decimal_to_text, decimal_to_binary, decimal_to_hex
from hex_conversions import hex_to_text, hex_to_binary, hex_to_decimal

def convert(input_data, input_type, output_type):
    input_type = input_type.lower()
    output_type = output_type.lower()

    converters = {
        'text': {
            'binary': text_to_binary,
            'decimal': text_to_decimal,
            'hex': text_to_hex
        },
        'binary': {
            'text': binary_to_text,
            'decimal': binary_to_decimal,
            'hex': binary_to_hex
        },
        'decimal': {
            'text': decimal_to_text,
            'binary': decimal_to_binary,
            'hex': decimal_to_hex
        },
        'hex': {
            'text': hex_to_text,
            'binary': hex_to_binary,
            'decimal': hex_to_decimal
        }
    }

    try:
        return converters[input_type][output_type](input_data)
    except KeyError:
        return "Invalid conversion types!"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("🧠 Universal Converter (Modular Version)\n")
    while True:
        print("\nSupported Types: text, binary, decimal, hex")
        source_type = input("From: ").strip()
        target_type = input("To: ").strip()
        value = input("Enter your value: ").strip()

        result = convert(value, source_type, target_type)
        print(f"➡️ Result: {result}")

        again = input("\nDo another conversion? (y/n): ").strip().lower()
        if again != 'y':
            break
