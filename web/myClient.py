import socket, ssl, pprint, time, timeit, threading, queue

HOST = '172.16.20.5'

# 443 32825;8443 32826
HOST = '127.0.0.1'
# PORT = 32831
PORT = 8443
BUFSIZE = 1024
host, port, bufsize = HOST, PORT, BUFSIZE
try:
    # socket create success
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # require a cert
    #
    #
    # ificate from the server

    #   single authentication (单向验证)
    ssl_sock = ssl.wrap_socket(s,ca_certs="D:/myServer/myNginx/myClient4Test/jigCA/ca.crt",cert_reqs=ssl.CERT_REQUIRED)
    #   mutual authentication(双向验证)
    # ssl_sock = ssl.wrap_socket(s, ca_certs="jigCA/ca.crt", certfile="jigCA/client.crt", keyfile="jigCA/client.key",
    #                            cert_reqs=ssl.CERT_REQUIRED)

    # socket connect success
    ADDR = (host, port)
    ssl_sock.settimeout(5.0)
    ssl_sock.connect(ADDR)
    # note that closing the SSLSocket will also close the underlying socket
    pprint.pprint(ssl_sock.getpeercert())
    count = 0
    # while True:
    #     data = "hello this message from client"
    #     if not data:
    #         break
    #     count += 1
        # print(count, "  send data:", data)
    # time.sleep(1)
    for i in range(1):
        # User-Agent: PostmanRuntime/7.23.0
        # Accept: */*
        # Cache-Control: no-cache
        # Postman-Token: c6a39f3a-8073-4083-8850-9126c674cb20
        # Host: 127.0.0.1
        # Accept-Encoding: gzip, deflate, br
        # Connection: keep-alive
        #ssl_sock.send('GET / HTTP/1.1\r\n'.encode())
        # ssl_sock.send('User-Agent: \r\n'.encode())
        # ssl_sock.send('Accept: */*\r\n'.encode())
        # ssl_sock.send('Cache-Control: no-cache\r\n'.encode())
        #ssl_sock.send('Host: 127.0.0.1\r\n\r\n'.encode())
        # ssl_sock.send('Accept-Encoding: gzip, deflate, br\r\n'.encode())
        # ssl_sock.send('Connection: keep-alive\r\n\r\n'.encode())

        data = ssl_sock.recv(bufsize)
        if not data:
            print(f"sock {i} no data")
    # time.sleep(10)
    print("received data:", data.decode("utf-8"))
finally:
    ssl_sock