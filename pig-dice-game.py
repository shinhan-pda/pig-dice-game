from random import randint, choice
from time import sleep

def game_start():
  player_num = int(input('플레이 인원 수를 정해주세요 (1~3) >> '))
  print('컴퓨터를 포함해 총 {}명이 플레이합니다.'.format(player_num + 1))
  print(f'모든 게임의 시작은 컴퓨터가 합니다.')

  global turn
  global order
  global order_limit

  turn = ['com']
  order = 0
  order_limit = player_num+1

  for i in range(1, player_num+1):
    turn.append('user' + str(i))

  return roll_dice(turn, order, order_limit)

def roll_dice(turn, order, order_limit):
    if order == order_limit:
      order = 0

    print(f'{turn[order]} 차례 주사위를 굴립니다.')
    sleep(1)

    dice = randint(1,6)
    print(f'{dice}가 나왔습니다.')

    if dice == 1:
      change_turn(turn, order)
    else:
      if order == 0:
        com_choose_roll(turn, order)
      else:
        user_choose_roll(turn, order)

def change_turn(turn, order):
  order += 1
  roll_dice(turn, order, order_limit)
  # 멈추고 점수 추가 할지 아님 더 굴릴지

def com_choose_roll(turn, order):
  choose = ['roll', 'stop']
  com_choose = choice(choose)

  if com_choose == 'roll':
    print(f"{com_choose}로 이어하겠습니다.")
    roll_dice(turn, order, order_limit)
    
  else:
    print(f"{com_choose}로 턴을 넘기겠습니다.")
    change_turn(turn, order)
    

def user_choose_roll(turn, order):
    user_choose = input('주사위를 굴리겠습니까?(roll or stop) >> ')

    if user_choose == 'roll':
        roll_dice(turn, order, order_limit)
    elif user_choose == 'stop':
      print(f"{user_choose}로 턴을 넘기겠습니다.")
      change_turn(turn, order)
    else:
      print('roll or stop 중 입력하십시오.')
      user_choose_roll(turn, order)

def choose_roll(turn):
  if turn == 'com':
    print('미완성')

bank = 0    # 임시점수(누적)
score = 0   # 총합점수 ## roll 시 나온 주사위 숫자dice 임시저장

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













>>>>>>> 052cb7a4ada7dbd9368e5de1b53258e1be1cacb4
