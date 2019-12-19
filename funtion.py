# function 函式/功能
# function 是用來【收納】程式碼的
# 它是個功能

def wash(dry):
    print('加水')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash(False)
wash(True)  # 使用function


def say_hi():
    print('hi!')


say_hi()

def add(x, y):
    print(x + y)
add(3, 4)
add(5, 5)

