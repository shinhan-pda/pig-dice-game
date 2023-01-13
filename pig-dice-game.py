bank = 0    # 임시점수(누적)
score = 0   # 총합점수(누적)

## roll 시 나온 주사위 숫자dice 임시저장

# 만약 사용자가 roll을 입력한다면
def num_bank(dice):
    if dice != 1:       # 1이 아닌 경우 임시저장
        bank += dice
    else:               # 1인 경우 임시점수 초기화
        bank = 0


## Stop 시 임시저장된 점수 총합 점수에 저장

# 만약 사용자가 stop을 입력한다면
def store(bank):
    score += bank       # 총합점수에 저장
    if score >= 50:     # 총점이 50이 넘는다면 게임 종료
        print(f"{username} 이 이겼습니다!")
        break













