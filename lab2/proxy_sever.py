import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 4096

def get_remote_ip(host):
    print('Getting IP for {}'.format(host))
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print("Host name could not be resolved")
        sys.exit()

    print('IP of address of {0} is {1}'.format(host, remote_ip))
    return remote_ip

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_s:
                full_data = conn.recv(BUFFER_SIZE)
                client_s.connect((get_remote_ip('www.google.com'), 80))
                client_s.sendall(full_data)
                client_s.shutdown(socket.SHUT_WR)

                google_data = b""
                while True:
                    data = client_s.recv(BUFFER_SIZE)
                    if not data:
                        break
                    google_data += data
                print(google_data)
                conn.sendall(google_data)
            conn.close()


if __name__ == "__main__":
    main()
