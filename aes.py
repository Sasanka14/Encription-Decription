from Crypto.Cipher import AES  # Import the AES cipher from the Crypto library
from Crypto.Util.Padding import pad, unpad  # Import functions for padding and unpadding messages
from Crypto.Random import get_random_bytes  # Import function to generate random bytes

# Function to encrypt a message
def encrypt_message(message, secret_key):
    """
    Encrypts a given plaintext message using AES encryption in CBC mode.

    Args:
        message (str): The plaintext message to encrypt.
        secret_key (bytes): A 16, 24, or 32-byte secret key used for encryption.

    Returns:
        bytes: The encrypted message (IV concatenated with ciphertext).
    """
    # Create a new AES cipher object in CBC mode with the provided secret key
    cipher = AES.new(secret_key, AES.MODE_CBC)
    
    # Encrypt the padded plaintext message
    # AES requires the input to be a multiple of the block size (16 bytes)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    
    # Return the IV (Initialization Vector) concatenated with the ciphertext
    # The IV is required for decryption
    return cipher.iv + ciphertext

# Function to decrypt a message
def decrypt_message(encrypted_message, secret_key):
    """
    Decrypts a given encrypted message using AES decryption in CBC mode.

    Args:
        encrypted_message (bytes): The encrypted message (IV + ciphertext).
        secret_key (bytes): A 16, 24, or 32-byte secret key used for decryption.

    Returns:
        str: The decrypted plaintext message.
    """
    # Extract the IV (Initialization Vector) from the first 16 bytes of the encrypted message
    iv = encrypted_message[:16]
    
    # Extract the actual ciphertext from the encrypted message (everything after the IV)
    ciphertext = encrypted_message[16:]
    
    # Create a new AES cipher object in CBC mode with the provided secret key and extracted IV
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext and remove padding
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    # Return the decrypted plaintext message as a string
    return decrypted_message.decode()
