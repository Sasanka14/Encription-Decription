# AES Encryption and Decryption

This project demonstrates the implementation of AES (Advanced Encryption Standard) encryption and decryption for secure communication between a client and a server. The project includes functionalities for encrypting and decrypting messages, benchmarking AES performance, and handling encrypted communication over a network.

## Project Files

1. **aes.py**: Contains the core AES encryption and decryption functions.
2. **benchmark.py**: Measures and plots the encryption and decryption times for different message sizes.
3. **client.py**: Implements the client-side program to send encrypted messages to the server.
4. **server.py**: Implements the server-side program to receive and decrypt messages from the client.

## Requirements

- Python 3.x
- `pycryptodome` library for AES encryption
- `matplotlib` library for plotting the performance benchmark

You can install the required dependencies using pip:

```bash
pip install pycryptodome matplotlib
```

## How It Works

### 1. **AES Encryption & Decryption**

- **encrypt_message(message, secret_key)**: Encrypts a given plaintext message using AES in CBC mode. It returns the encrypted message, including the Initialization Vector (IV) concatenated with the ciphertext.
  
- **decrypt_message(encrypted_message, secret_key)**: Decrypts an encrypted message by extracting the IV and ciphertext, then using AES in CBC mode with the provided secret key to recover the original plaintext message.

### 2. **Benchmarking AES Performance**

- **benchmark_aes_performance()**: This function benchmarks the time taken for encryption and decryption for different message sizes (128, 256, 512, 1024, and 2048 bytes) and plots the results using `matplotlib`. It shows how the time varies with message size.

### 3. **Client-Server Communication**

- **client.py**: The client program connects to the server, takes input from the user, encrypts the message using AES, and sends the encrypted message to the server.
  
- **server.py**: The server listens for incoming encrypted messages from the client, decrypts them, and displays the decrypted message. After the communication ends, the server runs the AES performance benchmark.

## Usage

1. **Start the Server**: Run `server.py` to start the server.
   ```bash
   python server.py
   ```
   The server will listen for incoming connections on `127.0.0.1:5000`.

2. **Start the Client**: Run `client.py` to start the client.
   ```bash
   python client.py
   ```
   The client will connect to the server and prompt you to enter a message. The message will be encrypted using AES and sent to the server.

3. **Benchmarking**: After the communication ends, the server will automatically run the performance benchmark, displaying the time taken for encryption and decryption for various message sizes.

## Example Output

### Client Output:
```
Enter 'exit' to quit.
Enter message: Hello, server!
Encrypted message: b'...'
```

### Server Output:
```
Server listening on 127.0.0.1:5000...
Connection established with ('127.0.0.1', 12345)
Encrypted message received: b'...'
Received message: Hello, server!
```

### Benchmark Plot:
A plot showing the encryption and decryption times for different message sizes will be displayed after the server finishes processing.
![image](https://github.com/user-attachments/assets/8449c953-f931-4d13-b286-43984279d7a5)


## Contributing

Feel free to fork the repository and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**GitHub Repository:** [https://github.com/Sasanka14/AES-Encryption-and-Decryption](https://github.com/Sasanka14/Encription-Decription.git)
