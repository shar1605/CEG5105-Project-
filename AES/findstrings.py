import sys
import re

def extract_strings_from_bin(filename, min_length=4):
    with open(filename, 'rb') as bin_file:
        data = bin_file.read()

    # Find sequences of printable characters (including control characters)
    # This regex will match sequences of any byte (0-255) that have a minimum length
    strings = re.findall(rb".{%d,}" % min_length, data)

    # Decode bytes to string, ignoring errors
    decoded_strings = [s.decode("utf-8", errors="ignore") for s in strings]

    return decoded_strings

def save_strings_to_file(strings, output_filename="extracted_strings.txt"):
    with open(output_filename, 'w', encoding='utf-8') as output_file:  # Use UTF-8 encoding
        for string in strings:
            output_file.write(string + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python findstrings.py <AEScode.bin>")
        sys.exit(1)

    bin_file = sys.argv[1]
    extracted_strings = extract_strings_from_bin(bin_file)

    print("\nExtracted Strings:")
    for s in extracted_strings:
        print(s)
    
    # Save extracted strings to a text file
    save_strings_to_file(extracted_strings)

    print(f"\nStrings have been saved to 'extracted_strings.txt'")
