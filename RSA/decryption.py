from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Decrypt the AES key with the RSA private key
def decrypt_aes_key(encrypted_aes_key, private_key_file):
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    # Decrypt the AES key using the RSA private key
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return aes_key

# Decrypt the file using AES encryption
def decrypt_file(input_file, private_key_file, output_file):
    with open(input_file, 'rb') as f:
        # Read the encrypted AES key (first part of the file)
        encrypted_aes_key = f.read(256)  # RSA key size (2048 bits = 256 bytes)

        # Read the IV (16 bytes for AES)
        iv = f.read(16)

        # Read the encrypted file data
        encrypted_data = f.read()

    # Decrypt the AES key using the RSA private key
    aes_key = decrypt_aes_key(encrypted_aes_key, private_key_file)

    # Decrypt the file using AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB8(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Write the decrypted file data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Decrypt the encrypted file
decrypt_file("code2_encrypted_rsa.bin", "private_key.pem", "code2_decrypted.ino")
