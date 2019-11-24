import learn_random
r = learn_random.randint(1, 100)
while True:
    num = input('請猜數字')
    num = int(num)
    if num == r:
        print("你猜中了")
        break
    elif num > r :
        print("再猜小一點")
    elif num < r :
        print("再猜大一點")
    else:
        break