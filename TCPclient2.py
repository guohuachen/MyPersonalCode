import socket
import threading
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_msg(conn):
    while True:
        msg=input()
        conn.send(msg.encode("utf-8"))
def recv_msg(conn):
    while True:
        try:
            recvmsg=conn.recv(1024)
        except BlockingIOError as e:
            recvmsg = None
        if recvmsg:
            print("服务端说：",recvmsg.decode("utf-8"))
if __name__ == '__main__':
    conn.connect(('127.0.0.1', 80))
    conn.setblocking(0)
    client_send=threading.Thread(target=send_msg,args=[conn])
    client_send.start()
    client_recv=threading.Thread(target=recv_msg,args=[conn])
    client_recv.start()

