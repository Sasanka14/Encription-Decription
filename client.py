import socket
from aes import encrypt_message

# Function to send encrypted messages
def client_program():
    host = '127.0.0.1'  # Server's IP
    port = 5000          # Port to connect to
    secret_key = b'my_secret_key_16'  # AES secret key
    
    client_socket = socket.socket()  # Create socket object
    client_socket.connect((host, port))  # Connect to the server
    
    print("Enter 'exit' to quit.")
    
    try:
        while True:
            # Input message from the user
            message = input("Enter message: ")
            if message.lower() == 'exit':
                print("Exiting...")
                break
            
            # Encrypt the message
            encrypted_message = encrypt_message(message, secret_key)
            
            # Display encrypted message in client terminal
            print(f"Encrypted message: {encrypted_message}")
            
            # Send the encrypted message
            client_socket.send(encrypted_message)
    
    except KeyboardInterrupt:
        print("\nClient exiting...")

    finally:
        client_socket.close()  # Close the connection
        print("Client closed.")

if __name__ == '__main__':
    client_program()
