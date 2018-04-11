from socket import *
import selectors

sel = selectors.DefaultSelector()
def accept(server_fileobj,mask):
    conn,addr = server_fileobj.accept()
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    try:
        data = conn.recv(1024)
        if not data:
            print("closing",conn)
            sel.unregister(conn)
            conn.close()
            return
        conn.send(data.upper()+b"_SB")
    except Exception:
        print("closing",conn)
        sel.unregister(conn)
        conn.close()
server_fileobj = socket(AF_INET,SOCK_STREAM)
server_fileobj.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_fileobj.bind(("127.0.0.1",8080))
server_fileobj.listen(5)
server_fileobj.setblocking(False)  #设置socket的接口为非阻塞
sel.register(server_fileobj,selectors.EVENT_READ,accept)
# 相当于往select的读列表里append了一个文件句柄server_fileobj,并且绑定了一个回调函数accept

while True:
    events = sel.select() #检测所有的fileobj,是否有完成wait data的
    for sel_obj,mask in events:
        callback = sel_obj.data #callback = accept
        callback(sel_obj.fileobj,mask) #accpt(server_fileobj,1)