import sys
import random

## ランダムな数字を当てるゲーム
## 最大値と最小値を任意で入力し、5回以内にその範囲内のランダムな数字を当てる

# 最小値の入力
sys.stdout.buffer.write(b'Write Minimum Number: ')
sys.stdout.flush()
min = int(sys.stdin.buffer.readline().decode())
# 最大値の入力
sys.stdout.buffer.write(b'Write Max Number: ')
sys.stdout.flush()
max = int(sys.stdin.buffer.readline().decode())

# 乱数の生成
random.seed()
rand = random.randint(min, max)

# ユーザの推測値真偽判定
print('Guess The Random Number!\n')
for i in range(5):
    sys.stdout.buffer.write(b'Write Guess Number: ')
    sys.stdout.flush()
    guess = int(sys.stdin.buffer.readline().decode())
    if (guess == rand):
        print('Correct Answer!!\n')
        break

# ゲーム終了
print('Random Number is ', rand, ' And Finish The Game')





