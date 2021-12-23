# socket 服务端
import socket

# 1.调用sokcet()创建套接字
server = socket.socket()

# 2.调用bind()绑定本地ip和端口：绑定到0.0.0.0:8000 port
server.bind(('0.0.0.0', 8000))

# 3.调用listen()监听端口
server.listen()

# 4.调用accept() 等待连接, 若无连接则阻塞等待
sock, addr = server.accept()

# 5.1调用recv()等待传输的数据实现单向接收
# data = ""
# while True:
#     tmp_data = sock.recv(1024)
#     if tmp_data:
#         data += tmp_data.decode("utf8")
#         if tmp_data.decode("utf8").endswith("#"):
#             break
#     else:
#         break;
# print(data)


# 5.2调用recv()和send()实现服务端和客户端的双向通信
# 向客户端表示连接成功
data = ""
if True:
    sock.send("哈！你终于连上了!".encode("utf8"))
    while True:
        tmp_data = sock.recv(1024)
        print(tmp_data.decode("utf8"))
        input_data = input()
        sock.send(input_data.encode("utf8"))

# 6.调用close关闭套接字
sock.close()


