import socket
import os

"""オンラインチャットメッセンジャー
stage1: クライアントがUDPを用いてサーバに接続。サーバに送信したメッセージが他の全てのクライアントに中継される。
stage2: 自分専用のチャットルームを作成する機能を有する。他のクライアントはチャットルームに参加してコミュニケーションが可能。
stage3: GUIを有し、共有メモリを利用したマルチプロセスチャットルームの作成が可能。    
"""

# UDPソケットオブジェクトの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# サーバアドレス、ポートの設定
server_address = '0.0.0.0'
server_port = 9001

# ソケットをサーバのアドレス、ポートに紐付ける
sock.bind((server_address, server_port))

try:
    while True:
        # クライアントからの接続を許可
        print('クライアントからのメッセージを待機しています...\n')
        data, address = sock.recvfrom(4096)      
        print('クライアントからメッセージを受信しました...\nデータ量: {}bytes\nアドレス: {}'.format(len(data), address))
        
        if data:
            # 全クライアントにデータ送信
            print('受信データ: {}\n'.format(data.decode('utf-8')))
            sock.sendto(data, address)

except KeyboardInterrupt:
    pass

finally:
    print('サーバを停止します\n')
    sock.close()
        
    
