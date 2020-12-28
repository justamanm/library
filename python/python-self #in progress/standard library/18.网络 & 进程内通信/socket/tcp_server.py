import socket
import time


def main():
    server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp.bind(("127.0.0.1", 12345))
    print("开始监听12345端口")
    server_tcp.listen(128)

    while True:
        new_tcp, client_addr = server_tcp.accept()
        print("客户端已连接")

        # 发送消息
        content = "aaa"
        # content = input("请输入要发送的文字：")
        new_tcp.send(content.encode())
        # a = input("input something:")
        # recv_data = new_tcp.recv(1024)
        # if not recv_data:
        #     print("客户端断开连接")
        # time.sleep(5)
        # 接收客户端消息
        # recv_data = new_tcp.recv(1024)
        # print("%s发送了信息：%s" % (client_addr, recv_data.decode()))
        # if recv_data:
        #     new_tcp.send("消息接收成功".encode())
        # time.sleep(20)

    server_tcp.close()
    new_tcp.close()


if __name__ == '__main__':
    main()
    # print(""==None)
