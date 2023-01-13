from random import randint

turn = 1    # turn이 1이면 roll, 0이면 stop

# 컴퓨터가 언제 턴을 넘길지(언제까지 roll?)
go = randint(0, 1)

if go == 1:     # 1이면 계속 진행
    turn = 1
else:           # 0이면 턴 넘기기
    turn = 0

