import base64
import random
import string


def encrypt(plaintext: str, key: str) -> str:
    key_stream = [ord(key[i % len(key)]) for i in range(len(plaintext))]
    encrypted = bytes([ord(p) ^ k for p, k in zip(plaintext, key_stream)])
    return base64.b64encode(encrypted).decode('utf-8')


def decrypt(ciphertext: str, key: str) -> str:
    try:
        encrypted_bytes = base64.b64decode(ciphertext)
        key_stream = [ord(key[i % len(key)]) for i in range(len(encrypted_bytes))]
        decrypted = ''.join(chr(c ^ k) for c, k in zip(encrypted_bytes, key_stream))
        return decrypted
    except Exception:
        raise ValueError("Decryption failed. Check the key and input format.")


def generate_random_key(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def evaluate_key_strength(length: int) -> str:
    if length < 8:
        return "Weak"
    elif length < 16:
        return "Moderate"
    else:
        return "Strong"
    
