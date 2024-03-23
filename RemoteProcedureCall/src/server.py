import socket
import json
import math

# 10進数 x を最も近い整数に切り捨て、その結果を整数で返す
def floor(x):
    return (int) (x - (x % 1))

# 
def nroot(n, x):
    return math.pow(x, 1/n)

# 入力文字列の逆である文字列を返す
def reverse(str):
    reverse_str = ''
    for i in range(len(str)):
        reverse_str += str[len(str) - i - 1]
    return reverse_str

# 引数のJSON文字列を元に特定の関数を呼び出す
def rpcFunction(json):
    method = json['method']
    params = json['params']
    print('===== Pamrams:  ==> {}'.format(params[0]))
    
    response = ''
    if method == 'floor':
        response = {
            "results": floor(params[0]),
            "result_type": "int",
            "id": json['id']
        }
    elif method == 'nroot': 
        response = {
            "results": nroot(params[0], params[1]),
            "result_type": "double",
            "id": json['id']
        }
    elif method == 'reverse':
        response = {
            "results": reverse(params[0]),
            "result_type": "string",
            "id": json['id']
        }
        
    print('===== Response: <== {} '.format(response['results']))
    return response

# AF_INETをストリームモードで作成 (AF_UNIXではhostとportの指定ができない)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバのホストとポート番号を設定
server_address = ('localhost', 50000)

print('Starting up on {}:{}'.format(*server_address))

# サーバアドレスにソケットをバインド(接続)
sock.bind(server_address)

# ソケットが接続要求を待機するように設定
sock.listen(1)

# 無限ループでクライアントからの接続を待機
while True:
    # クライアントからの接続を許可
    connection, client_address = sock.accept()
    try:
        print('Connection from: ', client_address)

        # ループ開始(サーバが新しいデータの待機を継続する)
        while True:
            # データの受信
            data = connection.recv(1024)

            # 受け取ったデータはバイナリ形式なので、それを文字列に変換します。
            # 'utf-8'は文字列のエンコーディング方式です。
            data_str =  data.decode('utf-8')
            
            try:
                # JSON文字列に変換する
                data_json = json.loads(data_str)
                # 受け取ったデータを表示します。
                print('Received data: ' + data_json["method"])
            except Exception:
                pass
            
            # クライアントからメッセージを受信した場合
            if data:
                # RPC関数を用いてメッセージを送信 (strをencodeする)
                connection.sendall(json.dumps(rpcFunction(data_json)).encode())

            # クライアントからデータが送られてこなければ、ループを終了します。
            else:
                print('no data from', client_address)
                break

    # 最終的に接続を閉じます
    finally:
        print("Closing current connection")
        connection.close()