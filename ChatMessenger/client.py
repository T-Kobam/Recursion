import socket

# ソケットオブジェクトの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# サーバが接続待機しているポートにソケットを接続
server_address = '0.0.0.0'
server_port = 9001

# クライアント側のソケット情報
client_address = '0.0.0.0'
client_port = 9050

sock.bind((client_address, client_port))

try:
    while True:
        message = input('送信するメッセージを入力してください: ')
        if message == '終了':
            break
        
        # サーバにメッセージ送信
        sock.sendto(message.encode(), (server_address, server_port))
        
        # サーバからデータを受信
        data, address = sock.recvfrom(4096)
            
        if data:
            print('サーバからのメッセージ: {}\n'.format(data.decode()))
            
except KeyboardInterrupt:
    pass

finally:
    print('サーバとの通信を終了します')
    sock.close()
