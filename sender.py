import socket

HOST = 'localhost'
PORT = 8080

def send_coins(amount):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(str(amount).encode())
        print(f'Sent coins: {amount}')

if __name__ == '__main__':
    amount = 10.5  # Amount of coins to transfer
    send_coins(amount)
