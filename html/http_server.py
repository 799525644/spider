# socket 服务端，访问端口，以http形式返回内容
import json
import socket
import threading

# 1.调用sokcet()创建套接字
server = socket.socket()
# 这句话可以使socket关闭后，操作系统不保留端口，立即释放
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 2.调用bind()绑定本地ip和端口：绑定到0.0.0.0:8000 port
server.bind(('0.0.0.0', 8000))
# 3.调用listen()监听端口
server.listen()


# 4 获取客户端连接并启动线程去处理，并注释4；此时每来一个新用户运行一个模式
# Thread()方法中需要用方法而是不方法名的调用
def handle_sock(sock, addr):
    while True:
        # recv方法是阻塞的
        tmp_data = sock.recv(1024*10)
        tmp_data = tmp_data.decode("utf8")
        request_line = tmp_data.splitlines()[0]

        if request_line:
            method = request_line.split()[0]
            path = request_line.split()[1]
            if method == "GET":
                response_template = '''HTTP/1.1 200 OK
Access-Control-Allow-Origin:http://localhost:63342

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/" method="POST" enctype="multipart/form-data">
    <input type="text" name="name"/>
    <input type="password" name="password">
    <input type="file" name="file">
    <input type="submit" value="登录">
</form>

</body>
</html>

'''
            sock.send(response_template.encode("utf8"))
            sock.close()
        elif method == "POST":
            response_template = '''HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: http://localhost:63342

{}

            '''
            data = [
                {
                    "name": "django打造在线教育",
                    "teacher": "bobby",
                    "url": "https://coding.imooc.com/class/78.html"
                },
                {
                    "name": "python高级编程",
                    "teacher": "bobby",
                    "url": "https://coding.imooc.com/class/200.html"
                },
                {
                    "name": "scrapy分布式爬虫",
                    "teacher": "bobby",
                    "url": "https://coding.imooc.com/class/92.html"
                },
                {
                    "name": "django rest framework打造生鲜电商",
                    "teacher": "bobby",
                    "url": "https://coding.imooc.com/class/131.html"
                },
                {
                    "name": "tornado从入门到精通",
                    "teacher": "bobby",
                    "url": "https://coding.imooc.com/class/290.html"
                },
            ]
            sock.send(response_template.format(json.dumps(data)).encode("utf8"))
            sock.close()
            break
while True:
    # 阻塞等待连接
    sock, addr = server.accept()
    # 启动线程去处理新的用户连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()


