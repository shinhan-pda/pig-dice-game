from random import randint
from time import sleep

player_num = int(input())





def roll_dice():
    print('주사위를 굴립니다.')
    sleep(1)
    
    dice = randint(1,6)
    print(f'{dice}가 나왔습니다.')














