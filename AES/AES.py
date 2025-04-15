from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = bytes([
    0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe,
    0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81
])

msg = b"Secret message"  # 18 chars
padded = pad(msg, 16)
cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(padded)

print(", ".join(f"0x{b:02x}" for b in enc))
