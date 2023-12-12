import socket
import threading
import base64
import os
import argparse

# Encryption libraries (for educational purposes only, not recommended for real-world usage)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class ChatApp:
    def __init__(self):
        self.host = '127.0.0.1'  # Default IP address
        self.port = 12345  # Default port
        self.connected = False
        self.debug_mode = False
        self.encryption_enabled = False
        self.private_key = None
        self.public_key = None
        self.remote_public_key = None
        self.symmetric_key = None
        
    def start(self):
        print("Welcome to Secure Chat App!")
        self.print_help()
        
        while True:
            command = input("Enter command: ")
            self.handle_command(command)
            
    def handle_command(self, command):
        command_parts = command.split()
        
        if not command_parts:
            return
        
        main_command = command_parts[0].lower()
        
        if main_command == 'help':
            self.print_help()
        elif main_command == 'port':
            self.set_port(command_parts)
        elif main_command == 'ipaddress':
            self.set_ip_address(command_parts)
        elif main_command == 'connect':
            self.connect_to_user()
        elif main_command == 'setmode':
            self.set_encryption_mode(command_parts)
        elif main_command == 'mode':
            self.display_encryption_mode()
        elif main_command == 'send':
            self.send_message(command_parts)
        elif main_command == 'displayip':
            print(f"Local IP Address: {self.host}")
        elif main_command == 'displayport':
            print(f"Local Port: {self.port}")
        elif main_command == 'debug':
            self.toggle_debug_mode(command_parts)
        elif main_command == 'disconnect':
            self.disconnect()
        elif main_command == 'quit':
            exit()
        else:
            print("Invalid command. Type 'help' for a list of commands.")
    
    def print_help(self):
        print("""
        Supported Commands:
        help:           Displays information on available supported commands.
        
        port:           Sets the port used for incoming chat communications.
        
        ipaddress:      Sets the established IP address for the local user.
        
        connect:        Allows a user to connect to another user via the provided IP address and receiving port.
        
        setmode:        Followed by “u” or “e” allows the user to activate or deactivate encryption. u = unencrypted, e = encrypted.
        
        mode:           Displays information indicating if the chat is encrypted or not depending on the setmode setting.
        
        send:           The send command is followed by a simple short message that needs to be sent to another user already connected through their provided IP address and port.
        
        displayip:      Displays the IP address of the local chat application.
        
        displayport:    Displays the UDP port configured for the local chat application.
        
        debug:          Followed by “on” or “off” sets the application in debugging environment.
        
        disconnect:     Disconnects chat.
        
        quit:           Exit the application.
        """)
        
    def set_port(self, command_parts):
        if len(command_parts) == 2:
            try:
                new_port = int(command_parts[1])
                self.port = new_port
                print(f"Port set to {new_port}")
            except ValueError:
                print("Invalid port number")
        else:
            print("Usage: port <port_number>")
            
            
    def set_ip_address(self, command_parts):
        if len(command_parts) == 2:
            try:
                ip_check_list = command.parts[1].split('.')
            except ValueError:
                print("Invalid IP address. Use X.X.X.X")
                
            self.host = command_parts[1]
            print(f"IP Address set to {self.host}")
        else:
            print("Usage: ipaddress <ip_address>")
        
    def connect_to_user(self):
        if not self.connected:
            self.remote_host = input("Enter remote IP address: ")
            self.remote_port = int(input("Enter remote port: "))

            self.connected = True

            if self.encryption_enabled:
                self.generate_key_pair()
                self.send_public_key(self.remote_host, self.remote_port)
                self.receive_public_key(self.remote_host, self.remote_port)
                self.exchange_symmetric_key()

            threading.Thread(target=self.receive_messages, args=()).start()
            print("Connected to remote user.")
        else:
            print("Already connected to a user.")
        
    def set_encryption_mode(self, command_parts):
        if len(command_parts) == 2:
            mode = command_parts[1].lower()
            if mode == 'u':
                self.encryption_enabled = False
                print("Encryption disabled.")
            elif mode == 'e':
                self.encryption_enabled = True
                if self.symmetric_key == None:
                    key_input = input("Enter encryption key (must be 16, 24, or 32 bytes): ")
                    try:
                        self.symmetric_key = self.validate_and_adjust_key(key_input)
                        #console log
                        # print(f'symmetric_key in set_encryption_mode function: {self.symmetric_key}')
                    except ValueError as e:
                        print(f"Error: {e}")
                        return
                else:
                    print("Encryption enabled.")
            else:
                print("Invalid mode. Use 'u' for unencrypted or 'e' for encrypted.")
        else:
            print("Usage: setmode <u/e>")
            
    def validate_and_adjust_key(self, key):
        key_bytes = key.encode()
        key_length = len(key_bytes)
        if key_length not in {16, 24, 32}:
            raise ValueError("Invalid key size. Key must be 16, 24, or 32 bytes.")
        if key_length < 32:
            # Pad the key with zeros to make it 32 bytes
            key_bytes += b'\x00' * (32 - key_length)
        return key_bytes
    
    def display_encryption_mode(self):
        if self.encryption_enabled:
            print("Encryption is enabled.")
        else:
            print("Encryption is disabled.")
            
    def send_message(self, command_parts):
        if len(command_parts) > 1:
            message = ' '.join(command_parts[1:]) 
            if self.connected:
                if self.encryption_enabled:
                    if self.symmetric_key:
                        encrypted_message = self.encrypt_message(message)
                        self.send_encrypted_message(encrypted_message, self.remote_host, self.remote_port)
                        #console log
                        # print(f'symmetric_key in send_message function: {self.symmetric_key}')
                    else:
                        print("Symmetric key is not available. Make sure to establish a connection and exchange keys.")
                else:
                    self.send_plain_message(message, self.remote_host, self.remote_port)
            else:
                print("Not connected to a user. Use 'connect' to establish a connection.")
        else:
            print("Usage: send <message>")
        
    def display_debug_message(self, message):
        if self.debug_mode:
            print(f"[DEBUG] {message}")
            
    def toggle_debug_mode(self, command_parts):
        if len(command_parts) == 2:
            mode = command_parts[1].lower()
            if mode == 'on':
                self.debug_mode = True
                print("Debug mode enabled.")
            elif mode == 'off':
                self.debug_mode = False
                print("Debug mode disabled.")
            else:
                print("Invalid mode. Use 'on' to enable or 'off' to disable.")
        else:
            print("Usage: debug <on/off>")      
            
            
    def disconnect(self):
        if self.connected:
            print("Disconnected from the remote user.")
            self.connected = False
        else:
            print("Not connected to any user.")
        
        
    def receive_messages(self):
        while True:
            message = self.receive_plain_message(self.host, self.port)
            if self.encryption_enabled:
                decrypted_message = self.decrypt_message(message)
                print(f"Received (Decrypted): {decrypted_message}")
            else:
                print(f"Received: {message}")
                
    def generate_key_pair(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        #console log
        # print(f'In generate_key_pair function: private_key: {self.private_key}')
        # print(f'public_key: {self.public_key}')

    def send_public_key(self, remote_host, remote_port):
        public_key_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        #console log
        # print(f'public_key_bytes in send_public_key function: {public_key_bytes}')

        self.send_plain_message(base64.b64encode(public_key_bytes).decode(), remote_host, remote_port)
        

    def receive_public_key(self, remote_host, remote_port):
        public_key_data = self.receive_plain_message(remote_host, remote_port)
        self.remote_public_key = serialization.load_pem_public_key(base64.b64decode(public_key_data), default_backend())
        #console log
        # print(f'received public key: public_key_data: {public_key_data}')
        # print(f'remote_public_key: {self.remote_public_key}')

    def exchange_symmetric_key(self):
        shared_key = self.private_key.decrypt(serialization.load_pem_public_key(base64.b64encode(self.remote_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode(), default_backend()))
        self.symmetric_key = base64.b64encode(shared_key).decode()
        self.display_debug_message(f"Symmetric key exchanged: {self.symmetric_key}")
        #console log
        # print(f'In exchange_symmertric_key function received symmetric_key: {base64.b64encode(shared_key).decode()}')
        # print(f'shared_key: {shared_key}')
            
            
    def encrypt_message(self, message):
        iv = os.urandom(16)  # Generate a random IV
        cipher = Cipher(algorithms.AES(self.symmetric_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        #console log
        # print(f'In encrypt_message function: padder: {padder}')
        # print(f'iv: {iv}')
        # print(f'cipher: {cipher}')
        # print(f'symmetric_key: {self.symmetric_key}')
        # print(f'padded_data: {padded_data}')
        # print(f'return: {base64.b64encode(iv + ciphertext).decode()}')

        return base64.b64encode(iv + ciphertext).decode()
    
    
    def send_encrypted_message(self, encrypted_message, remote_host, remote_port):
        self.send_plain_message(encrypted_message, remote_host, remote_port)

    def decrypt_message(self, encrypted_message):
        encrypted_data = base64.b64decode(encrypted_message)
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(self.symmetric_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        #console log
        # print('In decrypt_message function:')
        # print(f'Received symmetric key: {self.symmetric_key}')
        # print(f'unpadder: {unpadder}')
        # print(f'Encrypted data: {encrypted_data}')
        # print(f'iv: {iv}')
        # print(f'ciphertext: {ciphertext}')
        # print(f'cipher: {cipher}')
        # print(f'decrypted data: {decrypted_data}')
        # print(f'return: {unpadder.update(decrypted_data) + unpadder.finalize()}')

        return unpadder.update(decrypted_data) + unpadder.finalize()

    
    def send_plain_message(self, message, remote_host, remote_port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(message.encode(), (remote_host, remote_port))
            self.display_debug_message(f"Sent: {message} to {remote_host}:{remote_port}")
            s.close()

    def receive_plain_message(self, remote_host, remote_port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((remote_host, remote_port))
            data, addr = s.recvfrom(1024)
            self.display_debug_message(f"Received: {data} from {addr[0]}:{addr[1]}")
            s.close()
            return data.decode()         
            
            
   # Add command-line argument parsing using argparse
def parse_args():
    parser = argparse.ArgumentParser(description='Secure Chat Application')
    parser.add_argument('--port', type=int, help='Set the port for incoming chat communications')
    parser.add_argument('--ipaddress', type=str, help='Set the established IP address for the local user')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    chat_app = ChatApp()

    if args.port:
        chat_app.port = args.port
    if args.ipaddress:
        chat_app.host = args.ipaddress

    chat_app.start()