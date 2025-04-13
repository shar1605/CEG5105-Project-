"""
Finds strings from .ino hex files, which can be attained via Arduino -> Export 
Compiled Binary
"""


import sys
import re
from intelhex import IntelHex

def extract_strings_from_bin(filename, min_length=4):
    intel_hex = IntelHex(filename)
    data = intel_hex.tobinarray()

    # Printable ASCII characters
    strings = re.findall(rb"[ -~]{%d,}" % min_length, data)

    decoded_strings = [s.decode("utf-8", errors="ignore") for s in strings]

    return decoded_strings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_strings.py <file.ino.bin>")
        sys.exit(1)

    bin_file = sys.argv[1]
    extracted_strings = extract_strings_from_bin(bin_file)

    print("\nExtracted Strings:")
    for s in extracted_strings:
        print(s)