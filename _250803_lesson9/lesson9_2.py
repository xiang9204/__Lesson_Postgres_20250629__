import argparse
import random

def get_user_name()->str:
    """
    取得使用者姓名的函式

    這個函式可以透過命令列參數或是手動輸入來取得使用者姓名。

    Returns:
        str: 使用者的姓名

    命令列參數:
        -n, --name: 使用者姓名
        -f, --frequency: 遊戲次數 (預設值為1)

    範例:
        >>> get_user_name()  # 如果沒有提供命令列參數，會提示使用者輸入姓名
        請輸入您的姓名:王小明
        '王小明'

        >>> get_user_name()  # 使用命令列參數
        # python script.py -n 王小明
        '王小明'
    """


    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name

def play_game(name:str)->None:
    """一個猜數字遊戲的函式。

    這個遊戲會隨機產生一個1-100之間的數字，讓玩家來猜。
    每次猜測後會提示太大或太小，直到猜對為止。

    參數:
        name (str): 玩家的名字

    回傳:
        None

    功能:
        - 隨機產生1-100之間的目標數字
        - 提供玩家輸入數字進行猜測
        - 顯示猜測範圍和次數
        - 判斷玩家輸入是否在有效範圍內
        - 提供太大或太小的提示
        - 記錄並顯示總猜測次數
    """

    i = 0
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")




# main
def main():
    frequency = 1
    name = get_user_name()
    for i in range(frequency):
        play_game(name)
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()