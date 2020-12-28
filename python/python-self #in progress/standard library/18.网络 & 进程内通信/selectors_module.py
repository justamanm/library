# !!!epoll只适用与linux系统
# epoll实现http多任务

import select
import socket


tcp_socket = socket.socket()

# 1.创建一个epoll对象
epoll = select.epoll()

# 2.将监听套接字对应的fd放到epoll中，并绑定事件，输入触发
epoll.register(tcp_socket.fileno(), select.EPOLLIN)

"""3.接收epoll检测到的事件及其对应的socket文件描述符，默认堵塞，直到内核检测到数据通知程序，才会解堵塞
之前使用while True，内部设置非堵塞；所以一直在占用cpu资源；而有事件发生才执行，否则挂起，减少资源占用
返回列表[(fd,event)，(fd,event) . . .]，event即EPOLLIN或EPOLLOUT"""
fd_event_list = epoll.poll()

"""4.循环遍历列表，如果fd是接收客户端连接的socket，则程序调accept()；如果是与客户端连接的socket，且事件是发送数据，则调recv()
因为循环中只有fd，所以需要创建字典，保存accept()得到的new_socket，之后通过键fd来取得各new_socket"""
fd_event_dict = dict()

while True:  # 用来刷新新的事件
    fd_event_list = epoll.poll()

    for fd, event in fd_event_list:
        if fd == tcp_socket.fileno():
            new_socket, client_addr = tcp_socket.accept()
            epoll.register(new_socket.fileno(), select.EPOLLIN)
            # 通过字典保存socket，键为fd,值为socket
            fd_event_dict[new_socket.fileno()] = new_socket
        elif event == select.EPOLLIN:
            # 判断已经链接的客户端是否有数据发送过来
            recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
            if recv_data:
                # 处理数据
                print(recv_data.decode())