import time
import matplotlib.pyplot as plt
from aes import encrypt_message, decrypt_message

def benchmark_aes_performance():
    # Benchmark encryption and decryption times
    message_sizes = [128, 256, 512, 1024, 2048]  # Message sizes in bytes
    encryption_times = []
    decryption_times = []
    secret_key = b'my_secret_key_16'  # Fixed secret key for AES

    for size in message_sizes:
        message = "A" * size  # Generate a message of the given size
        start_time = time.time()
        encrypted_message = encrypt_message(message, secret_key)
        encryption_times.append(time.time() - start_time)  # Time taken to encrypt

        start_time = time.time()
        decrypted_message = decrypt_message(encrypted_message, secret_key)
        decryption_times.append(time.time() - start_time)  # Time taken to decrypt

    # Plot the encryption and decryption times
    plt.figure(figsize=(10, 6))
    plt.plot(message_sizes, encryption_times, label="Encryption Time", marker='o')
    plt.plot(message_sizes, decryption_times, label="Decryption Time", marker='o')
    plt.title("Encryption and Decryption Time vs. Message Size")
    plt.xlabel("Message Size (Bytes)")
    plt.ylabel("Time (Seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    benchmark_aes_performance()
