import sys

# 入力ファイルパス
input_path = sys.argv[2]
# 実行コマンド
command = sys.argv[1]
# ファイルパスチェック
print(input_path)
if input_path.find('.txt') == -1:
    print('Select ".txt" File!')
    command = 'none'

# reverse関数
# 入力ファイルの内容を逆にした新しいファイルを作成する
def reverse():
    contents = ''
    # 入力ファイルの読み込み
    with open(input_path) as f:
        contents = f.read()
        # イテレータをリストに変換して文字列を連結 
        reversed_contents = ''.join(list(reversed(contents)))
    # 出力ファイルの作成
    output_path = sys.argv[3]
    with open(output_path, 'w') as f_out:
            f_out.write(reversed_contents)    
    return

# copy関数
# 入力ファイルの内容を出力先ファイルパスとしてコピーする
def copy():
    # 入力ファイルの読み込み
    with open(input_path) as f:
        # 出力ファイルの作成
        output_path = sys.argv[3]
        with open(output_path, 'w') as f_out:
            f_out.write(f.read())
    return

# duplicate-contents関数
# 入力ファイルの内容を指定された回数分複製して、入力ファイルに書き込む
def duplicate_contents():
    # 入力ファイルの読み込み
    with open(input_path) as f:
        contents = f.read()
    with open(input_path, 'a') as f_out:
        duplicate_number = int(sys.argv[3])
        # 指定された回数分複製して末尾に出力
        i = 0
        while i != duplicate_number:
            f_out.write('\n' + contents)
            i += 1
    return

# replace-string関数
# 入力ファイル内から文字列を検索し、指定した文字列に置換する
def replace_string():
    # 入力ファイルの読み込み
    contents = ''
    with open(input_path) as f:
        needle = sys.argv[3]
        new_string = sys.argv[4]
        contents = f.read()
        replace_str = contents.replace(needle, new_string)     
    #出力ファイルとして上書き
    with open(input_path, 'w') as f_out:
            f_out.write(replace_str)
    return

# 第2引数から実行コマンドの判別を行う
if command == 'reverse':
    reverse()
elif command == 'copy':
    copy()
elif command == 'duplicate':
    duplicate_contents()
elif command == 'replace':
    replace_string()
