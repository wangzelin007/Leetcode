import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234))
    s.sendall(b"Hello Socket!")
    data = s.recv(1024)
    # 将对象转化为供解释器读取的形式。
    print("Received:", repr(data))