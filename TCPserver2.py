import socket
import threading
def send_msg(conn,addr):
    while True:
        msg=input()
        conn.send(msg.encode("utf-8"))
def recv_msg(conn,addr):
    while True:
        try:
            recvmsg=conn.recv(1024)
        except BlockingIOError as e:
            recvmsg=None
        if recvmsg :
            print("客户端说：",recvmsg.decode("utf-8"))
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen()
    conn,addr=s.accept()
    conn.setblocking(0)
    server_send = threading.Thread(target=send_msg, args=[conn, addr])
    server_send.start()
    server_recv = threading.Thread(target=recv_msg, args=[conn, addr])
    server_recv.start()