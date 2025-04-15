import re

def xor_encrypt_decrypt(data, key):
    # XOR decryption/encryption function
    return ''.join([chr(ord(c) ^ key) for c in data])

def extract_strings_from_bin(filename, key, min_length=4):
    with open(filename, 'rb') as bin_file:
        data = bin_file.read()

    # Convert binary data to string, then decrypt the XOR-encrypted content
    decrypted_data = xor_encrypt_decrypt(data.decode('latin1'), key)

    # Find sequences of printable characters (including control characters)
    strings = re.findall(r'.{%d,}' % min_length, decrypted_data)

    return strings

def save_strings_to_file(strings, output_filename="extracted_strings.txt"):
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for string in strings:
            output_file.write(string + '\n')

if __name__ == "__main__":
    # Replace with your binary file and XOR key
    bin_file = "Obfuscationcode.bin"
    key = 0xAA  # XOR key used in the Arduino code
    extracted_strings = extract_strings_from_bin(bin_file, key)

    print("\nExtracted Strings:")
    for s in extracted_strings:
        print(s)
    
    # Save extracted strings to a text file
    save_strings_to_file(extracted_strings)

    print(f"\nStrings have been saved to 'extracted_strings.txt'")
