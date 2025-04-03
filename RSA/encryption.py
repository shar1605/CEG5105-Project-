from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate RSA keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Save private key
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Save public key
    public_key = private_key.public_key()
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

# Encrypt the AES key with the RSA public key
def encrypt_aes_key(aes_key, public_key_file):
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_aes_key

# Encrypt the file using AES encryption
def encrypt_file(input_file, public_key_file, output_file):
    # Generate a random AES key
    aes_key = os.urandom(32)  # AES-256 key (32 bytes)

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)  # AES block size is 16 bytes

    # Encrypt the file with AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB8(iv), backend=default_backend())  # Pass IV here
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        data = f.read()

    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Encrypt the AES key with RSA
    encrypted_aes_key = encrypt_aes_key(aes_key, public_key_file)

    # Save the encrypted AES key and the encrypted file
    with open(output_file, 'wb') as f:
        f.write(encrypted_aes_key)  # First write the encrypted AES key
        f.write(iv)  # Write the IV used for AES encryption (needed for decryption)
        f.write(encrypted_data)     # Then write the encrypted file data

# Generate RSA keys
generate_rsa_keys()

# Encrypt a file
encrypt_file("code2.ino", "public_key.pem", "code2_encrypted_rsa.bin")
