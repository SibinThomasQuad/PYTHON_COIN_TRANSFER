import socket

HOST = 'localhost'
PORT = 8080

def receive_coins():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print('Server started. Listening for connections...')

        conn, addr = server_socket.accept()
        with conn:
            print('Connected by:', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                amount = float(data.decode())
                print(f'Received coins: {amount}')
                # Process the received coins or update account balance
                # Here, we are just printing the received amount

if __name__ == '__main__':
    receive_coins()
