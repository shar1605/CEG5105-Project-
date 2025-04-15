import re

def hex_to_bin(hex_file, bin_file):
    with open(hex_file, 'r') as hexf:
        hex_data = hexf.read()

        # Replace non-hex characters with their byte equivalent or a placeholder
        # For simplicity, we'll use '00' (which represents a null byte) for non-hex characters
        hex_data_with_nonhex = re.sub(r'[^0-9a-fA-F]', '00', hex_data)  # Replace non-hex with '00'

    with open(bin_file, 'wb') as binf:
        binf.write(bytes.fromhex(hex_data_with_nonhex))  # Write everything, now in valid hex format

hex_to_bin("Obfuscationcode.ino.hex", "Obfuscationcode.bin")
