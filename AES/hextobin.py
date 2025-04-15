import re

def hex_to_bin(hex_file, bin_file):
    with open(hex_file, 'r') as hexf:
        hex_data = hexf.read()
        
        # Remove any characters that are not hex digits (0-9, a-f, A-F)
        hex_data = re.sub(r'[^0-9a-fA-F]', '', hex_data)

    with open(bin_file, 'wb') as binf:
        binf.write(bytes.fromhex(hex_data))

hex_to_bin("AEScode.ino.hex", "AEScode.bin")
