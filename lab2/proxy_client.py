import socket, sys

def create_tcp_socket():
    print("Creaeting socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print('Failed to create socket. Error code: {}'.format(str(msg[0])))
        sys.exit()
    print("Successfully created socket")
    return s
    
def get_remote_ip(host):
    print('Getting IP for {}'.format(host))
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print("Host name could not be resolved")
        sys.exit()

    print('IP of address of {0} is {1}'.format(host, remote_ip))
    return remote_ip


def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except (socket.error, msg):
        print("Send failed")
        sys.exit()
    print("Send successfully")
    

def main():
    try:
        host = ''
        port = 8001
        payload = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
        buffer_size = 4096

        s = create_tcp_socket()
        remote_ip = get_remote_ip(host)

        s.connect((remote_ip, port))
        print()

        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(buffer_size)
            # print(data)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

if __name__ == "__main__":
    main()