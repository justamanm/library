import socket

"""TCP_client-接收文件"""
# def recv(tcp):
#     recv_data = tcp.recv(1024)
#     print("%s:%s" % (recv_data[1],recv_data[0].decode()))

# def send(tcp):
#     content = input()
#     tcp.send(content.encode())


def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ("192.168.0.63", 12345)
    # server_addr = ("", 9876)
    tcp.connect(server_addr)
    while True:
        # 发送给服务器消息
        send_data = input(":")
        tcp.send(send_data.encode())

        # 接收服务器的消息
        recv_data = tcp.recv(1024)
        print(recv_data.decode())

        # 如果接收到bye，则退出
        if send_data == "bye":
            break
    tcp.close()


if __name__ == '__main__':
    main()