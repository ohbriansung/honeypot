import socket
import sys
import threading
import paramiko

from _thread import start_new_thread

KEY = paramiko.RSAKey(filename='server.key')
PORT = 2222
LOGFILE = 'login.txt'
LOGFILE_LOCK = threading.Lock()


class SSHServerHandler(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        LOGFILE_LOCK.acquire()
        try:
            with open(LOGFILE, 'a') as logfile_handle:
                print(username + ':' + password)
                logfile_handle.write(username + ':' + password + '\n')
        finally:
            LOGFILE_LOCK.release()
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'


def handld_connection(client):
    transport = paramiko.Transport(client)
    transport.add_server_key(KEY)

    server_handler = SSHServerHandler()

    transport.start_server(server=server_handler)

    channel = transport.accept(1)
    if channel is not None:
        channel.close()


if __name__ == '__main__':
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', PORT))
        server_socket.listen(100)

        paramiko.util.log_to_file('paramiko.log')

        while True:
            try:
                client_socket, client_addr = server_socket.accept()
                start_new_thread(handld_connection, (client_socket,))
            except Exception as e:
                print('ERROR: Client handling')
                print(e)

    except Exception as e:
        print('ERROR: Failed to create socket')
        print(e)
        sys.exit(1)
