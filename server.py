import socket
from aes import decrypt_message
from benchmark import benchmark_aes_performance  # Import the benchmarking function

def server_program():
    host = '127.0.0.1'  # Localhost
    port = 5000         # Port to bind to
    secret_key = b'my_secret_key_16'  # AES secret key
    
    server_socket = socket.socket()  # Create socket object
    server_socket.bind((host, port))  # Bind to IP and port
    server_socket.listen(1)           # Listen for one connection
    
    print(f"Server listening on {host}:{port}...")
    
    try:
        conn, address = server_socket.accept()  # Accept incoming connection
        print(f"Connection established with {address}")
        
        while True:
            # Receive the encrypted message from the client
            encrypted_message = conn.recv(1024)
            if not encrypted_message:
                print("Connection closed by client.")
                break
            
            # Display encrypted message in server terminal
            print(f"Encrypted message received: {encrypted_message}")
            
            # Decrypt the message
            decrypted_message = decrypt_message(encrypted_message, secret_key)
            print(f"Received message: {decrypted_message}")
    
    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        conn.close()  # Close the connection
        server_socket.close()  # Close the server socket
        print("Server closed.")

        # Run the benchmark after the server is closed
        print("Running AES performance benchmark...")
        benchmark_aes_performance()  # Call the benchmarking function

if __name__ == '__main__':
    server_program()
